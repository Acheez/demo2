import os
import json
from pydantic import BaseSettings


class PDFServiceSettings(BaseSettings):
    chunk_size: int
    chunk_overlap: int

    class Config:
        extra = "ignore"


def load_settings() -> PDFServiceSettings:
    """
    Loads config.json from this directory,
    parses it into PDFServiceSettings.
    """
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        data = json.load(f)
    data = {k: v for k, v in data.items()}
    return PDFServiceSettings(**data)


settings = load_settings()
