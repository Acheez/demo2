import os
import json
from pydantic import BaseSettings

class OrchestratorSettings(BaseSettings):
    pdf_service_url: str
    question_service_url: str

    class Config:
        extra = "ignore"

def load_settings() -> OrchestratorSettings:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        data = json.load(f)
    data = {k: v for k, v in data.items()}
    return OrchestratorSettings(**data)

settings = load_settings()
