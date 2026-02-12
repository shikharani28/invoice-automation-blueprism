# Invoice Processing Automation  
### Blue Prism + Python Integration

---

## Overview

This project demonstrates an enterprise-style **Invoice Processing Automation** solution built using:

- **Blue Prism** for orchestration and UI automation  
- **Python (PyMuPDF)** for structured PDF text extraction  

The solution follows production-ready design principles including:

- Dispatcher–Worker architecture  
- Queue-based transaction processing  
- Structured Business vs System exception handling  
- Modular integration with external components  
- Clean separation of concerns  

---

## Architecture

![Architecture](docs/architecture.png)

### Component Flow

Blue Prism Dispatcher
↓
Blue Prism Worker
↓
Python Extraction Module
↓
Structured JSON
↓
Validation → ERP Posting → Reporting


---

## Design Principles

### Separation of Responsibilities

**Blue Prism**
- Transaction orchestration  
- Queue management  
- Exception routing  
- ERP automation  
- Reporting  

**Python Module**
- PDF text extraction  
- Field parsing  
- Structured JSON output  

---

## PDF Extraction Module

Location:

python/pdf_invoice_extract.py


Features:
- Extracts structured data from text-based PDFs  
- Deterministic parsing (regex-based)  
- Returns structured JSON  
- Supports exit codes for automation control  

Detailed setup and standalone testing instructions:  
[`python/README.md`](python/README.md)

---

## Execution Flow

1. Place input PDFs in:
sample-data/input/


2. Run **Dispatcher**
- Scans input folder  
- Creates queue items  

3. Run **Worker**
- Calls Python extractor  
- Validates extracted fields  
- Posts to ERP simulator  
- Writes output report  
- Marks item Completed or Exception  

---

## Exception Handling Strategy

### Business Exceptions
- Missing required fields  
- Vendor validation failure  
- Total mismatch  

(No retry)

### System Exceptions
- Script execution failure  
- File access issues  
- Unexpected runtime errors  

(Retry handled via Work Queue configuration)

---

## Repository Structure

invoice-automation-blueprism/
├── blueprism/
│ └── releases/
├── docs/
│ ├── architecture.png
│ ├── runbook.md
│ └── erp-simulator/
├── sample-data/
│ ├── input/
│ └── output/
├── python/
│ ├── pdf_invoice_extract.py
│ └── README.md
├── requirements.txt
└── README.md


---

## Documentation

- Operational guide → [`docs/runbook.md`](docs/runbook.md)  
- Python extraction details → [`python/README.md`](python/README.md)  

---

## Release

Latest packaged Blue Prism release available under:
**Releases → v1.0**

---

## Notes

- Supports text-based PDFs only  
- Uses sample/demo data  
- ERP target is an HTML-based simulator  
- Designed for portfolio and learning purposes  

---

**Author**  
Shikha Rani  
Blue Prism Consultant
