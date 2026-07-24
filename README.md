# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python** and **Streamlit** that analyzes a user's resume, matches it against different job roles, and recommends the most suitable career opportunities based on the skills present in the resume.

---

## 📌 Project Overview

Finding the right job based on a resume can be difficult, especially for students and fresh graduates. This project simplifies that process by automatically extracting skills from a resume and comparing them with predefined job role requirements.

The application provides:

- 🎯 Top recommended job roles
- 📊 Match percentage for each job
- ✅ Matched skills
- ❌ Missing skills
- 📄 Resume analysis report

---

## 🚀 Features

- Upload resumes in PDF format
- Extract text from resumes using PDF processing
- Detect technical skills automatically
- Compare resume skills with multiple job roles
- Calculate skill match percentage
- Recommend Top 5 matching jobs
- Display matched and missing skills
- Interactive Streamlit interface

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Libraries
- Pandas
- PDFPlumber
- Matplotlib
- Streamlit

### Dataset
- Custom Job Role Dataset
- Custom Skills Dataset

---

## 📂 Project Structure

```text
Resume Analyzer/
│
├── practice.py              # Streamlit Frontend
├── resume_analyzer.py       # Resume Analysis Logic
├── analytics.py             # Data Analysis
├── hist.py                  # Visualization
├── resume_score.py          # Resume Score
├── Skills.csv               # Skills Database
├── Job Roles.csv            # Job Role Database
├── recommendations.csv      # Generated Recommendations
├── resumes/                 # Uploaded Resumes
└── README.md
```

---

## ⚙️ How It Works

1. User uploads a resume (PDF).
2. Resume text is extracted using PDFPlumber.
3. Skills are identified from the extracted text.
4. Skills are compared with predefined job roles.
5. Match percentage is calculated.
6. Top 5 job recommendations are generated.
7. Results are displayed to the user.

---

## 📊 Current Functionalities

- Resume Upload
- Resume Text Extraction
- Skill Detection
- Job Recommendation
- Match Percentage Calculation
- Recommendation Report Generation

---

## 🚧 Future Improvements

- Resume Score Dashboard
- Skill Gap Analysis
- Resume Improvement Suggestions
- AI-powered Resume Feedback
- Job Portal Integration
- ATS Compatibility Score
- Interactive Graphs and Charts
- Multi-page Resume Support

---

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

- Python Programming
- Data Processing
- File Handling
- PDF Parsing
- Pandas
- Streamlit
- Git & GitHub
- Project Structuring


---

## 👨‍💻 Author

**Shashank Sres**

B.Tech Computer Science (Data Science)

GitHub: https://github.com/pwrobin636282-bit