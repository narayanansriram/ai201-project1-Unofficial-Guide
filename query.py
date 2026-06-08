from retriever import retrieve
from generator import generate_response


def ask(query: str) -> dict:
    """
    Full RAG pipeline: retrieve relevant chunks then generate a grounded answer.

    Returns {"answer": str, "sources": list[str]}
    """
    chunks = retrieve(query)
    return generate_response(query, chunks)


if __name__ == "__main__":
    eval_questions = [
        "What do students say about the AVL tree assignment in CS 261?",
        "How difficult is CS 325 and what do students recommend to get through it?",
        "Is CS 344 a good course and how much time should I expect to spend on it?",
        "How hard is CS 225 and what math background do I need?",
        "What class should I take with CS 162?",
        # Out-of-scope — should refuse
        "What is the CS 499 capstone like?",
    ]

    for q in eval_questions:
        print(f"\n{'='*60}")
        print(f"Q: {q}")
        print(f"{'='*60}")
        result = ask(q)
        print(result["answer"])
        print(f"\nSources: {result['sources']}")
