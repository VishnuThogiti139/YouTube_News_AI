# app/visual_generator/visual_creator.py
import os
from typing import List
from pexels_api import API
from config import PEXELS_API_KEY

class VisualCreator:
    def __init__(self, api_key: str = PEXELS_API_KEY):
        if not api_key:
            raise ValueError("PEXELS_API_KEY is required in .env")
        self.api = API(api_key)

    def generate_visuals(
        self,
        articles: list[dict],
        per_article: int = 1
    ) -> List[str]:
        """
        For each article, fetch `per_article` images from Pexels using the article title as a query.
        Returns a list of local filepaths where images are saved.
        """
        os.makedirs("output/images", exist_ok=True)
        saved_paths = []

        for idx, article in enumerate(articles, start=1):
            query = article.get("title", "").split(" - ")[0]  # simplify query
            self.api.search(query, page=1, results_per_page=per_article)
            photos = self.api.get_entries()
            for i, photo in enumerate(photos):
                url = photo.original  # highest-quality image
                # Download and save
                filename = f"output/images/article_{idx}_img_{i+1}.jpg"
                with open(filename, "wb") as img_f:
                    img_f.write(requests.get(url).content)
                saved_paths.append(filename)

            # If no photos found, create a blank placeholder
            if not photos:
                placeholder = "output/images/placeholder.jpg"
                if not os.path.exists(placeholder):
                    from PIL import Image, ImageDraw
                    img = Image.new("RGB", (1280, 720), color=(200, 200, 200))
                    draw = ImageDraw.Draw(img)
                    draw.text((50, 350), "No Image Found", fill=(0, 0, 0))
                    img.save(placeholder)
                saved_paths.append(placeholder)

        return saved_paths
