
import os
from dotenv import load_dotenv

load_dotenv()
STRIPE_SECRET = os.getenv("STRIPE_SECRET")
PRINTIFY_TOKEN = os.getenv("PRINTIFY_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")
