import os
import chromadb
from chromadb.utils import embedding_functions
from ingest import load_and_chunk

CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")
CHROMA_COLLECTION = "unofficial_guide"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)
_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function=_ef,
    metadata={"hnsw:space": "cosine"},
)


def get_collection():
    return _collection


def build_index(force=False):
    """
    Load chunks from ingest.py, embed them, and store in ChromaDB.
    Skips if already populated unless force=True.
    """
    if _collection.count() > 0 and not force:
        print(f"Index already contains {_collection.count()} chunks — skipping ingestion.")
        print("Run with force=True or delete chroma_db/ to re-ingest.")
        return

    if force and _collection.count() > 0:
        _client.delete_collection(CHROMA_COLLECTION)
        # Re-create after delete
        globals()["_collection"] = _client.get_or_create_collection(
            name=CHROMA_COLLECTION,
            embedding_function=_ef,
            metadata={"hnsw:space": "cosine"},
        )

    print("Loading and chunking documents...")
    chunks = load_and_chunk()
    print(f"  {len(chunks)} chunks ready for embedding.")

    # Build parallel lists for ChromaDB; IDs must be unique strings
    documents = [c["text"] for c in chunks]
    metadatas = [{"source": c["source"], "course": c["course"]} for c in chunks]
    ids = [f"{c['source']}_{i}" for i, c in enumerate(chunks)]

    print("Embedding and storing (first run downloads ~80 MB model)...")
    _collection.add(documents=documents, metadatas=metadatas, ids=ids)
    print(f"Done. {_collection.count()} chunks stored in {CHROMA_PATH}")


if __name__ == "__main__":
    build_index()

    # Spot-check: query for a known phrase and inspect results
    print("\n--- Spot-check: 'AVL tree' ---")
    results = _collection.query(
        query_texts=["AVL tree"],
        n_results=3,
        include=["documents", "metadatas", "distances"],
    )
    for text, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        print(f"  [{meta['course']} | {meta['source']}] dist={dist:.3f}")
        print(f"  {text[:120]!r}\n")
