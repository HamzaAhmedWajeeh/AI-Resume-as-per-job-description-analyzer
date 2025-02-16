📝 AI Resume Analyzer & Job Fit Predictor

🚀 Overview

The AI Resume Analyzer & Job Fit Predictor is a Streamlit-based web application that allows users to upload their resumes (PDF or DOCX) and compare them against a job description. The app leverages Groq's LLaMA 3 AI model to analyze the resume and provide:

A match percentage (0-100%)

Missing skills based on the job description

Suggestions to improve the resume for better alignment

🎯 Features

📄 Upload Resumes (PDF or DOCX)

📝 Paste Job Description

🤖 AI-Powered Analysis using LLaMA 3 via Groq API

📊 Match Percentage Calculation

🎯 Skill Gap Identification

🛠 Resume Improvement Suggestions

🏗️ Tech Stack

Python 🐍

Streamlit (Frontend UI)

Groq API (AI processing via LLaMA 3)

PyMuPDF (PDF parsing)

python-docx (DOCX parsing)

python-dotenv (Environment variable management)

📦 Installation

1️⃣ Clone the Repository

git clone https://github.com/HamzaAhmedWajeeh/AI-Resume-as-per-job-description-analyzer.git
cd AI-Resume-as-per-job-description-analyzer

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up API Key

Create a .env file in the project root and add your Groq API Key:

GROQ_API_KEY=your_groq_api_key_here

🚀 Running the Application

streamlit run app.py

📌 Usage

1️⃣ Upload your resume (PDF/DOCX).
2️⃣ Paste the job description.
3️⃣ Click Analyze and view:

Match score

Missing skills

Resume improvement tips

📜 License

This project is licensed under the MIT License.

🤝 Contributing

Pull requests are welcome! If you'd like to contribute, please fork the repository and submit a PR.

📧 Contact

For questions or collaborations, reach out at hamzaahmedwajeeh@gmail.com.

