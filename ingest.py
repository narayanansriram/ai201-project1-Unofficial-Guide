import os
import re

DOCS_PATH = os.path.join(os.path.dirname(__file__), "documents")

CHUNK_SIZE = 1000
OVERLAP = 100
MAX_CHUNK = 1000
MIN_CHUNK = 100


def extract_course(filename: str) -> str:
    """Extract course code from filename, e.g. 'cs161_reviews.txt' -> 'CS 161'."""
    match = re.match(r"(cs\d+)", filename, re.IGNORECASE)
    if match:
        code = match.group(1).upper()
        return code[:2] + " " + code[2:]
    return filename


def clean_reviews(text: str) -> list[str]:
    """Split a *_reviews.txt file on '---' separators and return non-empty reviews."""
    parts = text.split("---")
    reviews = []
    for part in parts:
        cleaned = part.strip()
        if len(cleaned) >= MIN_CHUNK:
            reviews.append(cleaned)
    return reviews


def clean_reddit(text: str) -> list[str]:
    """Split a *_redditthreads.txt file on blank lines and return non-empty paragraphs."""
    parts = re.split(r"\n\s*\n", text)
    paragraphs = []
    for part in parts:
        cleaned = part.strip()
        # Drop deleted/removed placeholders
        if cleaned.lower() in ("[deleted]", "[removed]", ""):
            continue
        if len(cleaned) >= MIN_CHUNK:
            paragraphs.append(cleaned)
    return paragraphs


def split_sentences(text: str) -> list[str]:
    """Naive sentence splitter on '. ', '! ', '? '."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in sentences if s.strip()]


def sliding_window_chunks(text: str, source: str, course: str) -> list[dict]:
    """
    Break a long text into overlapping character-window chunks.
    Used as a fallback when a segment exceeds MAX_CHUNK.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        # Snap to nearest word boundary so we never cut mid-word
        if end < len(text) and not text[end].isspace():
            boundary = text.rfind(" ", start, end)
            if boundary > start:
                end = boundary
        chunk = text[start:end].strip()
        if len(chunk) >= MIN_CHUNK:
            chunks.append({"text": chunk, "source": source, "course": course})
        start += CHUNK_SIZE - OVERLAP
    return chunks


def chunk_segment(segment: str, source: str, course: str) -> list[dict]:
    """
    Turn one logical segment (a review or reddit paragraph) into chunks.

    If the segment fits within MAX_CHUNK it becomes one chunk.
    If it exceeds MAX_CHUNK we try a sentence-boundary split first, then
    fall back to a sliding-window split for any sentence that is still too long.
    """
    if len(segment) <= MAX_CHUNK:
        return [{"text": segment, "source": source, "course": course}]

    # Sentence-boundary split with overlap
    sentences = split_sentences(segment)
    chunks = []
    current = ""
    for sentence in sentences:
        candidate = (current + " " + sentence).strip() if current else sentence
        if len(candidate) <= MAX_CHUNK:
            current = candidate
        else:
            if current and len(current) >= MIN_CHUNK:
                chunks.append({"text": current, "source": source, "course": course})
            # carry overlap tail into next chunk, snapped to word boundary
            raw_tail = current[-OVERLAP:] if len(current) > OVERLAP else current
            space = raw_tail.find(" ")
            overlap_text = raw_tail[space + 1:] if space != -1 else raw_tail
            current = (overlap_text + " " + sentence).strip() if overlap_text else sentence

            # single sentence still too long — sliding window
            if len(current) > MAX_CHUNK:
                chunks.extend(sliding_window_chunks(current, source, course))
                current = ""

    if current and len(current) >= MIN_CHUNK:
        chunks.append({"text": current, "source": source, "course": course})

    return chunks if chunks else sliding_window_chunks(segment, source, course)


def load_and_chunk() -> list[dict]:
    """
    Load every .txt file from DOCS_PATH, split it into segments using the
    appropriate cleaner, then chunk each segment.

    Returns a list of dicts: {"text": str, "source": str, "course": str}
    """
    all_chunks: list[dict] = []

    for filename in sorted(os.listdir(DOCS_PATH)):
        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(DOCS_PATH, filename)
        course = extract_course(filename)

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        if "_reviews" in filename:
            segments = clean_reviews(text)
        elif "_redditthreads" in filename:
            segments = clean_reddit(text)
        else:
            segments = [text.strip()]

        for segment in segments:
            all_chunks.extend(chunk_segment(segment, filename, course))

    return all_chunks


if __name__ == "__main__":
    import random

    chunks = load_and_chunk()
    print(f"\nTotal chunks: {len(chunks)}\n")

    # Print first 5 chunks
    print("=== First 5 chunks ===")
    for i, chunk in enumerate(chunks[:5]):
        print(f"[{i}] source={chunk['source']}  course={chunk['course']}  len={len(chunk['text'])}")
        print(f"     {chunk['text'][:120]!r}")
        print()

    # Print 10 random chunks across different files
    print("=== 10 random chunks ===")
    sample = random.sample(chunks, min(10, len(chunks)))
    for chunk in sample:
        print(f"source={chunk['source']}  course={chunk['course']}  len={len(chunk['text'])}")
        print(f"  {chunk['text'][:120]!r}")
        print()

    # Length distribution check
    lengths = [len(c["text"]) for c in chunks]
    too_short = sum(1 for l in lengths if l < MIN_CHUNK)
    too_long = sum(1 for l in lengths if l > MAX_CHUNK)
    print(f"Min len: {min(lengths)}  Max len: {max(lengths)}  "
          f"Too short (<{MIN_CHUNK}): {too_short}  Too long (>{MAX_CHUNK}): {too_long}")
