# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

I chose Oregon State University's Computer Science course reviews. Oregon State University has an eCampus BS in Computer Science program. The program has several asynchronous, online students who review the courses in a variety of websites such as reddit (subreddit r/OSUOnlineCS) and its own bespoke website https://osu-cs-course-explorer.com/. The reviews are scattered throughout these sources and are not available on Oregon State's ecampus website.
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location | Local file |
|---|--------|-------------|-----------------|------------|
| 1 | OSU CS Course Explorer | Student reviews for CS 161, 162, 165, 225, 261, 271, 290, 325, 344, 372 — copied manually from SPA | https://osu-cs-course-explorer.com | documents/cs161_reviews.txt, documents/cs162_reviews.txt, documents/cs165_reviews.txt, documents/cs225_reviews.txt, documents/cs261_reviews.txt, documents/cs271_reviews.txt, documents/cs290_reviews.txt, documents/cs325_reviews.txt, documents/cs344_reviews.txt, documents/cs372_reviews.txt |
| 2 | r/OSUOnlineCS | Reddit thread: CS 162 vent thread | https://www.reddit.com/r/OSUOnlineCS/comments/59qykl/162_vent/ | documents/cs162_redditthreads.txt |
| 3 | r/OSUOnlineCS | Reddit thread: CS 225 anonymous rant/PSA | https://www.reddit.com/r/OSUOnlineCS/comments/19eytrd/rip_225_bro_psa_if_you_want_to_rant_anonymously/ | documents/cs225_redditthreads.txt |
| 4 | r/OSUOnlineCS | Reddit thread: CS 261 prep recommendations | https://www.reddit.com/r/OSUOnlineCS/comments/185hy2y/261_prep_recommendations/ | documents/cs261_redditthreads.txt |
| 5 | r/OSUOnlineCS | Reddit thread: CS 290 feeling lost and overwhelmed | https://www.reddit.com/r/OSUOnlineCS/comments/4i65as/cs_290_anyone_else_feeling_lost_and_overwhelmed/ | documents/CS290_redditthreads.txt |
| 6 | r/OSUOnlineCS | Reddit thread: CS 325 just want to pass | https://www.reddit.com/r/OSUOnlineCS/comments/kyu17s/325_just_want_to_pass/ | documents/cs325_redditthreads.txt |
| 7 | r/OSUOnlineCS | Reddit thread: CS 340 dark horse candidate for worst course | https://www.reddit.com/r/OSUOnlineCS/comments/oso0c1/cs340_dark_horse_candidate_for_worst_course/ | documents/cs340_redditthreads.txt |
| 8 | r/OSUOnlineCS | Reddit thread: CS 344 tips and experiences | https://www.reddit.com/r/OSUOnlineCS/comments/kgfgpa/for_those_of_us_about_to_take_cs344/ | documents/cs344_redditthreads.txt |
| 9 | r/OSUOnlineCS | Reddit thread: CS 372 revamp discussion | https://www.reddit.com/r/OSUOnlineCS/comments/185hy2y/did_they_revamp_cs_372/ | documents/cs372_redditthreads.txt |
| 10 | r/OSUOnlineCS | Reddit thread: CS 492 tougher than expected | https://www.reddit.com/r/OSUOnlineCS/comments/t5auuy/anyone_else_have_a_tougher_time_with_492_than/ | documents/cs492_redditthreads.txt |
| 11 | r/OSUOnlineCS | Reddit thread: CS 493 new reviews | https://www.reddit.com/r/OSUOnlineCS/comments/1pvvlsg/any_new_reviews_for_493/ | documents/cs493_redditthreads.txt |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
1000 characters — segments up to 1000 chars are kept whole; anything longer triggers sentence-boundary splitting
**Overlap:**
100 characters which is sufficient to preserve meaning and context of the review without sacrificing retrieval
**Why these choices fit your documents:**
1000-char chunks keep most multi-sentence reviews intact and provide sufficient context per retrieval slot. The 100-char overlap preserves continuity across sentence-split boundaries. The 100-char minimum filters out thread titles and one-line fragments that produce poor embeddings and waste retrieval slots.
**Final chunk count:**
1538 chunks

**Sample chunks:**

**Chunk 1** — `cs344_reviews.txt` (CS 344, 502 chars)
> pointers and to learn how to implement a basic hash table structure for better time complexity. This was not strictly necessary to complete the assignments but would be something I would recommend students learn. The assignments are all very doable if you learn the foundational concepts early on and start the projects early (it will probably be a fairly time intensive course for most students). The grading criteria is very clear and lenient as well. The final is open book and tests basic concepts.

**Chunk 2** — `cs162_reviews.txt` (CS 162, 250 chars)
> [December 2020] If CS 161 was your only experience with programming, prepare for weeks 2 and 3. Refresh your knowledge of classes and list comprehension. It gets easier after that (in my opinion), but don't leave those assignments to the last minute.

**Chunk 3** — `cs225_reviews.txt` (CS 225, 658 chars)
> [September 2017] In my term, there were two textbooks (the required textbook and an optional textbook). If your CS 225 term is like mine, definitely use both textbooks. Sometimes one textbook explained certain concepts better than the other textbook. Practice the homework problems, previous term homework problems, the demo quizzes, and similar problems from the textbooks. CS 225 was difficult for me at first, but I got the hang of it by constantly practicing problems and rereading the required readings. Make sure you review how to do algebra especially if math is not your strength.

**Chunk 4** — `cs261_redditthreads.txt` (CS 261, 352 chars)
> There's definitely a ton of busy work, but I think that's there to help struggling groups more than anything. If you found a solid partner and are always ahead on your project, the peer reviews and the like seem over the top. But for groups that require a lot of troubleshooting or adjustment, I think the peer reviews and busy work are quite critical.

**Chunk 5** — `cs492_redditthreads.txt` (CS 492, 220 chars)
> Same, I had to turn this past one in a little late. There was definitely a difficulty spike, particularly with state management (not being allowed to use Provider sucked). Starting early on these assignments helps a lot.

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
all-MiniLM-L6-v2 via sentence-transformers. It is a good fit for this (albeit student) project as it performs well for synthesis tasks like summarizing student reviews.

**Production tradeoff reflection:**
Context length: Several CS 344 and CS 290 reviews have between 2000-4500 characters which are detailed and are cut into smaller pieces and therefore losing nuance and coherence. A better fit would be text-embedding-3-small which supports up to 8191 tokens and for 1538 chunks would cost less than a cent
Privacy concerns/local vs API hosted: The data here contains student opinions on instructors which when sent to an API means leaving the infrastructure completely [concerns about FERPA-adjacent data leaving infrastructure, i.e.]. all-MiniLM-L6-v2 would keep it on-prem, therefore allaying privacy concerns
Multilingual support and domain-specific accuracy: non issues here since the data is in informal American English which are handled well by general-purpose models
Latency: Negligible since embedding happens once at index time
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
"You are an unofficial guide for the OSU eCampus BS Computer Science program.
Answer the student's question using ONLY the review excerpts provided below.
Do not add information from your own knowledge — if the excerpts don't cover it, say so.
Be concise and specific."

Structural choices:

Distance threshold filter — chunks with cosine distance > 0.5 are dropped before the LLM ever sees them (DISTANCE_THRESHOLD = 0.5 in config.py). This prevents weakly-matched chunks from being passed as context, which reduces the chance the model fills gaps with hallucinated content.

Empty-context refusal — if no chunks pass the distance threshold, generate_response() returns a hardcoded refusal string before any LLM call is made. The model is never invoked on an empty context, so it has no opportunity to hallucinate from general knowledge.

No chat history — the UI does not pass conversation history to the LLM. Every query is answered independently from retrieved context only, preventing the model from building on a prior answer that may have drifted from the documents.

**How source attribution is surfaced in the response:**
Labeled context blocks — each chunk is passed to the LLM with its source labeled: [CS 261 | cs261_reviews.txt]. This makes it explicit to the model what it is drawing from and makes citations tractable.

---

## Retrieval Tests

**Query 1:** "What do students say about the AVL tree assignment in CS 261?"

| Rank | Course | Source | Distance | Snippet |
|------|--------|--------|----------|---------|
| 1 | CS 261 | cs261_reviews.txt | 0.400 | "AVL assignment is much more difficult than other assignments. Expect to spend at least twice as much time on this assignment" |
| 2 | CS 261 | cs261_reviews.txt | 0.414 | "Make sure to get started early on the homeworks, or you'll probably be in trouble..." |
| 3 | CS 261 | cs261_reviews.txt | 0.431 | "I feel like each of the assignments is fairly straightforward, with the exception of AVL trees..." |

*Why relevant?:* All 3 results are from `cs261_reviews.txt` and directly address AVL trees by name. Chunks 1 and 3 explicitly mention the AVL assignment's difficulty; chunk 2 provides supporting context about starting early on CS 261 homeworks. The low cosine distances (0.400–0.431) confirm strong semantic match to the query.

---

**Query 2:** "Is CS 344 a good course and how much time should I expect to spend on it?"

| Rank | Course | Source | Distance | Snippet |
|------|--------|--------|----------|---------|
| 1 | CS 344 | cs344_reviews.txt | 0.308 | "seems to have finally been tuned to the point where almost everyone seemed to think it was fair..." |
| 2 | CS 344 | cs344_reviews.txt | 0.316 | "Go into this knowing it's a 'weed-out' class; only a few students in each section are supposed to pass it..." |
| 3 | CS 261 | cs261_reviews.txt | 0.336 | "This is one of (arguably) few true CS courses in the program..." |

*Why relevant:* Chunks 1 and 2 directly address CS 344's course quality and difficulty level — exactly what the query asks. Chunk 3 drifts to CS 261 but shares vocabulary around "challenging technical course," illustrating how cross-course embedding similarity can pull in adjacent results. The very low distances on chunks 1–2 (0.308, 0.316) reflect a strong semantic match.

---

**Query 3:** "What class should I take with CS 162?"

| Rank | Course | Source | Distance | Snippet |
|------|--------|--------|----------|---------|
| 1 | CS 165 | cs165_reviews.txt | 0.346 | "Condenses CS161 and CS162 into one fast-paced course..." |
| 2 | CS 162 | cs162_reviews.txt | 0.346 | "Really make sure you understand the last couple of modules in CS161..." |
| 3 | CS 290 | cs290_reviews.txt | 0.363 | "If you're thinking about getting an override to take it with CS162, I'd say do it because it was a nice, low-effort..." |

*Why relevant:* Chunk 3 is the strongest hit — it explicitly mentions taking CS 290 *with* CS 162, directly matching the pairing question (distance 0.363). Chunk 2 is relevant because it references what students need going into CS 162, establishing course-sequencing context that informs which courses sit alongside it. Chunk 1 is the weakest: CS 165 is the accelerated replacement for CS 161+162, so the embedding model treats it as semantically adjacent to CS 162 content — it surfaces because it shares the CS 161/162 vocabulary, not because it directly answers the pairing question.

---

## Example System Responses

**Response 1 — "What do students say about the AVL tree assignment in CS 261?"**

> According to the reviews, students say that the AVL tree assignment in CS 261 is "much more difficult than other assignments" and "very time consuming" — an exception to the otherwise "fairly straightforward" assignments. They recommend expecting to spend at least twice as much time on this assignment.
>
> **Sources:**
> - `cs261_reviews.txt`

---

**Response 2 — "What class should I take with CS 162?"**

> According to the reviews, if you have any prior web development experience, taking CS 290 with CS 162 might be a good option, as CS 290 is described as a "low-effort" class. Additionally, taking CS 271 with CS 162 is also mentioned as a possible combination, as CS 162 can help alleviate some of the concerns related to managing the stack and registers in CS 271.
>
> **Sources:**
> - `cs161_reviews.txt`
> - `cs162_reviews.txt`
> - `cs165_reviews.txt`
> - `cs225_redditthreads.txt`
> - `cs290_reviews.txt`

---

**Out-of-scope query — "What is the CS 499 capstone like?"**

> I don't have enough information in my sources to answer that question. Try asking about a specific OSU eCampus CS course (e.g. CS 161, 162, 225, 261, 271, 290, 325, 340, 344, 372, 492, or 493).
>
> **Sources:** none

---

## Query Interface

**Interface:** Gradio web app launched via `python3 app.py`, served at `http://localhost:7860`

**Input:** A plain-language text box — the student types a question about any covered OSU eCampus CS course and submits with the Ask button or Enter key. Example questions are provided as clickable shortcuts below the input.

**Output:** Two fields rendered in the chat panel:
- **Answer** — a grounded, concise response synthesized from retrieved student reviews
- **Sources** — a list of source filenames (e.g. `cs261_reviews.txt`) that the retrieved chunks came from, appended below the answer

**Sample interaction transcript:**

---

*User:* What do students say about the AVL tree assignment in CS 261?

*System:* According to the reviews, students say that the AVL tree assignment in CS 261 is "much more difficult than other assignments" and "very time consuming" — an exception to the otherwise "fairly straightforward" assignments. They recommend expecting to spend at least twice as much time on this assignment.

**Sources:**
- `cs261_reviews.txt`

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What do students say about the AVL tree assignment in CS 261? | Hardest assignment, pseudocode intentionally incorrect, BST affects AVL compatibility, most time-consuming | Described as "much more difficult" and "very time consuming," advises expecting twice the time — misses pseudocode issues and BST compatibility detail | Relevant | Partially accurate |
| 2 | How difficult is CS 325 and what do students recommend to get through it? | Heavy math/proofs, recommends Abdul Bari / MIT OCW, grind homework and extra credit | Refused to answer — retrieved CS 161, 261, 344, 162 chunks instead of CS 325; no CS 325 content passed the distance threshold | Off-target | Inaccurate |
| 3 | Is CS 344 a good course and how much time should I expect to spend on it? | 20+ hrs/week, C programming, test on os1, one of the hardest but well-designed | Described as challenging and weed-out, mentions daily assignments and TA office hours — misses C programming and os1 testing details | Partially relevant | Partially accurate |
| 4 | How hard is CS 225 and what math background do I need? | Challenging especially with limited math background, algebra skills important, MTH 231 relevant, heavy assignment load | Described as difficult with limited math background, recommends reviewing algebra — misses MTH 231 specifically | Relevant | Partially accurate |
| 5 | What class should I take with CS 162? | 162+271 is a heavy combo to avoid, 162+225 also rough, 162 pairs better with a low-effort course | Recommends CS 290 as a low-effort pairing and mentions CS 271 — directionally correct but inverts the CS 271 warning | Partially relevant | Partially accurate |


**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
How difficult is CS 325 and what do students recommend to get through it? 

**What the system returned:**
Refused to answer — retrieved CS 161, 261, 344, 162 chunks instead of CS 325; no CS 325 content passed the distance threshold

**Root cause (tied to a specific pipeline stage):**
The issue appears to be in the embedding stage. Since the query has two intents - i.e., "how difficult" and "what do students recommend to get through it" leads the embedding model to average these into a single vector that sits somwhere between "difficulty" and "advice" which matches to CS 344 for "most time-intensive course, averaging over 20 hours per week" for difficulty, CS 492 for mentions of difficulty comparisons with 344 and CS 225 which has "plan to spend 25 hours a week minimum" which is a match for both difficulty and advice. This seems to be because CS 325 is just another token rather than a classifier.

Additionally, the reviews for CS 325 are very short at about 100-200 characters. This would mean most of the chunks are low information and overridden by the likes of 344 and 225.

**What you would change to fix it:**
There are 2 ways to approach this:
- Since the reason for the failure is that "CS 325" is just another token, adding a _course_ metadata filter in the retriever.py file so the relevant chunks are filed under it
- Since the CS 325 reviews are so short, reduce MIN_CHUNK to 50 characters so they are not dropped, i.e, added to increase the CS 325 review pool
---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
Writing the chunking strategy before implementing the code forced me to walk through the process manually -- this ultimately led me to choosing Fixed Size. If I had dove in to coding, I would have probably have gone with the 500-character split in the Week 1 Lab RAG application. Since the spec made me lay out the reasoning for the chunking strategy, I realized that the average review had a definitive fixed size.

**One way your implementation diverged from the spec, and why:**
I specified (in the spec) that the chunk split should be 800 chars at sentence boundaries with a 100 character overlap. During implementation, I increased it to 1000 chars after further testing with the documents and diving deep into all-MiniLM-L6-v2. all-MiniLM-L6-v2 has a truncation limit at about 1000 chars since the 800 char-split was breaking apart ~170 chunks that did not need splitting - therefore reducing retrieval benefits from longer reviews. The increase to 1000 chars, therefore, allowed for longer multi-sentence reviews.
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* The Architecture diagram and Milestone 3 section of planning.md (two file types: `*_reviews.txt` and `*_redditthreads.txt`, review-boundary split on `---`, blank-line split for Reddit, sentence-boundary fallback for chunks >800 chars, 100-char overlap), plus the reference `ingest.py` from the rulesbot lab
- *What it produced:* `ingest.py` with `load_and_chunk()`, `chunk_segment()`, and a sliding-window fallback — matching the spec closely
- *What I changed or overrode:* Raised `MAX_CHUNK` from 800 to 1000 and `CHUNK_SIZE` from 500 to 1000 after observing that most reviews were being sentence-split unnecessarily; raised `MIN_CHUNK` from 50 to 100 after identifying that thread titles like "CS 290 - Anyone else feeling lost and overwhelmed?" (exactly 50 chars) were passing the filter and producing weak embeddings

**Instance 2**

- *What I gave the AI:* The Architecture diagram, Milestone 4 and 5 sections of planning.md, the reference `retriever.py` and `generator.py` from the rulesbot lab, and the chunk output from `ingest.py`
- *What it produced:* `retriever.py` with `embed_and_store()` and `retrieve()`, `generator.py` with `generate_response()`, `query.py` with `ask()`, and `app.py` with a Gradio UI
- *What I changed or overrode:* Changed `TOP_K` from 5 to 7 during retrieval testing after noticing sparse results for some courses; replaced question 4 in the evaluation plan from a CS 340 complaint question to a CS 225 math background question after CS 340 retrieval failed completely due to that course only having a Reddit thread file and no structured reviews file; removed the system prompt instruction to self-cite source filenames after discovering it produced a duplicate sources list alongside the one already appended by `app.py`

---

## Demo Video

[![Watch the demo](https://cdn.loom.com/sessions/thumbnails/beff1e496a764fbda2a13307a3f5ee8a-with-play.gif)](https://www.loom.com/share/beff1e496a764fbda2a13307a3f5ee8a)
