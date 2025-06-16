# app/video_assembler/assembler.py
import os
from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips,
    CompositeVideoClip
)

class VideoAssembler:
    def __init__(self, fps: int = 24, image_duration: int = 5):
        """
        fps: frames per second of final video
        image_duration: seconds each image will appear
        """
        self.fps = fps
        self.image_duration = image_duration

    def assemble(
        self,
        script_text: str,
        audio_path: str,
        visuals: list[str],
        output_path: str = "output/videos/final_video.mp4"
    ) -> str:
        """
        Creates a video:
        - Each image is displayed for `image_duration` seconds
        - Audio is overlaid and trimmed/padded to match total duration
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        print("[VideoAssembler] Creating video...")

        # Load audio
        audio_clip = AudioFileClip(audio_path)
        audio_duration = audio_clip.duration

        # Create an ImageClip for each image
        clips = []
        for img_path in visuals:
            img_clip = ImageClip(img_path).set_duration(self.image_duration)
            img_clip = img_clip.resize(width=1280)  # ensure consistent width
            clips.append(img_clip)

        # Concatenate image clips
        video_clip = concatenate_videoclips(clips, method="compose")
        video_duration = video_clip.duration

        # If audio is longer than video, extend video duration by repeating last frame
        if audio_duration > video_duration:
            last_frame = clips[-1].to_ImageClip().set_duration(audio_duration - video_duration)
            video_clip = concatenate_videoclips([video_clip, last_frame], method="compose")
        # If audio is shorter, trim the video
        else:
            video_clip = video_clip.subclip(0, audio_duration)

        # Set audio
        video = video_clip.set_audio(audio_clip).set_fps(self.fps)
        video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        audio_clip.close()
        video_clip.close()
        return output_path
