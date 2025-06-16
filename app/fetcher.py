# app/news_fetcher/fetcher.py
import requests
from config import NEWSAPI_KEY

class NewsFetcher:
    def __init__(self, api_key: str = NEWSAPI_KEY):
        if not api_key:
            raise ValueError("NEWSAPI_KEY is required in .env")
        self.api_key = api_key
        self.endpoint = "https://newsapi.org/v2/top-headlines"

    def fetch_top_headline(
        self,
        country: str = "us",
        category: str = "general",
        limit: int = 5
    ) -> list[dict]:
        """
        Returns a list of articles: [{"title": ..., "content": ...}, ...]
        """
        params = {
            "apiKey": self.api_key,
            "country": country,
            "category": category,
            "pageSize": limit
        }
        resp = requests.get(self.endpoint, params=params, timeout=10)
        if resp.status_code != 200:
            print(f"[NewsFetcher] Error {resp.status_code}: {resp.text}")
            return []

        data = resp.json().get("articles", [])
        result = []
        for a in data:
            title = a.get("title", "")
            # prefer description, fallback to content
            content = a.get("description") or a.get("content") or ""
            result.append({"title": title, "content": content})
        return result
