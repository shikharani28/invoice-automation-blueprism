# Invoice Processing Automation – Blue Prism Portfolio Project

## Overview
Automation that processes invoices end-to-end: reads invoice details, validates against rules, updates a system (or ERP simulator), and generates an output report.

## What it demonstrates
- Work Queues (items, retries, exception handling)
- Robust UI automation / app model usage
- Data validation & business rules
- Logging and reporting
- Config-driven design

## Tech Stack
- Blue Prism 7.5 (Trial)
- Excel / CSV (test data)
- (Optional) Python / OCR / email integration

## How to run
1. Update config (input folder, output folder)
2. Load sample invoices / test data
3. Run Dispatcher to populate queue
4. Run Worker to process items
5. Review output report

## Repository Structure
- /blueprism – process/object exports, screenshots
- /docs – architecture diagram, design notes
- /sample-data – fake invoices (no sensitive data)
- /output-samples – sample output report
