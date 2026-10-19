# SmartHire – Resume Analyzer & Job Matcher

SmartHire is a Python-based web application that analyzes resumes, compares candidate skills with job requirements, identifies skill gaps, and recommends learning resources.

## Features

- **Resume Analysis:** Upload a PDF resume and extract its text.
- **Skill Extraction:** Identify technical skills from resume content.
- **Job Matching:** Compare resume skills with required job skills and calculate a match score.
- **Skill Gap Analysis:** Identify missing skills.
- **Learning Recommendations:** Suggest topics and resources to improve missing skills.
- **Career Assistant:** Get rule-based guidance on job matching and resume improvement.
- **Analysis History:** Store and view previous analysis summaries using SQLite.
- **Automated Tests:** Includes unit tests for the skill extractor and job matcher.

## Technologies Used

- Python
- Streamlit
- PyMuPDF
- SQLite
- Regular Expressions
- Unittest

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Harini-K20/SmartHire.git
cd SmartHire
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install the required packages

Install the packages used by the project:

```bash
pip install streamlit pymupdf
```

If additional imports require other packages, install those as well.

### 4. Run the application

```bash
streamlit run app.py
```

### 5. Run the tests

```bash
python -m unittest test_smart_hire.py
```

## How It Works

1. Upload a PDF resume.
2. Extract text and identify technical skills.
3. Enter the skills required for a target job.
4. View the matching skills, missing skills, and match score.
5. Explore suggested learning resources and career guidance.

## Important Note

The skill extractor uses dictionary-based matching and the career assistant uses predefined rules. The match score indicates skill overlap with the entered job requirements; it does not predict hiring success.

## Privacy

Resume files are analyzed by the application and are not intentionally saved in the analysis database. Use caution when uploading resumes containing personal information.

## Future Improvements

- Expand skill recognition.
- Improve job-description analysis.
- Add more learning resources.
- Enhance the user interface and reporting features.

---

**Developed as a Python portfolio project.**
