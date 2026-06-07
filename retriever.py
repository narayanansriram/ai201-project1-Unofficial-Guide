import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_COLLECTION, CHROMA_PATH, EMBEDDING_MODEL, TOP_K, DISTANCE_THRESHOLD

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


def embed_and_store(chunks):
    """Embed a list of chunks and store them in ChromaDB."""
    _collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"], "course": c["course"]} for c in chunks],
        ids=[f"{c['source']}_{i}" for i, c in enumerate(chunks)],
    )
    print(f"Stored {_collection.count()} total chunks in the vector database.")


def retrieve(query: str, top_k: int = TOP_K) -> list[dict]:
    """
    Embed a query and return the top-k most similar chunks from ChromaDB.

    Returns a list of dicts sorted by relevance (lowest distance first):
      {"text": str, "source": str, "course": str, "distance": float}
    """
    count = _collection.count()
    if count == 0:
        print("Index is empty — run embed.py first.")
        return []

    results = _collection.query(
        query_texts=[query],
        n_results=min(top_k, count),
        include=["documents", "metadatas", "distances"],
    )

    output = []
    for text, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        if dist <= DISTANCE_THRESHOLD:
            output.append({
                "text": text,
                "source": meta["source"],
                "course": meta["course"],
                "distance": dist,
            })

    return output
