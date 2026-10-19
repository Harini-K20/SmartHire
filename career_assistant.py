
def get_career_answer(
    question,
    match_score,
    matched_skills,
    missing_skills
):
    question = question.lower()

    if any(word in question for word in ["score", "match", "percentage"]):
        return (
            f"Your required-skill coverage is {match_score}%. "
            "This measures recognized job skills found in your resume, "
            "not your probability of getting hired."
        )

    elif any(word in question for word in ["missing", "gap", "lack"]):
        if missing_skills:
            return (
                "The skills to develop are: "
                + ", ".join(missing_skills)
                + ". Start with the skills marked high priority "
                "in your learning roadmap."
            )
        return "No missing skills were detected from our current skill list."

    elif any(word in question for word in ["learn", "study", "first", "start"]):
        if missing_skills:
            return (
                f"Start by learning {missing_skills[0]}. "
                "Practice with a small project, then update your resume "
                "with skills you have genuinely learned."
            )
        return "Review the job description and build a project that demonstrates your skills."

    elif any(word in question for word in ["matched", "strength", "good at"]):
        if matched_skills:
            return "Your matching skills are: " + ", ".join(matched_skills) + "."
        return "No matching skills were detected yet."

    elif any(word in question for word in ["improve", "better", "resume"]):
        return (
            "Add relevant projects, describe what you built, "
            "mention the technologies you actually used, and include "
            "measurable results where possible. Tailor your resume "
            "to the job description."
        )

    else:
        return (
            "I can help with your match score, missing skills, "
            "learning priorities, and resume improvement. "
            "Try asking: Which skills should I learn first?"
        )
