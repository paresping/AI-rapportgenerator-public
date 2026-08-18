import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = "gpt-4o"

if not openai.api_key:
    raise ValueError(
        "OPENAI_API_KEY is not set. Define it in your local .env file or export it manually."
    )
