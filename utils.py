import fitz
import docx
from groq import Groq
import os
import json
from dotenv import load_dotenv


load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def extract_text_from_resume(uploaded_file):
    """Extract text from PDF or DOCX resume."""
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "pdf":
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = "\n".join([page.get_text("text") for page in doc])

    elif file_type == "docx":
        doc = docx.Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])

    else:
        text = ""

    return text

def analyze_resume(resume_text, job_description):
    """Call LLaMA 3 API via Groq to analyze resume against job description."""
    prompt = f"""
    Given the following resume and job description, analyze the match and provide:
    - A match percentage (0-100%).
    - Missing skills.
    - Suggested improvements.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Provide the response in JSON format with keys: match_percentage, missing_skills, suggestions.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_json = response.choices[0].message.content.replace("```json", "").replace("```", "").strip()

    try:
        parsed_result = json.loads(raw_json)
        return parsed_result
    except json.JSONDecodeError:
        return {"match_percentage": "N/A", "missing_skills": [], "suggestions": "Error in parsing response"}
