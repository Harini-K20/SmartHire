# SmartHire— Resume Skill Analyzer and Job Matcher

**SmartHire** is a Python-based web application that analyzes resumes, extracts technical skills, compares them with job requirements, and recommends areas for improvement.

## 🚀LIVE DEMO

Try SmartHire here: https://smarthire-mnst2vzymud4qcujnnwjmn.streamlit.app/

## ✨FEATURES

- **Resume Analysis:** Upload a PDF resume and extract its text.
- **Skill Extraction:** Identify technical skills from the resume.
- **Job Matching:** Compare resume skills against required job skills and calculate a match score.
- **Missing Skills:** Identify skills that need improvement.
- **Learning Recommendations:** Get suggestions for learning missing skills.
- **Career Assistant:** Get rule-based career guidance.
- **Analysis History:** Store analysis history locally using SQLite.

## 🛠️TECHNOLOGIES USED

- Python
- Streamlit
- PyMuPDF
- SQLite
- Regular Expressions
- Unit Testing

## 💻RUN LOCALLY

1. Clone this repository:

   `git clone https://github.com/Harini-K20/SmartHire.git`

2. Open the project folder:

   `cd SmartHire`

3. Install the dependencies:

   `pip install -r requirements.txt`

4. Run the application:

   `streamlit run app.py`

## 🧪RUN TESTS

`python -m unittest test_smart_hire.py`

## ⚠️LIMITATIONS

- Skill extraction uses predefined keywords and rules, so it may miss skills written in unusual formats.
- Career guidance is rule-based and does not replace professional career advice.
- SQLite history is stored locally and may not persist across cloud deployments.

## 🔒PRIVACY

Use sample resumes for testing. Avoid uploading resumes containing sensitive personal information unless you understand how the deployed application handles uploaded files.

## 👩‍💻PROJECT GOAL

Built to practice Python development, resume analysis, skill matching, and deployment using Streamlit Community Cloud.
