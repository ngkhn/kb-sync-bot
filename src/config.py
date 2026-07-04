from dotenv import load_dotenv
import os

load_dotenv()


# Load OPENAI_API_KEY from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing")

