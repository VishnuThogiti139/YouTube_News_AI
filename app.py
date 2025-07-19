from app.news_fetcher.fetcher import NewsFetcher
from app.script_generator.generator import ScriptGenerator
from app.voiceover.voice_engine import VoiceEngine
from app.visual_generator.visual_creator import VisualCreator
from app.video_assembler.assembler import VideoAssembler
from app.uploader.youtube_uploader import YouTubeUploader

def main():
    print("🔎 Fetching news...")
    news = NewsFetcher().fetch_top_news()

    print("🧠 Summarizing...")
    script = ScriptGenerator().summarize(news)

    print("🔊 Generating voiceover...")
    audio_path = VoiceEngine().generate(script)

    print("🖼️ Generating visuals...")
    keywords = [n["title"].split(" ")[0] for n in news]
    images = VisualCreator().fetch_images(keywords)

    print("🎞️ Creating video...")
    video = VideoAssembler().assemble(images, audio_path)

    print("📤 Uploading...")
    link = YouTubeUploader().upload(video)

    print("✅ Done! Watch here:", link)

if __name__ == "__main__":
    main()
