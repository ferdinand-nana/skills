#!/usr/bin/env python3
"""Dump a .pdf file (CV) to plain text on stdout.

Usage:
    python3 read_pdf.py path/to/file.pdf
"""
import sys

from pypdf import PdfReader


def dump_pdf(path: str) -> str:
    reader = PdfReader(path)
    pages = (page.extract_text() or "" for page in reader.pages)
    return "\n".join(pages)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: read_pdf.py <file.pdf>")
    print(dump_pdf(sys.argv[1]))
