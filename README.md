```markdown
# 🦾 Resume_Rag_Screening

Welcome to **Resume_Rag_Screening** – an open-source Retrieval-Augmented Generation (RAG) system that leverages powerful language models and vector search to answer questions based on uploaded resumes! This project demonstrates how to build a simple QA application using Gradio.

---

## 🚀 Introduction

Resume_Rag_Screening is designed to streamline resume screening and question-answering processes by combining the power of language models and efficient vector search. Upload resumes in PDF format, ask custom questions related to the candidate, and receive context-aware answers generated from the resume content.

---

## ✨ Features

- **Resume Upload:** Easily upload PDF resumes for processing.
- **Chunking & Embedding:** Automatic chunking of resume content and embedding using SentenceTransformers.
- **Vector Search:** Fast context retrieval powered by FAISS vector indexing.
- **QA Pipeline:** Answers questions based on resume content using advanced RAG techniques.
- **Gradio Interface:** Simple and interactive web app for end-to-end screening.

---

## ⚡ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mathi7585/Resume_Rag_Screening.git
   cd Resume_Rag_Screening
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root.
   - Add your OpenRouter API key:
     ```
     OPENROUTER_API_KEY=your_api_key_here
     ```

---

## 🛠️ Usage

1. **Start the Gradio App:**
   ```bash
   python app.py
   ```
2. **Open the Gradio interface in your browser.**
3. **Upload a resume (PDF format).**
4. **Ask questions related to the candidate's experience, skills, etc.**
5. **Receive context-driven answers instantly!**

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes.
4. Push to the branch and open a Pull Request.

Please review the [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📁 Project Structure

```
Resume_Rag_Screening/
├── app.py
├── rag_pipeline.py
├── resume_loader.py
├── README.md
├── requirements.txt
└── .env
```

---

## 🙋‍♂️ Support

For questions or support, please open an issue or contact the maintainer.

---

**Happy Screening!** 🦾
```


## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/mathi7585/Resume_Rag_Screening
