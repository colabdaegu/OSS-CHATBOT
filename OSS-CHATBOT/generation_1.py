import os

from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

# 2. 환경변수 불러오기
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
api_version = "2025-01-01-preview"  # Azure에서 제공한 버전

client = OpenAI(
    api_key=api_key,
    base_url=f"{endpoint}openai/deployments/{deployment}",
    default_query={"api-version": api_version}
)

app = FastAPI(debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    temperature: float = 1

SYSTEM_MSG = "You are a helpful professor, Your name is Jini, 25 years old"

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": SYSTEM_MSG},
            {"role": "user", "content": req.message}
        ],
        temperature=req.temperature,
    )
    return {"message": response.choices[0].message.content}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)