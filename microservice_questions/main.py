from fastapi import FastAPI
from pydantic import BaseModel
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from config import settings
from prompt_templates import GENERAL_QUESTIONS_PROMPT

app = FastAPI(title="Question Generation Service")

class QuestionRequest(BaseModel):
    chunks: list[str]

@app.post("/generate-questions")
def generate_questions(request: QuestionRequest):
    """
    Accepts PDF chunks, returns a list of general questions in JSON array format.
    """
    context = "\n".join(request.chunks)

    # Configure the LLM using settings from config.json
    llm = ChatOpenAI(
        model_name=settings.openai_model,
        temperature=settings.temperature
    )

    prompt = PromptTemplate(
        input_variables=["context"],
        template=GENERAL_QUESTIONS_PROMPT
    )

    chain = LLMChain(prompt=prompt, llm=llm)
    # We pass 'context=context' since that's the only variable in the prompt template
    result = chain.run(context=context)

    # result should be a JSON array string if everything goes right
    return {"questions": result}
