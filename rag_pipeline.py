import os
import faiss
import requests
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

# Load embedding model
EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Global FAISS objects
index = None
documents = []


def build_faiss_index(chunks):
    """
    Build FAISS index from resume chunks
    """
    global index, documents
    documents = chunks

    embeddings = EMBED_MODEL.encode(chunks)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)


def retrieve_context(query, k=3):
    """
    Retrieve top-k relevant resume chunks
    """
    if index is None:
        return []

    query_emb = EMBED_MODEL.encode([query])
    distances, indices = index.search(query_emb, k)

    results = []
    for idx in indices[0]:
        if idx != -1:
            results.append(documents[idx])

    return results


def generate_answer(context_chunks, question):
    """
    Generate answer strictly from resume context
    """
    if not context_chunks:
        return "No information found in the uploaded PDF."

    context = "\n".join(context_chunks)

    prompt = f"""
You are an AI Resume Assistant.

RULES:
- Answer ONLY using the context below.
- Do NOT use any external knowledge.
- If the answer is not clearly present, reply exactly:
"No information found in the uploaded PDF."

Context:
{context}

Question:
{question}
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Resume RAG App"
    }

    payload = {
        "model": "mistralai/devstral-2512:free",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=60
    )

    if response.status_code != 200:
        return "Error generating answer."

    return response.json()["choices"][0]["message"]["content"].strip()
