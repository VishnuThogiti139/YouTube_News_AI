# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env in the current directory

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")
GOOGLE_OAUTH_CLIENT_JSON_PATH = os.getenv("GOOGLE_OAUTH_CLIENT_JSON_PATH", "")
YOUTUBE_REFRESH_TOKEN = os.getenv("YOUTUBE_REFRESH_TOKEN", "")
