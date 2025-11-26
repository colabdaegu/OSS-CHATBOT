import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1) .env 불러오기
load_dotenv()

# 2) LangChain용 LLM 객체 만들기 (Azure OpenAI v1 방식)
model = ChatOpenAI(
    model=os.getenv("DEPLOYMENT_NAME"),               
    api_key=os.getenv("OPENAI_API_KEY"),            
    base_url=os.getenv("ENDPOINT_URL").rstrip("/") + "/openai/v1/",
    temperature=0.0,
)

# 3) 메시지 보내보기
# from langchain_core.messages import HumanMessage
# msg = model.invoke([HumanMessage(content="안녕? 나는 김현수야.")])
# # print(msg.content)
# print(msg)

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

messages = [
    SystemMessage("너는 사용자를 도와주는 상담사야.")
]

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
        break

    messages.append(
        HumanMessage(user_input)
    )

    ai_response = model.invoke(messages)

    messages.append(
        ai_response
    )

    print("AI: " + ai_response.content)