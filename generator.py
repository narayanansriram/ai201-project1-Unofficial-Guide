from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

_client = Groq(api_key=GROQ_API_KEY)


def generate_response(query: str, retrieved_chunks: list[dict]) -> dict:
    """
    Generate a grounded answer from retrieved review chunks.

    Returns {"answer": str, "sources": list[str]}
    Refuses to answer if no chunks were retrieved.
    """
    if not retrieved_chunks:
        return {
            "answer": (
                "I don't have enough information in my sources to answer that question. "
                "Try asking about a specific OSU eCampus CS course (e.g. CS 161, 162, 225, "
                "261, 271, 290, 325, 340, 344, 372, 492, or 493)."
            ),
            "sources": [],
        }

    context = "\n\n".join(
        f"[{c['course']} | {c['source']}]\n{c['text']}" for c in retrieved_chunks
    )

    system_msg = (
        "You are an unofficial guide for the OSU eCampus BS Computer Science program. "
        "Answer the student's question using ONLY the review excerpts provided below. "
        "Do not add information from your own knowledge — if the excerpts don't cover it, say so. "
        "Be concise and specific."
    )

    response = _client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": f"Student reviews:\n{context}\n\nQuestion: {query}"},
        ],
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": sorted({c["source"] for c in retrieved_chunks}),
    }
