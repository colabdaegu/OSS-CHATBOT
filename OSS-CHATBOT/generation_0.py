import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. .env 파일 로드
load_dotenv()

# 2. 환경변수 불러오기
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
api_version = "2025-01-01-preview" # Azure에서 제공한 버전

# 3. 클라이언트 초기화 (Azure OpenAI는 base_url을 지정해야 함)
client = OpenAI(
    api_key=api_key,
    base_url=f"{endpoint}openai/deployments/{deployment}",
    default_query={"api-version": api_version}
)

# 4. ChatGPT 요청
response = client.chat.completions.create(
    model=deployment, # Azure에서는 모델 이름 대신 '배포 이름' 사용
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What can you do?"}
    ], 
    temperature=0.9,
    # n=1,
    # stop=[","],
    max_tokens=10,
)

# 5. 결과 출력
#for res in response.choices:
#    print(res.message)

print(response.choices[0].message.content)

# 토큰 수 확인 코드
# import tiktoken
# sample_text = "안녕하세요!"
# encoding = tiktoken.encoding_for_model("gpt-4.1")
# tokens = encoding.encode(sample_text)
# print("문장 예시:", sample_text)
# print(f"토큰 개수: {len(tokens)}")
# print(f"토큰화: {tokens}")