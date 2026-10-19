
def compare_skills(resume_skills, required_skills):
    """
    Compare resume skills with job requirements.
    """

    resume_set = {skill.casefold() for skill in resume_skills}
    required_set = {skill.casefold() for skill in required_skills}

    matched = sorted(resume_set & required_set)
    missing = sorted(required_set - resume_set)

    if required_set:
        score = round(len(matched) / len(required_set) * 100)
    else:
        score = 0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_score": score,
    }
