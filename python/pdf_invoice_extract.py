#!/usr/bin/env python3
"""
Text-based PDF invoice extractor (no OCR)

Usage:
  python pdf_invoice_extract.py --pdf "C:\\path\\to\\invoice.pdf"

Output:
  Prints a single JSON object to stdout:
  {
    "ok": true,
    "pdf_path": "...",
    "extraction_mode": "text",
    "text_length": 1234,
    "fields": {
      "invoice_no": "...",
      "invoice_date": "...",
      "due_date": "...",
      "po_number": "...",
      "vendor": "...",
      "subtotal": 123.45,
      "tax": 7.89,
      "total": 131.34,
      "currency": "USD"
    },
    "warnings": []
  }

Exit codes:
  0 = success
  2 = input error (missing file, invalid args)
  3 = extraction error
"""

import os
import re
import json
import sys
import fitz  # PyMuPDF

def extract_text(pdf_path: str) -> str:
    text_parts = []
    doc = fitz.open(pdf_path)
    try:
        for page in doc:
            text_parts.append(page.get_text("text") or "")
    finally:
        doc.close()
    return "\n".join(text_parts).strip()

def find_first(patterns, text: str):
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE | re.MULTILINE)
        if m:
            return m.group(1).strip()
    return None

def parse_money(val):
    if not val:
        return None
    cleaned = re.sub(r"[^0-9.\-]", "", val.replace(",", ""))
    try:
        return float(cleaned)
    except Exception:
        return None

def parse_fields(text: str):
    invoice_no = find_first(
        [
            r"Invoice\s*#:\s*([A-Z0-9\-_/]+)",
            r"Invoice\s*No\.?:\s*([A-Z0-9\-_/]+)",
            r"Invoice\s*Number:\s*([A-Z0-9\-_/]+)",
        ],
        text,
    )

    invoice_date = find_first(
        [
            r"Invoice\s*Date:\s*([0-9\-\/]+)",
            r"Date:\s*([0-9\-\/]+)",
        ],
        text,
    )

    due_date = find_first(
        [
            r"Due\s*Date:\s*([0-9\-\/]+)",
        ],
        text,
    )

    po_number = find_first(
        [
            r"PO\s*Number:\s*([A-Z0-9\-_/]+)",
            r"P\.?O\.?\s*#:\s*([A-Z0-9\-_/]+)",
        ],
        text,
    )

    vendor = find_first(
        [
            r"From\s*\(Vendor\)\s*\n([^\n]+)",
            r"Vendor:\s*([^\n]+)",
        ],
        text,
    )

    subtotal_s = find_first([r"Subtotal:\s*([$]?[0-9,]+\.[0-9]{2})"], text)
    tax_s = find_first([r"Tax.*?:\s*([$]?[0-9,]+\.[0-9]{2})"], text)
    total_s = find_first([r"Total.*?:\s*([$]?[0-9,]+\.[0-9]{2})"], text)

    return {
        "invoice_no": invoice_no,
        "invoice_date": invoice_date,
        "due_date": due_date,
        "po_number": po_number,
        "vendor": vendor,
        "subtotal": parse_money(subtotal_s),
        "tax": parse_money(tax_s),
        "total": parse_money(total_s),
        "currency": "USD",
    }

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "--pdf":
        print(json.dumps({"ok": False, "error": "Usage: --pdf <path>"}))
        sys.exit(2)

    pdf_path = sys.argv[2]

    if not os.path.isfile(pdf_path):
        print(json.dumps({"ok": False, "error": f"PDF not found: {pdf_path}"}))
        sys.exit(2)

    try:
        text = extract_text(pdf_path)

        if not text or len(text) < 20:
            print(json.dumps({
                "ok": False,
                "error": "No extractable text found (PDF may not be text-based)."
            }))
            sys.exit(3)

        fields = parse_fields(text)

        warnings = []
        if not fields.get("invoice_no"):
            warnings.append("invoice_no_not_found")
        if not fields.get("total"):
            warnings.append("total_not_found")
        if not fields.get("vendor"):
            warnings.append("vendor_not_found")

        print(json.dumps({
            "ok": True,
            "extraction_mode": "text",
            "fields": fields,
            "warnings": warnings
        }))
        sys.exit(0)

    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e)}))
        sys.exit(3)

if __name__ == "__main__":
    main()
