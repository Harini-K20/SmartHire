
LEARNING_RESOURCES = {
    "django": {
        "priority": "High",
        "topic": "Django fundamentals and building web applications",
        "duration": "7 days",
        "resource": "https://docs.djangoproject.com/en/stable/intro/tutorial01/"
    },
    "flask": {
        "priority": "Medium",
        "topic": "Flask routes, templates, and web applications",
        "duration": "4 days",
        "resource": "https://flask.palletsprojects.com/en/stable/tutorial/"
    },
    "sql": {
        "priority": "High",
        "topic": "SQL queries, filtering, joins, and aggregation",
        "duration": "5 days",
        "resource": "https://sqlbolt.com/"
    },
    "mysql": {
        "priority": "Medium",
        "topic": "MySQL databases and CRUD operations",
        "duration": "4 days",
        "resource": "https://dev.mysql.com/doc/"
    },
    "rest api": {
        "priority": "High",
        "topic": "HTTP methods, API requests, and JSON",
        "duration": "4 days",
        "resource": "https://fastapi.tiangolo.com/tutorial/"
    }
}


def recommend_learning(missing_skills):
    recommendations = []

    for skill in missing_skills:
        details = LEARNING_RESOURCES.get(skill.casefold())

        if details:
            recommendations.append({
                "skill": skill.title(),
                **details
            })
        else:
            recommendations.append({
                "skill": skill.title(),
                "priority": "Medium",
                "topic": f"Learn the fundamentals of {skill}",
                "duration": "3 days",
                "resource": ""
            })

    return recommendations
