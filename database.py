
import sqlite3
import json
from datetime import datetime


DB_NAME = "smarthire.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS analysis_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                analyzed_at TEXT NOT NULL,
                match_score INTEGER NOT NULL,
                matched_skills TEXT NOT NULL,
                missing_skills TEXT NOT NULL,
                required_count INTEGER NOT NULL
            )
        """)


def save_analysis(result, required_count):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            INSERT INTO analysis_history (
                analyzed_at,
                match_score,
                matched_skills,
                missing_skills,
                required_count
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            result["match_score"],
            json.dumps(result["matched_skills"]),
            json.dumps(result["missing_skills"]),
            required_count
        ))


def get_recent_analyses(limit=10):
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row

        rows = conn.execute("""
            SELECT *
            FROM analysis_history
            ORDER BY id DESC
            LIMIT ?
        """, (limit,)).fetchall()

    history = []

    for row in rows:
        history.append({
            "Date": row["analyzed_at"],
            "Match Score": f'{row["match_score"]}%',
            "Required Skills": row["required_count"],
            "Matched Skills": ", ".join(
                json.loads(row["matched_skills"])
            ) or "None",
            "Missing Skills": ", ".join(
                json.loads(row["missing_skills"])
            ) or "None"
        })

    return history
