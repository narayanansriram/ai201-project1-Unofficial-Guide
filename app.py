import gradio as gr
from embed import build_index
from query import ask
from retriever import get_collection

COURSES = [
    "CS 161", "CS 162", "CS 165", "CS 225", "CS 261",
    "CS 271", "CS 290", "CS 325", "CS 340", "CS 344",
    "CS 372", "CS 492", "CS 493",
]


def chat(message, history):
    if not message.strip():
        return "", history
    result = ask(message)
    answer = result["answer"]
    if result["sources"]:
        sources_md = "\n".join(f"- `{s}`" for s in result["sources"])
        answer += f"\n\n**Sources:**\n{sources_md}"
    history = history + [{"role": "user", "content": message}, {"role": "assistant", "content": answer}]
    return "", history


with gr.Blocks(title="OSU CS Unofficial Guide") as demo:

    gr.HTML("""
        <div style="text-align:center; padding:1.25rem 0 0.5rem;">
            <h1 style="font-size:2rem; font-weight:700; color:#D73F09; margin:0;">
                📚 OSU CS Unofficial Guide
            </h1>
            <p style="color:#6b7280; font-size:1rem; margin:0.4rem 0 0;">
                Real student reviews from Reddit and the CS Course Explorer —
                grounded answers, no hallucination.
            </p>
        </div>
    """)

    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(height=480)
            with gr.Row():
                msg = gr.Textbox(
                    placeholder='e.g. "How hard is the AVL tree assignment in CS 261?"',
                    scale=8,
                    container=False,
                )
                send = gr.Button("Ask", scale=1, variant="primary")

            gr.Examples(
                examples=[
                    "What do students say about the AVL tree assignment in CS 261?",
                    "How difficult is CS 325 and what do students recommend?",
                    "Is CS 344 worth taking and how many hours per week?",
                    "What are the biggest complaints about CS 340?",
                    "What class should I take with CS 162?",
                ],
                inputs=msg,
            )

        with gr.Column(scale=1, min_width=180):
            course_list = "\n".join(f"- {c}" for c in COURSES)
            gr.Markdown(f"""
**📖 Covered Courses**

{course_list}

---
*Answers are grounded in student reviews only. If a course isn't covered, the guide will say so.*
""")

    send.click(chat, inputs=[msg, chatbot], outputs=[msg, chatbot])
    msg.submit(chat, inputs=[msg, chatbot], outputs=[msg, chatbot])


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  OSU CS Unofficial Guide — starting up")
    print("=" * 50 + "\n")
    build_index()
    demo.launch(theme=gr.themes.Soft(primary_hue="orange", neutral_hue="stone"))
