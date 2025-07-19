import streamlit as st
from app.news_fetcher.fetcher import NewsFetcher
from app.script_generator.generator import ScriptGenerator
from app.voiceover.voice_engine import VoiceEngine
from app.visual_generator.visual_creator import VisualCreator
from app.video_assembler.assembler import VideoAssembler
from app.uploader.youtube_uploader import YouTubeUploader

st.set_page_config(page_title="AI News Generator", layout="centered")
st.title("📰 AI News Generator")

# Session storage
if "articles" not in st.session_state:
    st.session_state.articles = []
if "script" not in st.session_state:
    st.session_state.script = ""
if "audio_path" not in st.session_state:
    st.session_state.audio_path = ""
if "images" not in st.session_state:
    st.session_state.images = []
if "video_path" not in st.session_state:
    st.session_state.video_path = ""

# Fetch News
if st.button("🔎 Fetch News"):
    st.session_state.articles = NewsFetcher().fetch_top_news()
    for i, a in enumerate(st.session_state.articles):
        st.markdown(f"**{i+1}. {a['title']}**")
        st.caption(a['content'])

# Summarize
if st.button("🧠 Generate Summary Script"):
    if not st.session_state.articles:
        st.warning("Fetch news first!")
    else:
        script = ScriptGenerator().summarize(st.session_state.articles)
        st.session_state.script = script
        st.text_area("📝 Generated Script", script, height=300)
        if len(st.session_state.script) > 500:
            st.warning("Voiceover limited to 500 characters due to gTTS limits.")


# Voice
if st.button("🔊 Generate Voiceover"):
    if not st.session_state.script:
        st.warning("Generate script first!")
    else:
        path = VoiceEngine().generate(st.session_state.script)
        st.session_state.audio_path = path
        audio_file = open(path, "rb")
        st.audio(audio_file.read(), format="audio/mp3")

# Images
if st.button("🖼️ Generate Visuals"):
    if not st.session_state.articles:
        st.warning("Fetch news first!")
    else:
        keywords = [a["title"] for a in st.session_state.articles]
        st.session_state.images = VisualCreator().fetch_images(keywords)
        for img in st.session_state.images:
            st.image(img, width=350)

# Video
if st.button("🎞️ Create Video"):
    if not st.session_state.images or not st.session_state.audio_path:
        st.warning("Need visuals and audio first!")
    else:
        video_path = VideoAssembler(
            image_paths=st.session_state.images,
            audio_path=st.session_state.audio_path
        ).assemble()

        st.session_state.video_path = video_path
        st.video(video_path)

# Upload
if st.button("📤 Simulate Upload"):
    if not st.session_state.video_path:
        st.warning("Generate video first!")
    else:
        link = YouTubeUploader().upload(st.session_state.video_path)
        st.success(f"Video uploaded (simulated): {link}")
