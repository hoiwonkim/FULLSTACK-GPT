from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Turtle Code Mentor",
    description="프로그래밍 학습을 지원하는 GPT입니다. 초보부터 고급 개발자까지 다양한 사용자를 대상으로 합니다. 실수 반복을 피하고 오류를 최소화하여 안정적인 학습을 제공합니다.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 또는 특정 도메인을 명시할 수 있습니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodingAssistance(BaseModel):
    example: str = Field(
        description="Generated coding example to assist in learning.",
    )
    explanation: str = Field(
        description="Explanation of the provided code to aid understanding.",
    )

@app.get(
    "/",
    summary="Root",
    description="Root endpoint",
    response_description="A simple welcome message.",
)
def read_root():
    return {"message": "Welcome to Turtle Code Mentor API"}

@app.get(
    "/coding-assistance",
    summary="Generate coding example and explanation",
    description="This endpoint generates a coding example and provides an explanation to assist users in learning programming.",
    response_description="An object containing a coding example and its explanation.",
    response_model=CodingAssistance,
)
def get_coding_assistance():
    return {
        "example": "for i in range(5):\n    print(i)",
        "explanation": "This code prints numbers from 0 to 4 using a for loop.",
    }

