import os
from dotenv import load_dotenv

load_dotenv()

class Env:
    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = int(os.getenv("PORT", 8000))

env = Env()
