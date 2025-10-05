from crewai import tools
import google.generativeai as genai
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

# Gemini API
GEN_API_KEY = os.getenv("GEN_API_KEY")
genai.configure(api_key=GEN_API_KEY)

# YouTube API
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


# CrewAI Tool
class YouTubeGeminiTool(tools.BaseTool):
    name: str = "YouTube Gemini Tool"
    description: str = "Search YouTube videos and summarize them using Gemini"

    # ✅ Implement the required abstract method _run
    def _run(self, topic_channel_handle: str = "@krishnaik06") -> str:
        # Fetch latest videos
        request = youtube.search().list(
            part="snippet",
            q="AI, Machine Learning, Data Science",
            channelId="UCNU_lfiiWBdtULKOw6X0Dig",  # replace with actual channel ID
            maxResults=5
        )
        response = request.execute()
        titles = [item["snippet"]["title"] for item in response["items"]]

        # Summarize with Gemini
        model = genai.GenerativeModel("gemini-1.5-flash")
        summary = model.generate_content(f"Summarize these video titles:\n{titles}")
        return summary.text


# Create instance
yt_tool = YouTubeGeminiTool()

