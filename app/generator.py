# app/script_generator/generator.py
from transformers import pipeline

class ScriptGenerator:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """
        Uses a summarization pipeline from Hugging Face.
        """
        self.summarizer = pipeline("summarization", model=model_name)

    def generate_script(self, articles: list[dict]) -> str:
        """
        Takes a list of article dicts: {"title": ..., "content": ...}
        Returns a single combined "script" string.
        """
        combined_sections = []
        for idx, article in enumerate(articles, start=1):
            text = article.get("content", "")
            if not text.strip():
                continue
            # summarization expects reasonably long text; if short, skip summarization.
            summary = text
            if len(text.split()) > 50:
                # limit length to avoid overlong pipeline calls
                summary = self.summarizer(
                    text,
                    max_length=60,
                    min_length=20,
                    do_sample=False
                )[0]["summary_text"]

            section = f"---\nNews {idx}: {article['title']}\n{summary}\n"
            combined_sections.append(section)

        # Join all sections into a single script
        final_script = "\n".join(combined_sections)
        return final_script
