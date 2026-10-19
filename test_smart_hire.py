
import unittest

from skill_extractor import extract_skills
from job_matcher import compare_skills


class TestSkillExtractor(unittest.TestCase):

    def test_identifies_known_skills(self):
        text = "I know Python, Java, SQL and Git."
        skills = extract_skills(text)

        self.assertIn("Python", skills)
        self.assertIn("Java", skills)
        self.assertIn("SQL", skills)
        self.assertIn("Git", skills)

    def test_ignores_unrelated_text(self):
        text = "I enjoy reading books and playing games."
        skills = extract_skills(text)

        self.assertEqual(skills, [])

    def test_skill_is_not_matched_inside_another_word(self):
        text = "I use JavaScript for web development."
        skills = extract_skills(text)

        self.assertNotIn("Java", skills)


class TestJobMatcher(unittest.TestCase):

    def test_calculates_match_score(self):
        resume = ["Python", "Git"]
        required = ["Python", "SQL", "Git", "Django"]

        result = compare_skills(resume, required)

        self.assertEqual(result["match_score"], 50)
        self.assertEqual(
            result["matched_skills"],
            ["git", "python"]
        )
        self.assertEqual(
            result["missing_skills"],
            ["django", "sql"]
        )

    def test_all_skills_match(self):
        result = compare_skills(
            ["Python", "SQL"],
            ["Python", "SQL"]
        )

        self.assertEqual(result["match_score"], 100)
        self.assertEqual(result["missing_skills"], [])

    def test_no_matching_skills(self):
        result = compare_skills(
            ["Java"],
            ["Python", "SQL"]
        )

        self.assertEqual(result["match_score"], 0)
        self.assertEqual(
            result["matched_skills"],
            []
        )

    def test_empty_requirements(self):
        result = compare_skills(["Python"], [])

        self.assertEqual(result["match_score"], 0)
        self.assertEqual(result["missing_skills"], [])


if __name__ == "__main__":
    unittest.main()
