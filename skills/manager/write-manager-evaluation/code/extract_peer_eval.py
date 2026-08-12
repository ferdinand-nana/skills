"""
extract_peer_eval.py

Extracts peer evaluation data from an xlsx file and generates a markdown file
following the Peer_Eval_Template.md format.

Usage:
    python extract_peer_eval.py <path_to_xlsx> [--period FY26] [--role "Software Engineer"]

Example:
    python extract_peer_eval.py peer/eval/Hazel_Mendoza.xlsx
    python extract_peer_eval.py peer/eval/Steven_Ramirez.xlsx --period FY26 --role "Senior Software Engineer"

Output:
    peer/eval/Peer_Eval_<Name>.md
"""

import argparse
import re
import sys
from pathlib import Path

import openpyxl

# Maps question titles to the self-evaluation sections they belong to
QUESTION_MAPS = {
    "Work Quality & Improvement": "The WHAT, Your GROWTH",
    "Communication & Collaboration": "The HOW",
    "Reliability & Accountability": "The HOW, Your GROWTH",
    "Growth & Technical Skills": "Your GROWTH",
    "Team Culture & Support": "The HOW, Your GROWTH",
}

QUESTION_TITLES = {
    "Work Quality & Improvement": (
        "Work Quality & Improvement\n"
        "Can you share any examples where my work stood out—either positively or where it could have been better? What could I do to improve?"
    ),
    "Communication & Collaboration": (
        "Communication & Collaboration\n"
        "How well do I communicate and collaborate with the team? Are there any situations where I could have been clearer or more helpful?"
    ),
    "Reliability & Accountability": (
        "Reliability & Accountability\n"
        "Do I consistently deliver on my responsibilities and own up to mistakes? Please share any examples that come to mind."
    ),
    "Growth & Technical Skills": (
        "Growth & Technical Skills\n"
        "What skills or areas should I focus on to grow as a developer? Have you noticed any improvements since last year?"
    ),
    "Team Culture & Support": (
        "Team Culture & Support\n"
        "How do I contribute to a positive team environment? What more could I do to support team morale and camaraderie?"
    ),
}


def match_question_key(cell_value: str) -> str | None:
    """Return the short question key if cell_value starts with a known question title."""
    for key in QUESTION_MAPS:
        if cell_value.strip().startswith(key):
            return key
    return None


def parse_xlsx(path: Path) -> tuple[str, list[dict]]:
    """
    Parse the xlsx file and return (subject_name, questions).

    questions is a list of dicts:
        {
            "key": short question key,
            "responses": [{"date": ..., "feedback": ..., "from": ...}, ...]
        }
    """
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    subject_name = None
    questions = []
    current_question = None
    reading_responses = False

    for row in ws.iter_rows(values_only=True):
        cell0 = str(row[0]).strip() if row[0] else ""
        cell1 = str(row[1]).strip() if row[1] else ""
        cell2 = str(row[2]).strip() if row[2] else ""

        # Detect subject name from "Responses for <Name>" rows
        if cell0.startswith("Responses for ") and subject_name is None:
            subject_name = cell0.replace("Responses for ", "").strip()

        # Detect question type header rows (e.g., "Question Type", "Question 1")
        if cell0 == "Question Type":
            reading_responses = False
            current_question = None
            continue

        # Detect question title row
        q_key = match_question_key(cell0)
        if q_key:
            current_question = {"key": q_key, "responses": []}
            questions.append(current_question)
            reading_responses = False
            continue

        # Detect "Date / Feedback / From" header
        if cell0 == "Date" and cell1 == "Feedback" and cell2 == "From":
            reading_responses = True
            continue

        # Read response rows
        if reading_responses and current_question and row[1] and row[2]:
            current_question["responses"].append({
                "date": row[0],
                "feedback": str(row[1]).strip(),
                "from": str(row[2]).strip(),
            })

    return subject_name, questions


def render_markdown(subject_name: str, period: str, role: str, questions: list[dict]) -> str:
    lines = []
    lines.append(f"# Peer Evaluation — {period} — {subject_name}, {role}")
    lines.append("")

    for question in questions:
        key = question["key"]
        full_title_lines = QUESTION_TITLES[key].split("\n")
        maps_to = QUESTION_MAPS[key]

        lines.append("---")
        lines.append("")
        lines.append(f"### Question: {full_title_lines[0]}")
        if len(full_title_lines) > 1:
            lines.append(full_title_lines[1])
        lines.append("")
        lines.append(f"Maps To: {maps_to}")
        lines.append("")

        for i, response in enumerate(question["responses"]):
            lines.append(f'Evaluator: **{response["from"]}**')
            lines.append("```")
            lines.append(response["feedback"])
            lines.append("```")
            if i < len(question["responses"]) - 1:
                lines.append("")
                lines.append("--")
                lines.append("")

        lines.append("")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def name_to_filename(name: str) -> str:
    """Convert 'Hazel Mendoza' → 'Peer_Eval_Hazel_Mendoza.md'"""
    sanitized = re.sub(r"[^\w\s]", "", name).strip()
    parts = sanitized.split()
    return "Peer_Eval_" + "_".join(parts) + ".md"


def main():
    parser = argparse.ArgumentParser(description="Extract peer evaluation from xlsx to markdown.")
    parser.add_argument("xlsx", help="Path to the xlsx file (e.g. peer/eval/Hazel_Mendoza.xlsx)")
    parser.add_argument("--period", default="FY26", help="Evaluation period (default: FY26)")
    parser.add_argument("--role", default="Software Engineer", help="Role of the person being evaluated")
    parser.add_argument("--output-dir", default="peer/eval", help="Output directory for the markdown file")
    args = parser.parse_args()

    xlsx_path = Path(args.xlsx)
    if not xlsx_path.exists():
        print(f"Error: File not found: {xlsx_path}", file=sys.stderr)
        sys.exit(1)

    subject_name, questions = parse_xlsx(xlsx_path)

    if not subject_name:
        print("Error: Could not detect subject name from the xlsx file.", file=sys.stderr)
        sys.exit(1)

    if not questions:
        print("Error: No questions/responses found in the xlsx file.", file=sys.stderr)
        sys.exit(1)

    markdown = render_markdown(subject_name, args.period, args.role, questions)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / name_to_filename(subject_name)

    output_file.write_text(markdown, encoding="utf-8")
    print(f"Created: {output_file}")
    print(f"Subject: {subject_name}")
    print(f"Questions: {len(questions)}")
    total_responses = sum(len(q['responses']) for q in questions)
    print(f"Total responses: {total_responses}")


if __name__ == "__main__":
    main()
