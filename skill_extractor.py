import re

SKILLS = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "Django",
    "Flask",
    "FastAPI",
    "Machine Learning",
    "Data Analysis",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Git",
    "GitHub",
    "REST API",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Streamlit",
    "Power BI",
    "Excel"
]


def extract_skills(resume_text):
    found_skills = []

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, resume_text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills