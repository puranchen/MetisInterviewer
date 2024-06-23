import os
import openai
from dotenv import load_dotenv, find_dotenv

def load_api_key(llm='openai'):
    """ Load OpenAI API key from .env file """
    if not load_dotenv(find_dotenv()):
        raise EnvironmentError("No .env file found")

    api_key = os.getenv(f"{llm.upper()}_API_KEY")
    
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set in the environment")
    openai.api_key = api_key