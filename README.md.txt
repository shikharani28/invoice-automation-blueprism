# Invoice Processing Automation (Blue Prism)

## Overview
This project demonstrates an end-to-end **Invoice Processing Automation** built using **Blue Prism**, following enterprise-grade RPA design principles.  
The solution automates invoice intake, validation, posting to a target system, and operational reporting using a scalable, queue-driven architecture.

**Objective:**  
Reduce manual effort and errors in invoice processing by automating data validation, transaction handling, and reporting — using only sample data.

---

## What this project demonstrates
- Dispatcher / Worker design pattern
- Blue Prism Work Queues with retry logic
- Business vs System exception handling
- Config-driven and scalable automation
- UI automation against a simulated ERP system
- Operational reporting for audit and monitoring

---

## Architecture & Process Flow

![Architecture](docs/architecture.png)

This automation follows the **Blue Prism Dispatcher–Worker pattern** with queue-based orchestration to ensure scalability, reliability, and clear exception handling.

### 1. Input Layer
- **Vendor Master (Excel)** for reference and validation
- **Invoice data / documents** (sample only)
- All inputs are mock or dummy data used for learning and portfolio purposes

### 2. Dispatcher Process (Blue Prism)
The Dispatcher prepares and orchestrates the workload:
- Reads invoice input data
- Validates schema and mandatory fields
- Creates individual **queue items** for each invoice

This separation ensures clean orchestration and supports parallel processing.

### 3. Work Queue
A Blue Prism Work Queue is used to manage transactions:
- Enables **retry logic** for system exceptions
- Tracks item status and tags
- Supports scaling with multiple worker processes

### 4. Worker Process (Blue Prism)
The Worker performs transaction-level processing:
- Applies **business rule validations**
- Automates invoice posting using **UI automation**
- Handles exceptions in a structured manner:
  - **Business Exceptions** → validation failures, no retry
  - **System Exceptions** → technical failures, retried via queue

### 5. ERP Simulator
To avoid dependency on a real ERP system, the automation interacts with a lightweight **HTML-based ERP simulator**:
- Mimics invoice entry screens
- Enables safe and repeatable UI automation
- Contains no sensitive or real business data

Location:
- `docs/erp-simulator/invoice-form.html`

### 6. Output & Reporting
Processing results are captured in an **Excel output report**, providing:
- Invoice status (Success / Failed)
- Failure reason codes
- Processing timestamps and duration

This report supports monitoring, audit, and troubleshooting.

---

## Exception Handling (Mini Flow)

```text
                 Worker picks next queue item
                              │
                              ▼
                 Process invoice + ERP UI
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
              Success               Exception occurs
                 │                         │
     Mark Completed & Report       Classify exception
                                           │
                      ┌────────────────────┴────────────────────┐
                      │                                         │
                      ▼                                         ▼
            Business Exception                          System Exception
            (validation failure)                       (technical issue)
                      │                                         │
               No retry – report                     Retry via Work Queue
