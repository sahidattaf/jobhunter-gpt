from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from coverletter_generator import generate_cover_letter
from keyword_extractor import extract_keywords
from resume_optimizer import keyword_coverage, optimize_resume
from tracker import append_application, read_applications


class JobHunterCoreTests(unittest.TestCase):
    def test_keyword_extraction(self) -> None:
        text = "Python Python automation, customer success, and project management."
        keywords = extract_keywords(text, top_k=5)
        self.assertIn("python", keywords)
        self.assertTrue(len(keywords) <= 5)

    def test_keyword_coverage(self) -> None:
        present, missing = keyword_coverage("Python and CRM", ["python", "salesforce"])
        self.assertEqual(present, ["python"])
        self.assertEqual(missing, ["salesforce"])

    def test_resume_review_preserves_source(self) -> None:
        resume = "Sahid Attaf\nExperience with Python."
        job = "Seeking Python and automation experience."
        result = optimize_resume(resume, job)
        self.assertIn(resume, result)
        self.assertIn("human verification", result)

    def test_cover_letter_uses_verified_terms(self) -> None:
        letter = generate_cover_letter(
            "Experience with customer success and CRM.",
            "Customer success role using CRM.",
            "Example Company",
            "Customer Success Manager",
            "Sahid Attaf",
        )
        self.assertIn("Example Company", letter)
        self.assertIn("Sahid Attaf", letter)

    def test_tracker_round_trip(self) -> None:
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "applications.csv"
            append_application(path, {"Job Title": "AI Specialist", "Company": "Example"})
            rows = read_applications(path)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["Company"], "Example")


if __name__ == "__main__":
    unittest.main()
