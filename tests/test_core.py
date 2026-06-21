from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from candidate_profile import validate_profile, load_profile
from coverletter_generator import (
    generate_cover_letter,
    extract_resume_summary,
    extract_verified_strengths,
    clean_keyword_phrases,
    build_alignment_sentence,
)
from fit_scorer import score_fit, format_score_report
from job_search_agent import prepare_application
from keyword_extractor import extract_keywords
from resume_optimizer import keyword_coverage, optimize_resume
from tracker import append_application, read_applications


# ── Original core tests ───────────────────────────────────────────────────────

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


# ── Candidate profile validation tests ───────────────────────────────────────

class CandidateProfileValidationTests(unittest.TestCase):
    def _base(self) -> dict:
        return {"full_name": "Sahid Attaf", "email": "sahid@example.com",
                "target_job_titles": ["AI Specialist"], "verified_skills": ["python"]}

    def test_valid_profile_passes(self) -> None:
        result = validate_profile(self._base())
        self.assertEqual(result["full_name"], "Sahid Attaf")

    def test_missing_full_name_raises(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            validate_profile({})
        self.assertIn("full_name", str(ctx.exception))

    def test_empty_full_name_raises(self) -> None:
        with self.assertRaises(ValueError):
            validate_profile({"full_name": "   "})

    def test_placeholder_name_rejected(self) -> None:
        for placeholder in ("Candidate Name", "Jane Doe", "John Doe", "Your Name"):
            with self.subTest(placeholder=placeholder):
                with self.assertRaises(ValueError) as ctx:
                    validate_profile({"full_name": placeholder})
                self.assertIn("placeholder", str(ctx.exception).lower())

    def test_invalid_email_rejected(self) -> None:
        bad = dict(self._base())
        bad["email"] = "not-an-email"
        with self.assertRaises(ValueError) as ctx:
            validate_profile(bad)
        self.assertIn("email", str(ctx.exception))

    def test_valid_email_accepted(self) -> None:
        good = dict(self._base())
        good["email"] = "real@domain.org"
        result = validate_profile(good)
        self.assertEqual(result["email"], "real@domain.org")

    def test_target_job_titles_must_be_list(self) -> None:
        bad = dict(self._base())
        bad["target_job_titles"] = "AI Specialist"
        with self.assertRaises(ValueError) as ctx:
            validate_profile(bad)
        self.assertIn("list", str(ctx.exception))

    def test_load_profile_from_file(self) -> None:
        with TemporaryDirectory() as td:
            profile_path = Path(td) / "profile.json"
            import json
            profile_path.write_text(
                json.dumps({"full_name": "Sahid Attaf", "email": "sahid@example.com"}),
                encoding="utf-8",
            )
            result = load_profile(profile_path)
            self.assertEqual(result["full_name"], "Sahid Attaf")


# ── Fit scorer tests ──────────────────────────────────────────────────────────

class FitScorerTests(unittest.TestCase):
    _RESUME = (
        "Sahid Attaf\n"
        "Python automation engineer with customer success and salesforce experience.\n"
        "Located in New York, open to remote work."
    )
    _JD = (
        "We are seeking a Python developer experienced in automation and customer success.\n"
        "Salesforce knowledge preferred. Remote position. Location: New York, NY."
    )
    _PROFILE = {
        "full_name": "Sahid Attaf",
        "verified_skills": ["python", "automation", "customer success", "salesforce"],
        "preferred_locations": ["New York, NY"],
        "remote_preference": "remote",
    }

    def test_returns_required_keys(self) -> None:
        result = score_fit(self._RESUME, self._JD, self._PROFILE)
        for key in ("total", "matched_requirements", "missing_requirements",
                    "verification_warnings"):
            self.assertIn(key, result)

    def test_score_within_range(self) -> None:
        result = score_fit(self._RESUME, self._JD, self._PROFILE)
        self.assertGreaterEqual(result["total"], 0)
        self.assertLessEqual(result["total"], 100)

    def test_strong_match_scores_above_50(self) -> None:
        result = score_fit(self._RESUME, self._JD, self._PROFILE)
        self.assertGreater(result["total"], 50)

    def test_missing_requirements_identified(self) -> None:
        resume = "No relevant experience here whatsoever."
        jd = "Must know Python, machine learning, and data analysis."
        result = score_fit(resume, jd, {})
        self.assertGreater(len(result["missing_requirements"]), 0)

    def test_matched_requirements_are_present_in_resume(self) -> None:
        result = score_fit(self._RESUME, self._JD, self._PROFILE)
        resume_lower = self._RESUME.lower()
        for term in result["matched_requirements"]:
            self.assertIn(term.lower(), resume_lower,
                          f"'{term}' was reported matched but not found in resume")

    def test_unmatched_profile_skills_generate_warnings(self) -> None:
        profile = dict(self._PROFILE)
        profile["verified_skills"] = ["python", "quantum-computing"]
        result = score_fit(self._RESUME, self._JD, profile)
        warning_text = " ".join(result["verification_warnings"]).lower()
        self.assertIn("quantum-computing", warning_text)

    def test_empty_resume_raises(self) -> None:
        with self.assertRaises(ValueError):
            score_fit("", self._JD, {})

    def test_empty_jd_raises(self) -> None:
        with self.assertRaises(ValueError):
            score_fit(self._RESUME, "", {})

    def test_format_score_report_contains_total(self) -> None:
        result = score_fit(self._RESUME, self._JD, self._PROFILE)
        report = format_score_report(result)
        self.assertIn(str(result["total"]), report)
        self.assertIn("/100", report)


# ── Tracker integration tests ─────────────────────────────────────────────────

class TrackerIntegrationTests(unittest.TestCase):
    def test_fit_score_persists_in_tracker(self) -> None:
        with TemporaryDirectory() as td:
            path = Path(td) / "applications.csv"
            append_application(path, {
                "Job Title": "AI Specialist",
                "Company": "CorpX",
                "Fit Score": "72",
            })
            rows = read_applications(path)
            self.assertEqual(rows[0]["Fit Score"], "72")

    def test_empty_fit_score_persists(self) -> None:
        with TemporaryDirectory() as td:
            path = Path(td) / "applications.csv"
            append_application(path, {"Job Title": "Analyst", "Company": "Corp"})
            rows = read_applications(path)
            self.assertEqual(rows[0]["Fit Score"], "")

    def test_multiple_rows_tracked(self) -> None:
        with TemporaryDirectory() as td:
            path = Path(td) / "applications.csv"
            append_application(path, {"Job Title": "Role A", "Company": "Co1", "Fit Score": "80"})
            append_application(path, {"Job Title": "Role B", "Company": "Co2", "Fit Score": "60"})
            rows = read_applications(path)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[1]["Fit Score"], "60")


# ── Complete package generation test ─────────────────────────────────────────

class PackageGenerationTests(unittest.TestCase):
    def _profile(self) -> dict:
        return {
            "full_name": "Sahid Attaf",
            "verified_skills": ["python", "automation"],
            "preferred_locations": ["New York, NY"],
            "remote_preference": "remote",
        }

    def test_package_creates_all_output_files(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            resume_file = root / "resume.txt"
            job_file = root / "job.txt"
            resume_file.write_text(
                "Sahid Attaf\nPython automation engineer.", encoding="utf-8"
            )
            job_file.write_text(
                "Python developer for automation. Remote. New York, NY.", encoding="utf-8"
            )
            output_dir = root / "applications"
            tracker = root / "tracker.csv"

            pkg = prepare_application(
                resume_path=resume_file,
                job_path=job_file,
                company="Test Corp",
                title="Python Developer",
                source_url="https://example.com/jobs/1",
                candidate_name="Sahid Attaf",
                profile=self._profile(),
                output_dir=output_dir,
                tracker_path=tracker,
            )

            self.assertTrue((pkg / "resume-review.txt").exists())
            self.assertTrue((pkg / "cover-letter.txt").exists())
            self.assertTrue((pkg / "application-details.txt").exists())

    def test_package_records_fit_score_in_tracker(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            resume_file = root / "resume.txt"
            job_file = root / "job.txt"
            resume_file.write_text(
                "Sahid Attaf\nPython automation engineer.", encoding="utf-8"
            )
            job_file.write_text(
                "Python developer for automation. Remote.", encoding="utf-8"
            )
            tracker = root / "tracker.csv"

            prepare_application(
                resume_path=resume_file,
                job_path=job_file,
                company="Test Corp",
                title="Python Developer",
                source_url="https://example.com/jobs/2",
                candidate_name="Sahid Attaf",
                profile=self._profile(),
                output_dir=root / "applications",
                tracker_path=tracker,
            )

            rows = read_applications(tracker)
            self.assertEqual(len(rows), 1)
            self.assertTrue(rows[0]["Fit Score"].isdigit())

    def test_package_without_profile_leaves_score_blank(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            resume_file = root / "resume.txt"
            job_file = root / "job.txt"
            resume_file.write_text("Sahid Attaf\nExperience.", encoding="utf-8")
            job_file.write_text("Looking for Python experience.", encoding="utf-8")
            tracker = root / "tracker.csv"

            prepare_application(
                resume_path=resume_file,
                job_path=job_file,
                company="Acme",
                title="Analyst",
                source_url="https://example.com/jobs/3",
                candidate_name="Sahid Attaf",
                profile=None,
                output_dir=root / "applications",
                tracker_path=tracker,
            )

            rows = read_applications(tracker)
            self.assertEqual(rows[0]["Fit Score"], "")

    def test_details_file_contains_fit_score(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            resume_file = root / "resume.txt"
            job_file = root / "job.txt"
            resume_file.write_text(
                "Sahid Attaf\nPython automation engineer.", encoding="utf-8"
            )
            job_file.write_text(
                "Python developer for automation tasks. Remote.", encoding="utf-8"
            )

            pkg = prepare_application(
                resume_path=resume_file,
                job_path=job_file,
                company="Acme",
                title="Dev",
                source_url="https://example.com/jobs/4",
                candidate_name="Sahid Attaf",
                profile=self._profile(),
                output_dir=root / "applications",
                tracker_path=root / "tracker.csv",
            )

            details = (pkg / "application-details.txt").read_text(encoding="utf-8")
            self.assertIn("Fit Score", details)
            self.assertIn("/100", details)
            self.assertIn("NEXT ACTION", details)


# ── Cover letter v2 tests ─────────────────────────────────────────────────────

class CoverLetterV2Tests(unittest.TestCase):
    """Verify the improved cover letter generator produces clean, professional output."""

    _RESUME_WITH_SUMMARY = (
        "Jane Test\nNew York, NY\nEmail: jane@example.com\n\n"
        "Professional Summary\n"
        "Experienced customer success manager with a background in CRM tools "
        "and account management across SaaS companies.\n\n"
        "Core Skills\nCustomer success\nCRM\nAccount management\nSalesforce"
    )
    _RESUME_NO_SUMMARY = "Experience with customer success and CRM tools."
    _JD = (
        "Customer Success Manager role. Requires customer success and CRM experience. "
        "Account management skills preferred. Remote position."
    )
    _PROFILE = {
        "full_name": "Jane Test",
        "verified_skills": ["customer success", "CRM", "account management"],
        "preferred_locations": ["New York, NY"],
        "remote_preference": "remote",
    }

    def _letter(self, resume=None, jd=None, company="Example Corp",
                title="Customer Success Manager", name="Jane Test", profile=None):
        return generate_cover_letter(
            resume or self._RESUME_WITH_SUMMARY,
            jd or self._JD,
            company,
            title,
            name,
            profile=profile or self._PROFILE,
        )

    # ── Structure checks ──────────────────────────────────────────────────────

    def test_company_name_in_letter(self) -> None:
        self.assertIn("Example Corp", self._letter())

    def test_job_title_in_letter(self) -> None:
        self.assertIn("Customer Success Manager", self._letter())

    def test_candidate_name_in_letter(self) -> None:
        self.assertIn("Jane Test", self._letter())

    def test_letter_has_greeting(self) -> None:
        self.assertIn("Dear Hiring Manager", self._letter())

    def test_letter_has_closing(self) -> None:
        letter = self._letter()
        self.assertIn("Sincerely", letter)
        self.assertIn("Thank you", letter)

    def test_letter_length_reasonable(self) -> None:
        letter = self._letter()
        self.assertGreater(len(letter), 300)
        self.assertLess(len(letter), 2500)

    # ── Anti-fragment / no-raw-dump checks ───────────────────────────────────

    def test_no_raw_keyword_comma_dump(self) -> None:
        """Letter must not replicate the v1 pattern of raw extracted tokens in a comma list."""
        import re
        letter = generate_cover_letter(
            "Experience with customer success and CRM.",
            "Seeking customer success, CRM, salesforce experience.",
            "Corp",
            "Manager",
            "Jane Test",
        )
        # v1 produced: "relevant to customer, success, crm, salesforce"
        self.assertNotRegex(
            letter.lower(),
            r"relevant to \w+, \w+, \w+",
            "Cover letter still uses raw keyword comma-dump (v1 anti-pattern)",
        )

    def test_clean_keyword_phrases_removes_fragments(self) -> None:
        raw = ["real", "estate", "development", "real estate development", "github"]
        result = clean_keyword_phrases(raw)
        self.assertIn("real estate development", result)
        self.assertNotIn("real", result)
        self.assertNotIn("estate", result)
        self.assertNotIn("development", result)
        self.assertIn("github", result)  # not subsumed by any multi-word phrase

    def test_clean_keyword_phrases_keeps_standalone_singles(self) -> None:
        """Single words that are NOT components of any multi-word phrase are kept."""
        result = clean_keyword_phrases(["github", "notion", "business development"])
        self.assertIn("github", result)
        self.assertIn("notion", result)
        self.assertIn("business development", result)

    # ── Placeholder / validation checks ──────────────────────────────────────

    def test_placeholder_candidate_name_raises(self) -> None:
        for placeholder in ("Candidate Name", "candidate", "Your Name", "Name Here"):
            with self.subTest(placeholder=placeholder):
                with self.assertRaises(ValueError) as ctx:
                    generate_cover_letter(
                        self._RESUME_NO_SUMMARY, self._JD, "Corp", "Title", placeholder
                    )
                self.assertIn("placeholder", str(ctx.exception).lower())

    def test_empty_candidate_name_raises(self) -> None:
        with self.assertRaises(ValueError):
            generate_cover_letter(
                self._RESUME_NO_SUMMARY, self._JD, "Corp", "Title", ""
            )

    def test_missing_company_raises(self) -> None:
        with self.assertRaises(ValueError):
            generate_cover_letter(self._RESUME_NO_SUMMARY, self._JD, "", "Title", "Jane Test")

    def test_missing_title_raises(self) -> None:
        with self.assertRaises(ValueError):
            generate_cover_letter(self._RESUME_NO_SUMMARY, self._JD, "Corp", "", "Jane Test")

    # ── Summary extraction ────────────────────────────────────────────────────

    def test_extract_resume_summary_finds_section(self) -> None:
        summary = extract_resume_summary(self._RESUME_WITH_SUMMARY)
        self.assertIn("customer success manager", summary.lower())
        self.assertIn("crm", summary.lower())

    def test_extract_resume_summary_returns_empty_when_absent(self) -> None:
        summary = extract_resume_summary("Just some text. No sections here.")
        self.assertEqual(summary, "")

    def test_summary_used_in_letter_body(self) -> None:
        """When the resume has a Professional Summary, its content must appear in the letter."""
        letter = self._letter(resume=self._RESUME_WITH_SUMMARY)
        self.assertIn("customer success manager", letter.lower())

    def test_fallback_used_when_no_summary(self) -> None:
        """When there is no summary section, the letter still produces a background paragraph."""
        letter = self._letter(resume=self._RESUME_NO_SUMMARY)
        self.assertGreater(len(letter), 300)
        self.assertIn("Jane Test", letter)

    # ── Verified strengths ────────────────────────────────────────────────────

    def test_extract_verified_strengths_uses_profile_skills(self) -> None:
        strengths = extract_verified_strengths(
            self._RESUME_WITH_SUMMARY, self._JD, self._PROFILE
        )
        strength_lower = [s.lower() for s in strengths]
        self.assertIn("customer success", strength_lower)

    def test_extract_verified_strengths_no_invented_skills(self) -> None:
        """Skills that appear in the profile but NOT in resume must not be in strengths."""
        profile = {"verified_skills": ["quantum cryptography", "customer success"]}
        strengths = extract_verified_strengths(
            self._RESUME_WITH_SUMMARY, self._JD, profile
        )
        strength_lower = [s.lower() for s in strengths]
        self.assertNotIn("quantum cryptography", strength_lower)

    def test_build_alignment_sentence_two_items(self) -> None:
        result = build_alignment_sentence(["AI automation", "business development"])
        self.assertEqual(result, "AI automation and business development")

    def test_build_alignment_sentence_three_items(self) -> None:
        result = build_alignment_sentence(["A", "B", "C"])
        self.assertIn("and C", result)
        self.assertIn("A", result)

    def test_build_alignment_sentence_empty(self) -> None:
        result = build_alignment_sentence([])
        self.assertIn("attached resume", result)

    # ── No invented claims ────────────────────────────────────────────────────

    def test_letter_does_not_invent_unsupported_skills(self) -> None:
        """Skills absent from both resume and job description must not appear."""
        letter = generate_cover_letter(
            "Experience with Python scripting.",
            "Python developer needed.",
            "TechCorp",
            "Python Developer",
            "Jane Test",
        )
        self.assertNotIn("machine learning", letter.lower())
        self.assertNotIn("kubernetes", letter.lower())
        self.assertNotIn("blockchain", letter.lower())


if __name__ == "__main__":
    unittest.main()
