import os
import warnings
from dotenv import load_dotenv, find_dotenv

warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

# === Load environment variables ===
def load_env():
    load_dotenv(find_dotenv())

load_env()

# Get API keys from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not set in environment variables or .env file.")
if not serper_api_key:
    raise ValueError("SERPER_API_KEY not set in environment variables or .env file.")

# Set them into os.environ if needed for downstream tools
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["SERPER_API_KEY"] = serper_api_key
# print(f"Using API key: {serper_api_key}")
# print(f"Using API key: {openai_api_key}")

# === Instantiate tools ===
docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

# === Create agents ===
researcher = Agent(
    role='Market Research Analyst',
    goal='Provide up-to-date market analysis of the AI industry',
    backstory='An expert analyst with a keen eye for market trends.',
    tools=[search_tool, web_rag_tool],
    verbose=True
)

writer = Agent(
    role='Content Writer',
    goal='Craft engaging blog posts about the AI industry',
    backstory='A skilled writer with a passion for technology.',
    tools=[docs_tool, file_tool],
    verbose=True
)

# === Define tasks ===
research = Task(
    description='Research the latest trends in the AI industry and provide a summary.',
    expected_output='A summary of the top 3 trending developments in the AI industry with a unique perspective on their significance.',
    agent=researcher
)

write = Task(
    description=(
        "Write an engaging blog post about the AI industry, based on the research analyst's summary. "
        "Draw inspiration from the latest blog posts in the directory."
    ),
    expected_output='A 4-paragraph blog post formatted in markdown with engaging, informative, and accessible content, avoiding complex jargon.',
    agent=writer,
    output_file='blog-posts/new_post.md'
)

# === Assemble and execute crew ===
crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    verbose=True,
    planning=True
)

# === Kickoff ===
crew.kickoff()
