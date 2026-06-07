from retriever import embed_and_store, get_collection, _client
from ingest import load_and_chunk
from config import CHROMA_COLLECTION, CHROMA_PATH, EMBEDDING_MODEL
from chromadb.utils import embedding_functions


def build_index(force=False):
    """
    Load chunks from ingest.py, embed them, and store in ChromaDB.
    Skips if already populated unless force=True.
    """
    collection = get_collection()

    if collection.count() > 0 and not force:
        print(f"Index already contains {collection.count()} chunks — skipping ingestion.")
        print("Delete chroma_db/ and re-run to force re-ingestion.")
        return

    if force and collection.count() > 0:
        _client.delete_collection(CHROMA_COLLECTION)
        _ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=EMBEDDING_MODEL
        )
        _client.get_or_create_collection(
            name=CHROMA_COLLECTION,
            embedding_function=_ef,
            metadata={"hnsw:space": "cosine"},
        )

    print("Loading and chunking documents...")
    chunks = load_and_chunk()
    print(f"  {len(chunks)} chunks ready for embedding.")

    print("Embedding and storing (first run downloads ~80 MB model)...")
    embed_and_store(chunks)
    print(f"Done. {CHROMA_PATH}")


if __name__ == "__main__":
    build_index()

    # Spot-check
    from retriever import retrieve
    print("\n--- Spot-check: 'AVL tree' ---")
    for chunk in retrieve("AVL tree", top_k=3):
        print(f"  [{chunk['course']} | {chunk['source']}] dist={chunk['distance']:.3f}")
        print(f"  {chunk['text'][:120]!r}\n")
