import os
import streamlit as st
from utils import get_openai_api_key, get_serper_api_key
from crewai import Agent, Task, Crew
from crewai_tools import (
    FileReadTool,
    ScrapeWebsiteTool,
    MDXSearchTool,
    SerperDevTool
)
import warnings
warnings.filterwarnings('ignore')

# API Keys setup
openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

# Streamlit inputs
st.title("AI-Powered Resume + Interview Preparer")

job_posting_url = st.text_input("Job Description URL")
github_url = st.text_input("GitHub Repo URL")
personal_writeup = st.text_area("Personal Write-up")

uploaded_resume = st.file_uploader("Upload your resume.md", type=['md'])

if uploaded_resume is not None:
    with open("./uploaded_resume.md", "wb") as f:
        f.write(uploaded_resume.read())

    read_resume = FileReadTool(file_path="./uploaded_resume.md")
    semantic_search_resume = MDXSearchTool(mdx="./uploaded_resume.md")

    # Agents
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    researcher = Agent(
        role="Tech Job Researcher",
        goal="Make sure to do amazing analysis on job posting to help job applicants",
        tools=[scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "As a Job Researcher, your prowess in navigating and extracting critical "
            "information from job postings is unmatched. Your skills help pinpoint the "
            "necessary qualifications and skills sought by employers, forming the foundation "
            "for effective application tailoring."
        )
    )

    profiler = Agent(
        role="Personal Profiler for Engineers",
        goal="Do incredible research on job applicants to help them stand out in the job market",
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        verbose=True,
        backstory=(
            "Equipped with analytical prowess, you dissect and synthesize information from diverse sources "
            "to craft comprehensive personal and professional profiles, laying the groundwork for personalized "
            "resume enhancements."
        )
    )

    resume_strategist = Agent(
        role="Resume Strategist for Engineers",
        goal="Find all the best ways to make a resume stand out in the job market.",
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        verbose=True,
        backstory=(
            "With a strategic mind and an eye for detail, you excel at refining resumes to highlight the most "
            "relevant skills and experiences, ensuring they resonate perfectly with the job's requirements."
        )
    )

    interview_preparer = Agent(
        role="Engineering Interview Preparer",
        goal="Create interview questions and talking points based on the resume and job requirements",
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        verbose=True,
        backstory=(
            "Your role is crucial in anticipating the dynamics of interviews. With your ability to formulate key "
            "questions and talking points, you prepare candidates for success, ensuring they can confidently address "
            "all aspects of the job they are applying for."
        )
    )

    # Tasks
    research_task = Task(
        description=(
            "Analyze the job posting URL provided ({job_posting_url}) to extract key skills, experiences, and qualifications required. "
            "Use the tools to gather content and identify and categorize the requirements."
        ),
        expected_output=(
            "A structured list of job requirements, including necessary skills, qualifications, and experiences."
        ),
        agent=researcher,
        async_execution=True
    )

    profile_task = Task(
        description=(
            "Compile a detailed personal and professional profile using the GitHub ({github_url}) URLs, and personal write-up "
            "({personal_writeup}). Utilize tools to extract and synthesize information from these sources."
        ),
        expected_output=(
            "A comprehensive profile document that includes skills, project experiences, contributions, interests, and communication style."
        ),
        agent=profiler,
        async_execution=True
    )

    resume_strategy_task = Task(
        description=(
            "Using the profile and job requirements obtained from previous tasks, tailor the resume to highlight the most relevant areas. "
            "Employ tools to adjust and enhance the resume content. Make sure this is the best resume even but don't make up any information. "
            "Update every section, including the initial summary, work experience, skills, and education. All to better reflect the candidate's abilities "
            "and how it matches the job posting."
        ),
        expected_output=(
            "An updated resume that effectively highlights the candidate's qualifications and experiences relevant to the job."
        ),
        output_file="tailored_resume.md",
        context=[research_task, profile_task],
        agent=resume_strategist
    )

    interview_preparation_task = Task(
        description=(
            "Create a set of potential interview questions and talking points based on the tailored resume and job requirements. "
            "Utilize tools to generate relevant questions and discussion points. Make sure to use these question and talking points to help the candidate "
            "highlight the main points of the resume and how it matches the job posting."
        ),
        expected_output=(
            "A document containing key questions and talking points that the candidate should prepare for the initial interview."
        ),
        output_file="interview_materials.md",
        context=[research_task, profile_task, resume_strategy_task],
        agent=interview_preparer
    )

    job_application_crew = Crew(
        agents=[researcher, profiler, resume_strategist, interview_preparer],
        tasks=[research_task, profile_task, resume_strategy_task, interview_preparation_task],
        verbose=True
    )

    if st.button("Run Resume Tailoring + Interview Prep"):
        result = job_application_crew.kickoff(inputs={
            'job_posting_url': job_posting_url,
            'github_url': github_url,
            'personal_writeup': personal_writeup
        })

        # Display output files
        st.success("Process completed!")
        if os.path.exists("tailored_resume.md"):
            with open("tailored_resume.md", "r") as f:
                st.subheader("Tailored Resume")
                st.code(f.read(), language='markdown')

        if os.path.exists("interview_materials.md"):
            with open("interview_materials.md", "r") as f:
                st.subheader("Interview Materials")
                st.code(f.read(), language='markdown')
