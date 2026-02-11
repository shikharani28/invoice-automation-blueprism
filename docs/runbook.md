# Invoice Processing Automation — Runbook

## Purpose
This runbook provides step-by-step instructions to **deploy, configure, and run** the Invoice Processing Automation built using **Blue Prism**.  
It is intended for developers, testers, and support users reviewing this portfolio project.

---

## Scope
This runbook covers:
- Importing Blue Prism artifacts
- Configuration and setup
- Running Dispatcher and Worker processes
- Understanding outputs and exceptions
- Basic troubleshooting

---

## Prerequisites
- Blue Prism installed (Trial / Learning edition is sufficient)
- Microsoft Excel installed
- Access to the ERP Simulator HTML file
- Sample input data available

---

## Repository Reference
This runbook applies to the following repository structure:

invoice-automation-blueprism/
├── blueprism/releases/
├── docs/
│ ├── runbook.md
│ └── erp-simulator/
├── sample-data/
│ ├── input/
│ └── output/


---

## Blue Prism Artifacts
### Processes
- **Invoice_Dispatcher**
  - Reads input data
  - Performs schema validation
  - Loads invoices into the Work Queue

- **Invoice_Worker**
  - Processes queue items
  - Applies business rules
  - Posts invoices to ERP Simulator
  - Handles exceptions and reporting

### Work Queue
- **Queue Name:** Invoice_Processing_Queue
- **Retry Settings:** Configured for system exceptions
- **Tagging:** Used for categorization and tracking

---

## Setup Instructions

### 1. Import Blue Prism Release
1. Open **Blue Prism**
2. Navigate to **File → Import → Release**
3. Import the `.bprelease` file from:
blueprism/releases/

4. Confirm successful import of processes, objects, and queue

---

### 2. ERP Simulator Setup
1. Navigate to:
docs/erp-simulator/invoice-form.html
2. Open the file in a web browser (Chrome or Edge recommended)
3. Ensure the form loads successfully
4. Keep the browser open during Worker execution

---

### 3. Input Data Setup
1. Place sample invoice data in:
sample-data/input/

2. Ensure:
- Required columns are present
- File format matches expected schema
- Only sample / dummy data is used

---

### 4. Output Location
Processed results will be generated in:
sample-data/output-samples/


---

## Execution Steps

### Step 1 — Run Dispatcher
1. Log into Blue Prism Control Room
2. Select **Invoice_Dispatcher**
3. Run the process
4. Validate:
   - Input files are read successfully
   - Queue items are created
   - No system exceptions occurred

---

### Step 2 — Run Worker
1. Ensure ERP Simulator browser is open
2. Select **Invoice_Worker** in Control Room
3. Run the process
4. Validate:
   - Queue items are processed
   - Invoices are posted to ERP Simulator
   - Output report is generated

---

## Exception Handling

### Business Exceptions
Raised when:
- Mandatory fields are missing
- Business rule validation fails
- Invoice data is invalid

Behavior:
- Item marked as **Exception**
- No retry attempted
- Failure reason captured in report

---

### System Exceptions
Raised when:
- Application is not responding
- UI element is not found
- Timeout or unexpected error occurs

Behavior:
- Item retried automatically via Work Queue
- Retries limited by queue configuration
- Final failure marked as **Exception** after retry exhaustion

---

## Output Report Details
The output report includes:
- Invoice Number
- Vendor Name
- Invoice Amount
- Processing Status (Success / Failed)
- Failure Type (Business / System)
- Failure Reason / Message
- Start Time
- End Time
- Processing Duration

---

## Validation Checklist
After execution, confirm:
- Dispatcher completed without errors
- Queue items reflect correct status
- Worker processed all available items
- Output report is populated correctly
- Failed items include meaningful reason codes

---

## Known Limitations
- ERP Simulator is a simplified HTML form
- No real ERP or database integration
- Designed for demonstration and learning purposes
- Performance optimized for clarity, not volume

---

## Troubleshooting

### Issue: Dispatcher fails to load data
- Verify input file path
- Check schema and required columns
- Confirm file is not open/locked

### Issue: Worker fails on UI interaction
- Ensure ERP Simulator browser is open
- Validate screen resolution and zoom
- Confirm application model elements are valid

### Issue: Repeated system exceptions
- Review Work Queue retry configuration
- Check application availability
- Inspect exception messages in Control Room

---

## Notes
- This automation uses **only sample data**
- No credentials or sensitive information are stored
- This runbook is part of a **portfolio demonstration project**
