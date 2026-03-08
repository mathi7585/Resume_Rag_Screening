import gradio as gr
from resume_loader import load_and_chunk_resume
from rag_pipeline import (
    build_faiss_index,
    retrieve_context,
    generate_answer
)

def upload_resume(pdf):
    """
    Handle resume upload and FAISS indexing
    """
    if pdf is None:
        return "❌ Please upload a resume PDF."

    chunks = load_and_chunk_resume(pdf)
    build_faiss_index(chunks)

    return "✅ Resume uploaded and indexed successfully."


def answer_question(question):
    """
    Answer user question strictly from resume
    """
    if not question or question.strip() == "":
        return "Please enter a valid question."

    context_chunks = retrieve_context(question)
    answer = generate_answer(context_chunks, question)

    return answer


with gr.Blocks(title="Resume-Based Q&A Assistant") as demo:
    gr.Markdown("## 📄 Resume-Based Question Answering System")
    gr.Markdown(
        "Upload a resume and ask questions. "
        "The system answers strictly from the uploaded resume only."
    )

    with gr.Row():
        pdf_upload = gr.File(
            label="Upload Resume (PDF)",
            file_types=[".pdf"]
        )
        upload_btn = gr.Button("Process Resume")

    upload_status = gr.Textbox(
        label="Status",
        interactive=False
    )

    upload_btn.click(
        upload_resume,
        inputs=pdf_upload,
        outputs=upload_status
    )

    question = gr.Textbox(
        label="Ask a Question",
        placeholder="e.g. What skills are mentioned?"
    )

    answer = gr.Textbox(
        label="Answer",
        lines=6,
        max_lines=10,
        interactive=False
    )

    question.submit(
        answer_question,
        inputs=question,
        outputs=answer
    )

demo.launch()
