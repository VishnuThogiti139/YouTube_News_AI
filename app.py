# app.py (root)
from app.fetcher import NewsFetcher
from app.generator import ScriptGenerator
from app.voice_engine import VoiceEngine
from app.visual_creator import VisualCreator
from app.assembler import VideoAssembler
from app.youtube_uploader import YouTubeUploader

def main():
    # 1. Fetch news
    print("Step 1: Fetching news...")
    news_fetcher = NewsFetcher()
    articles = news_fetcher.fetch_top_headline(limit=5)

    if not articles:
        print("No articles fetched. Exiting.")
        return

    # 2. Generate script
    print("Step 2: Generating script...")
    script = ScriptGenerator().generate_script(articles)
    # Save script to file for review:
    with open("output/script.txt", "w", encoding="utf-8") as f:
        f.write(script)

    # 3. Generate voiceover
    print("Step 3: Generating voiceover...")
    audio_path = VoiceEngine().generate_voice(script, output_path="output/audio/news_voice.mp3")

    # 4. Fetch or generate visuals
    print("Step 4: Generating visuals...")
    visuals = VisualCreator().generate_visuals(articles)

    # 5. Assemble video
    print("Step 5: Assembling video...")
    video_path = VideoAssembler().assemble(
        script_text=script,
        audio_path=audio_path,
        visuals=visuals,
        output_path="output/videos/final_video.mp4"
    )

    # 6. Upload to YouTube
    print("Step 6: Uploading to YouTube...")
    yt_link = YouTubeUploader().upload(
        video_file_path=video_path,
        title="Daily AI-Generated News Summary",
        description="This video is generated automatically via an AI pipeline.",
        tags=["news", "AI", "automated"],
        privacyStatus="public"
    )

    print("Done! Video available at:", yt_link)


if __name__ == "__main__":
    main()
