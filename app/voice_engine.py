# app/voiceover/voice_engine.py
import os
from TTS.api import TTS

class VoiceEngine:
    def __init__(self, model_name: str = "tts_models/en/ljspeech/tacotron2-DDC"):
        """
        Initializes Coqui TTS with a pre-trained model.
        (e.g. "tts_models/en/ljspeech/tacotron2-DDC")
        """
        self.tts = TTS(model_name)

    def generate_voice(
        self,
        script_text: str,
        output_path: str = "output/audio/news_voice.mp3"
    ) -> str:
        """
        Generates an MP3 at output_path.
        Returns the file path.
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        print("[VoiceEngine] Generating voice for script...")

        # Coqui TTS can take a long text; if it errors out, split into chunks.
        self.tts.tts_to_file(text=script_text, file_path=output_path)
        return output_path
