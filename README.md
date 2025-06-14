# 📝 AI-Powered Resume Refinement & Interview Preparation Agent

## 📌 Project Description

This project leverages a multi-agent AI system to **analyze job descriptions**, **refine resumes for maximum alignment**, and **prepare interview materials**. The system uses CrewAI to coordinate specialized agents (Job Researcher, Personal Profiler, Resume Strategist, Interview Preparer). It automates:
- Extracting job requirements.
- Profiling the candidate’s skills and experience.
- Tailoring the resume to match the job posting.
- Generating interview questions and talking points.

---

## 🗓️ Week 1 Progress

### ✅ Completed Tasks
- Finalized the project goal: building an AI agent system to tailor resumes and generate interview materials for specific job postings.
- Defined system architecture:
  - Identified 4 key agent roles: Job Researcher, Profiler, Resume Strategist, Interview Preparer.
  - Chose CrewAI framework for multi-agent orchestration.
- Researched tools (e.g., `SerperDevTool`, `ScrapeWebsiteTool`, `MDXSearchTool`) for integration.

### ⚠️ Challenges Identified
- Ensuring agents collaborate seamlessly across dependent tasks (e.g., resume strategist depending on outputs from researcher and profiler).
- Designing tasks that produce structured, high-quality outputs consistently.

---

## 🗓️ Week 2 Progress

### ✅ Completed Tasks

#### Agent Implementation
- Implemented all 4 agents with unique goals, backstories, and appropriate tools.
- Integrated:
  - `SerperDevTool` for search queries.
  - `ScrapeWebsiteTool` for web scraping.
  - `FileReadTool` and `MDXSearchTool` for resume processing.

#### Task Design
- Defined and scripted tasks:
  - Extracting job requirements.
  - Building personal and professional profiles.
  - Tailoring resumes to match job descriptions.
  - Preparing interview materials.

### ⚠️ Challenges Identified
- Deciding on output file formats and paths for tailored resume and interview materials.
- Managing asynchronous task execution and context passing in CrewAI.

---

## 🗓️ Week 3 Progress

### ✅ Completed Tasks

#### Contextual Workflow Setup
- Configured Crew to link agent outputs using context.
- Ensured:
  - Resume refinement task consumes job requirements + profile.
  - Interview preparation task consumes refined resume + job requirements.

#### API Key & Environment Setup
- Set up environment variables securely for OpenAI and Serper API keys.
- Implemented model configuration (`gpt-3.5-turbo` as default).

### ⚠️ Challenges Identified
- Handling API rate limits and timeouts during web scraping and search queries.
- Structuring job requirement extraction to output consistently formatted results for downstream tasks.

---

## 🗓️ Week 4 Progress

### ✅ Completed Tasks

#### Full Pipeline Test
- Ran end-to-end execution using:
  - A real job posting URL (AI Fund example).
  - Sample GitHub profile and personal write-up.
  - Fake resume markdown file.
- Verified that agents:
  - Extract job requirements successfully.
  - Generate a detailed personal profile.
  - Produce a tailored resume that aligns bullet points with job description.
  - Output potential interview questions and talking points.

#### Output Handling
- Configured output files:
  - `tailored_resume.md` for the refined resume.
  - `interview_materials.md` for interview preparation content.

### ⚠️ Challenges Identified
- Execution time: full pipeline takes several minutes due to external queries and processing.
- Minor inconsistencies in how agents phrase refined bullet points (may require post-processing or fine-tuning prompts).

---
