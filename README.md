# 📝 AI-Powered Resume Refinement & Interview Preparation Agent

---
## 🌐 Project Demo
- **Live Application:** [Visit the live app](http://54.87.62.251:8501)
- **Video Presentation:** [Watch the demo video](https://youtu.be/-jQv7cNEvMQ)
---
## 📌 Project Description

This project leverages a multi-agent AI system to **analyze job descriptions**, **refine resumes for maximum alignment**, and **prepare interview materials**. The system coordinate specialized agents (Job Researcher, Personal Profiler, Resume Strategist, Interview Preparer). It automates:
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

## 🗓️ Week 5 Progress

### ✅ Completed Tasks

#### 🏗️ Architecture & Deployment
- **Dockerized the entire application** for reproducibility and deployment on AWS EC2.
- Used **multi-stage Docker build** to minimize image size and exclude unnecessary files (`.dockerignore` covers secrets, local artifacts).
- Deployed on EC2, exposed app via Streamlit with proper port forwarding (8501).

#### ⚙️ Error Handling & Resilience
- Added:
  - API retry logic for external queries (search + scraping).
  - Exception handling in agent task execution (graceful failover + logs).
  - Input validation for user queries and resume files.

#### 🚀 Performance & Scalability
- Containerized architecture ensures horizontal scaling via Docker orchestration if needed.
- Tested with concurrent agent executions to validate no crashes under load.

#### 🔒 Security & Responsibility
- No secrets hardcoded; all credentials via **.env** (kept out of Docker image when possible).
- Minimal data persistence; no sensitive candidate data stored beyond session runtime.
- AI outputs filtered for **non-biased, professional phrasing**.
- Deployment hardened with AWS security group rules (only required ports open).

#### 📄 Documentation
- Started full **technical documentation**:
  - Architecture diagrams.
  - Agent design docs (roles, tools, dependencies).
  - Deployment guide (EC2 + Docker + Streamlit).
- Drafted **user manual**:
  - How to provide input files.
  - How to interpret outputs (`tailored_resume.md`, `interview_materials.md`).

---



## ⚡ Technical Highlights

| Area | Details |
|-------|---------|
| **Architecture** | Multi-agent system with context-aware task chaining; Dockerized for cloud deployment |
| **Code Quality** | Modularized Python code, clear separation of concerns, robust error handling |
| **Performance** | Docker-based scaling, efficient API usage with retries |
| **Error Handling** | API failures and data issues logged and handled gracefully |
| **Security** | No sensitive data persisted; .env used for secrets; minimal EC2 exposure |

---

## 🚀 Deployment Guide

### 1️⃣ Build the Docker image locally:  
```bash
docker build --platform=linux/amd64 -t resume-prep-app .
```
### 2️⃣ Save and transfer to EC2: 
```bash
docker save resume-prep-app > resume-prep-app.tar
```
```bash
scp -i resume-refine-key.pem resume-prep-app.tar ec2-user@<EC2-IP>:~/
```
### On EC2:
```bash
docker load -i resume-prep-app.tar
```
```bash
docker run -p 8501:8501 resume-prep-app
```

---
## 🔑 Security Measures

✅ **.env for secrets**  
✅ **AWS security group hardened** (only port 8501 exposed)  
✅ **No data retention** beyond session  
✅ **Responsible AI:** outputs filtered to avoid bias, no hallucinated credentials  

---

## 📋 Compliance Documentation

- **Data Privacy:** The system does not store or log personal data beyond the session. All files and inputs are ephemeral.  
- **Security Practices:** Deployment secured via AWS security groups, API keys managed via `.env`.  
- **Ethical AI:** All outputs reviewed or filtered to prevent bias, misrepresentation, or hallucination.  
- **Institutional/Legal Compliance:** The system follows privacy best practices aligned with general data protection principles (e.g., no PII storage, no data sharing).

---
## 🧪 Testing & Validation

- Implemented manual validation of agent tasks across multiple job postings, resumes, and GitHub profiles.
- Verified end-to-end flow with different input variations to ensure reliability.
- TODO: Add automated unit tests for utility functions (e.g., API key loaders, input validation functions).
- Test coverage report: N/A (manual testing performed; future work includes adding `pytest`-based unit tests for core logic).

---
## 📌 API & Input/Output Documentation

- **Inputs:**  
  - `job_posting_url` (string) — Link to a valid job posting webpage  
  - `github_url` (string) — Link to a valid GitHub repository  
  - `personal_writeup` (string) — Short personal summary  
  - `fake_resume.md` — Markdown file containing initial resume  

- **Outputs:**  
  - `tailored_resume.md` — Customized resume aligned to job description  
  - `interview_materials.md` — Generated interview questions and talking points  

- The system does not expose external API endpoints but works via internal agent task execution.

