# Rag-project

# 🦾 Rag-project

Welcome to **Rag-project** – an open-source Retrieval-Augmented Generation (RAG) system that leverages powerful language models and vector search to answer questions based on uploaded resumes! This project demonstrates how to build a simple QA application using Gradio, FAISS, and Sentence Transformers, making it easy to interact with your own documents.

---

## 🚀 Introduction

**Rag-project** enables users to upload a resume (PDF), which is then processed and indexed for semantic search. By integrating a RAG pipeline, the system retrieves relevant context from the uploaded resume and generates accurate answers to user queries. This approach combines the strengths of information retrieval and language models, resulting in more reliable and context-aware answers.

---

## ✨ Features

- 📄 **Resume Upload:** Easily upload PDF resumes for processing.
- 🧩 **Automatic Chunking:** Resumes are split into manageable text chunks for better context retrieval.
- 🔍 **Semantic Search:** Utilizes FAISS and Sentence Transformers for efficient, relevant search.
- 💬 **QA Chatbot:** Ask questions and receive answers based on the uploaded resume.
- 🌐 **Gradio Interface:** User-friendly web interface for seamless interaction.

---

## ⚙️ Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/rag-project.git
    cd rag-project
    ```

2. **Create a Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**
    - Create a `.env` file in the root directory.
    - Add your OpenRouter API key:
      ```
      OPENROUTER_API_KEY=your_openrouter_api_key_here
      ```

---

## 🛠 Usage

1. **Run the Application**
    ```bash
    python app.py
    ```

2. **Open the Interface**
    - Follow the Gradio link in your terminal (usually `http://127.0.0.1:7860`).

3. **Interact**
    - **Upload Resume:** Click to upload your PDF resume.
    - **Ask Questions:** Enter any question about the uploaded resume and receive contextual answers!

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Please follow these steps:

1. Fork this repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

**Made with ❤️ for the AI community!**

## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/mathi7585/Rag-project