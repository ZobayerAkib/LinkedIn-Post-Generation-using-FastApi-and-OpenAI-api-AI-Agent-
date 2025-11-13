from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# Secure API Key (Hidden)
BASE_URL = os.getenv("BASE_URL") 
API_KEY = os.getenv("API_KEY") 
MODEL_NAME = os.getenv("MODEL_NAME") 

if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError(
        "Please set BASE_URL, API_KEY, and MODEL_NAME."
    )
    

# Initialize GitHub Models client
client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

# FastAPI App Setup

app = FastAPI(
    title="LinkedIn Post Generator API",
    description="Generate 2–4 paragraph professional LinkedIn posts",
    version="1.0.0",
)

#-------------------------AI in Healthcare------------------------
# Request Schema

class AiHealthCare(BaseModel):
    topic: str = Field(..., description="Topic of the post (e.g., 'AI in Healthcare')")
    language: str = Field(..., description="Language of the post (e.g., English, Bengali, Spanish)")


# Endpoint: /generate_post_health

@app.post("/generate_post_health")
async def generate_post(request: AiHealthCare):
    """
    Generate a LinkedIn-style post (2–4 paragraphs) in the requested language and topic.
    """

    try:
        prompt = f"""
        You are a professional LinkedIn content creator expertise on "AI in Healthcare".

        Write a post in {request.language} about the topic: "{request.topic}".

        The post should:
        - Be structured and easy to read.
        - Be engaging and informative.
        - Give a title that is catchy and engaging.
        - Be written in a professional and conversational LinkedIn tone.
        - Contain exactly 2 to 4 paragraphs.
        - Include a short concluding or motivational line at the end.
        - use some meaning-full hashtag {request.language} and emojis.


        Write a LinkedIn-style post using mentioned structure .
        """

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes LinkedIn posts."},
                {"role": "user", "content": prompt},
            ],
        )

        linkedin_post = response.choices[0].message.content.strip()
        return {
            "topic": request.topic,
            "language": request.language,
            "linkedin_post": linkedin_post
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#--------------------Remote Work Productivity------------------------

class RemoteWorkProductivity(BaseModel):
    topic: str = Field(..., description="Topic of the post (e.g., 'Remote Work Productivity')")
    language: str = Field(..., description="Language of the post (e.g., English, Bengali, Spanish)")


# Endpoint: /generate_post_remote_work

@app.post("/generate_post_remote_work")
async def generate_post(request: RemoteWorkProductivity):
    """
    Generate a LinkedIn-style post (2–4 paragraphs) in the requested language and topic.
    """

    try:
        prompt = f"""
        You are a professional LinkedIn content creator specially expertise on "Remote Work Productivity".

        Write a post in {request.language} about the topic: "{request.topic}".
        

        The post should:
        - give a title
        - Be professional, engaging, and insightful
        - Provide actionable tips or strategies for staying productive while working remotely
        - Contain exactly 2–4 paragraphs
        - Output only the post content, nothing else
        - use some meaning-full hashtag {request.language} and emojis.


        Write a LinkedIn-style post using mentioned structure .
        """

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes LinkedIn posts."},
                {"role": "user", "content": prompt},
            ],
        )

        linkedin_post = response.choices[0].message.content.strip()
        return {
            "topic": request.topic,
            "language": request.language,
            "linkedin_post": linkedin_post
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
