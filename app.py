import streamlit as st
from utils import extract_text_from_resume, analyze_resume


st.title("📝 AI Resume Analyzer & Job Fit Predictor")

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

job_description = st.text_area("Paste the Job Description Here", height=200)

if uploaded_file and job_description:
    resume_text = extract_text_from_resume(uploaded_file)

    with st.spinner("Analyzing..."):
        result = analyze_resume(resume_text, job_description)

    st.subheader("📊 Match Analysis")
    st.write(f"**Match Score:** {result['match_percentage']}%")
    st.write("**Missing Skills:**", ", ".join(result['missing_skills']))
    st.write("**Suggestions:**", result['suggestions'])
