# YouTube_News_AI
# 📰 AI News Video Generator

An end-to-end modular Python application that:
- Fetches real-time news headlines
- Summarizes them using NLP transformers
- Converts the summary to voice using TTS
- Adds relevant stock images
- Compiles everything into a narrated video
- Uploads the final video to YouTube

> 🔍 Powered entirely by open-source tools and free APIs.

---

## ✨ Features

- ✅ Modular & object-oriented code structure
- ✅ News fetching via NewsAPI
- ✅ Summarization using Hugging Face transformers (bart-large-cnn)
- ✅ Voiceover generation with Coqui TTS
- ✅ Visuals from Pexels API
- ✅ Video assembly via MoviePy
- ✅ Uploads to YouTube using YouTube Data API v3

---

## 🧠 Tech Stack

| Component         | Tool/Library                      | Type        |
|------------------|------------------------------------|-------------|
| News Fetching    | NewsAPI                            | API         |
| Summarization    | facebook/bart-large-cnn            | AI / NLP    |
| TTS              | Coqui TTS (Tacotron2-DDC)          | AI / Audio  |
| Images           | Pexels API                         | API         |
| Video Editing    | MoviePy/Google veo 3               | Library/API |
| Uploading        | YouTube Data API v3 + OAuth        | API         |
| Config Mgmt      | python-dotenv                      | Env loader  |

---

⚠️ **Note:** This project contains some empty folders (e.g., `output/`, `logs/`) that are created in advance to store output files like MP3s, images, and videos at runtime.

---

## 🏗️ Project Structure

├── app.py

├── config.py

├── .env

├── requirements.txt

├── app/

│ ├── news_fetcher/

│ ├── script_generator/

│ ├── voiceover/

│ ├── visual_generator/

│ ├── video_assembler/

│ └── uploader/

├── output/

│ ├── audio/

│ ├── images/

│ └── videos/

└── logs/

🚀 What Happens When You Run It
✅ Fetches headlines via NewsAPI

🧠 Summarizes using BART transformer

🔊 Generates voiceover (Coqui TTS)

🖼️ Pulls relevant images from Pexels

🎞️ Assembles video using MoviePy

📤 Uploads to YouTube
