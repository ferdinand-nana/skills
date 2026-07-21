import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "generate_interview_doc.py"
SPEC = importlib.util.spec_from_file_location("generate_interview_doc", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def question(prompt: str) -> dict[str, str]:
    return {
        "context": "Recent production work -",
        "question": prompt,
        "answer": "Specific context, reasoning, evidence, outcome, and lessons learned.",
    }


class GenerateInterviewDocTest(unittest.TestCase):
    def test_generate_accepts_long_form_skill_labels(self) -> None:
        answers = {
            "name": "Smoke Test",
            "years_experience": "9",
            "categories": {
                "Exploration (HR Interview)": [
                    question("what changed in your role?"),
                    question("why are you looking to move now?"),
                ],
                "Technical Expertise (Java, Spring Boot, Backend Development)": [
                    question("what backend tradeoff mattered most?"),
                ],
                "Problem Solving, Debugging & Root Cause Analysis": [
                    question("what evidence exposed the root cause?"),
                ],
                "Testing, Quality & Continuous Improvement": [
                    question("how did you know the release was safe?"),
                ],
                "Agile Team Collaboration": [
                    question("how did you align teams under deadline?"),
                ],
                "Team Leading & Team Impact": [
                    question("what did end-to-end ownership look like?"),
                ],
            },
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            answers_path = Path(tmpdir) / "answers.json"
            output_path = Path(tmpdir) / "interview-notes.docx"
            answers_path.write_text(json.dumps(answers), encoding="utf-8")

            MODULE.generate(str(answers_path), str(output_path))

            self.assertTrue(output_path.exists())
            with ZipFile(output_path) as generated_doc:
                document_xml = generated_doc.read("word/document.xml").decode("utf-8")

        flattened = re.sub(r"<[^>]+>", " ", document_xml)
        self.assertNotRegex(flattened, r"\[[^\]]+\]")
        self.assertIn("what changed in your role?", flattened)
        self.assertIn("what did end-to-end ownership look like?", flattened)


if __name__ == "__main__":
    unittest.main()