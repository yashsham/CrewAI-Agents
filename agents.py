from crewai import Agent, LLM
from tools import yt_tool
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="gemini-1.5-flash",
    temperature=0.7,
    stream=True
)

blog_researcher = Agent(
    role="Blog Researcher",
    goal="Get relevant video content for {topic}",
    backstory="Expert in understanding YouTube videos on AI and Data Science topics",
    llm=llm,
    tools=[yt_tool],  # CrewAI BaseTool instance
    memory=True,
    verboe=True
)

blog_writer = Agent(
    role="Blog Writer",
    goal="Write a detailed blog using content from blog researcher",
    backstory="Expert in writing detailed and engaging AI/DS blogs, SEO-friendly",
    llm=llm,
    tools=[yt_tool],
    memory=True,
    verboe=True
)
