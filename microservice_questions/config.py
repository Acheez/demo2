import os
import json
from pydantic import BaseSettings

class QuestionGenSettings(BaseSettings):
    openai_model: str
    temperature: float

    class Config:
        extra = "ignore"

def load_settings() -> QuestionGenSettings:
    """Loads config.json from this directory, returning a config object."""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        raw_data = json.load(f)
    # Filter out comment fields
    filtered = {k: v for k, v in raw_data.items()}
    return QuestionGenSettings(**filtered)

settings = load_settings()
