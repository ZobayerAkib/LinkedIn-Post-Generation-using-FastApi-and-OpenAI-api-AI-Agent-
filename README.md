# 🚀 LinkedIn Post Generator API (FastAPI + OpenAI)
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&pause=1000&width=435&lines=%F0%9F%9A%80+LinkedIn+Post+Generator+API+(FastAPI+%2B+OpenAI))](https://git.io/typing-svg)

This repository provides a **FastAPI-based API** that automatically generates professional **LinkedIn-style posts** using **OpenAI-compatible models**.  
The API supports two key domains:

- 🩺 **AI in Healthcare**  
- 🧑‍💻 **Remote Work Productivity**

Each endpoint produces a **2–4 paragraph** LinkedIn post written in a professional, engaging tone, complete with hashtags and emojis, in any specified language.

---

# LinkedIn Post Generator

## ⚙️ Setup Instructions
### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/LinkedIn-Post-Generator.git
cd LinkedIn-Post-Generator
```
### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt

```
requirements.txt 
```ini
fastapi==0.115.6
uvicorn==0.32.1
openai==1.66.3
python-dotenv==1.0.1
pydantic==2.10.6
```
### 4️⃣ Configure Environment Variables
```bash
BASE_URL="https://models.github.ai/inference"
API_KEY="your_api_key_here"
MODEL_NAME="openai/gpt-4.1-nano"
```
#▶️ Run the API
```bash
uvicorn main:app --reload
```
Then open your browser and go to:
 ```arduino
  http://127.0.0.1:8000/docs
```
You’ll see the Swagger UI, where you can interact with the API endpoints directly.

## 🧠 How It Works

- Loads environment variables from `.env`.
- Initializes the OpenAI client using the provided base URL and API key.
- Builds a prompt dynamically based on the request topic and language.
- Returns a professional LinkedIn-style post as a JSON response.

## 🛡️ Security Notes

- Never expose your `.env` or API key in public repositories.
- Use environment variables in deployment environments.
- Consider adding authentication if deploying publicly.

## 👨‍💻 Author

**Md. Zobayer Ibna Kabir**  
📧 Email: [ibnakabir081@gmail.com]  
🔗 GitHub: [https://github.com/ZobayerAkib](https://github.com/ZobayerAkib)  
💼 LinkedIn: [https://linkedin.com/in/mdzobayeribnakabir/](https://www.linkedin.com/in/mdzobayeribnakabir/)
