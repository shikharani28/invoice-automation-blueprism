\# PDF Invoice Extraction Component



\## Overview



This module contains the Python script used for extracting structured invoice data from \*\*text-based PDF invoices\*\*.



It is designed to be called externally by \*\*Blue Prism\*\*, following a modular architecture where:



\- Blue Prism handles orchestration, queue management, exception handling, and ERP interaction.

\- Python handles document parsing and structured data extraction.



This separation improves maintainability, testability, and scalability.



---



\## Script



`pdf\_invoice\_extract.py`



This script:

\- Reads a text-based PDF invoice

\- Extracts key header fields using pattern matching (regex)

\- Returns structured JSON output

\- Provides exit codes for integration handling



---



\## Supported Fields



The script attempts to extract:



\- Invoice Number

\- Invoice Date

\- Due Date

\- PO Number

\- Vendor Name

\- Subtotal

\- Tax

\- Total

\- Currency (default: USD)



Only \*\*text-based PDFs\*\* are supported.  

Scanned/image-based PDFs (OCR) are intentionally out of scope for this version.



---



\## Installation



Install dependencies using:



```bash

pip install -r ../requirements.txt

Or manually:

pip install pymupdf

Integration with Blue Prism

Blue Prism calls this script from a Code Stage using:
Integration with Blue Prism

python pdf_invoice_extract.py --pdf "<PdfPath>"

Exception Behaviour

The script returns:

| Exit Code | Meaning                    |
| --------- | -------------------------- |
| 0         | Successful extraction      |
| 2         | Input error (missing file) |
| 3         | Extraction failure         |


Limitations

Supports text-based PDFs only

Does not extract line-item tables

Assumes consistent invoice format
