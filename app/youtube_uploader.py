# app/uploader/youtube_uploader.py
import os
import json
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from config import GOOGLE_OAUTH_CLIENT_JSON_PATH, YOUTUBE_REFRESH_TOKEN

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
TOKEN_PICKLE = "token.pickle"

class YouTubeUploader:
    def __init__(self):
        self.creds = None
        self._authenticate()

    def _authenticate(self):
        creds = None
        # If token.pickle exists, load credentials
        if os.path.exists(TOKEN_PICKLE):
            with open(TOKEN_PICKLE, "rb") as token_file:
                creds = pickle.load(token_file)

        # If no valid credentials, do OAuth flow
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                    GOOGLE_OAUTH_CLIENT_JSON_PATH, SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for next runs
            with open(TOKEN_PICKLE, "wb") as token_file:
                pickle.dump(creds, token_file)

        self.creds = creds

    def upload(
        self,
        video_file_path: str,
        title: str = "Automated News Video",
        description: str = "Created by AI-powered pipeline",
        tags: list[str] = None,
        privacyStatus: str = "public"
    ) -> str:
        """
        Uploads video_file_path to YouTube. Returns the video URL.
        """
        tags = tags or ["news", "AI", "automation"]
        youtube = googleapiclient.discovery.build(
            "youtube", "v3", credentials=self.creds
        )

        request_body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags
            },
            "status": {
                "privacyStatus": privacyStatus
            }
        }

        media_file = googleapiclient.http.MediaFileUpload(
            video_file_path, chunksize=-1, resumable=True
        )

        request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media_file
        )

        response = None
        print("[YouTubeUploader] Uploading to YouTube...")
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"  Uploaded {int(status.progress() * 100)}%")

        video_id = response.get("id")
        video_url = f"https://youtu.be/{video_id}"
        print(f"[YouTubeUploader] Upload complete: {video_url}")
        return video_url
