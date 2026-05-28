# Breathe ESG Platform

## Project Overview

Breathe ESG Platform is a full-stack ESG (Environmental, Social, and Governance) data ingestion and emissions management system designed to simulate realistic enterprise sustainability workflows.

The platform ingests ESG-related operational data from multiple enterprise-style sources such as SAP exports, utility consumption reports, and travel systems. Uploaded data is normalized into standardized emission records, reviewed by analysts, and tracked through an audit-ready workflow.

---

# Features

## Backend Features

- Django REST Framework APIs
- PostgreSQL relational database
- ESG ingestion pipelines
- CSV and JSON upload handling
- Raw data preservation
- Emission normalization
- Suspicious record detection
- Analyst approval workflow
- Audit logging
- Dashboard metrics APIs

## Frontend Features

- React dashboard
- Upload management UI
- Pending review queue
- Approve/reject actions
- Live dashboard metrics
- REST API integration

---

# Tech Stack

## Frontend

- React
- Vite
- Axios
- React Router
- Tailwind CSS

## Backend

- Django
- Django REST Framework
- PostgreSQL
- Pandas

## Deployment

- Render Web Service
- Render PostgreSQL
- Render Static Site

---

# System Architecture

```text
React Frontend
       ↓
Django REST APIs
       ↓
PostgreSQL Database
```

---

# Ingestion Workflow

```text
Upload File/API Data
        ↓
Validate Input
        ↓
Store Raw Records
        ↓
Normalize ESG Data
        ↓
Generate Emission Records
        ↓
Flag Suspicious Records
        ↓
Analyst Review Workflow
        ↓
Audit Logging
```

---

# ESG Workflow

## Scope 1

Direct fuel emissions:

- diesel
- petrol
- natural gas

## Scope 2

Indirect electricity emissions.

## Scope 3

Travel and hotel-related emissions.

---

# Dashboard Features

- Total records
- Pending reviews
- Approved records
- Rejected records
- Flagged records

---

# Review Workflow

Imported records enter a pending review queue.

Analysts can:

- approve records
- reject records
- investigate suspicious values

Approved records become audit locked.

---

# Audit Logging

All review actions are tracked with:

- old values
- new values
- timestamps
- user references

This supports traceability and audit readiness.

---

# Local Setup

## Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

---

# API Endpoints

## Ingestion APIs

```text
POST /api/ingestion/upload/sap/
POST /api/ingestion/upload/utility/
POST /api/ingestion/upload/travel/
```

## Review APIs

```text
GET /api/review/dashboard/
GET /api/review/pending/
GET /api/review/flagged/
POST /api/review/approve/<id>/
POST /api/review/reject/<id>/
```

---

# Future Improvements

- Real SAP API integration
- OCR-based PDF ingestion
- Role-based authentication
- Asynchronous ingestion queues
- ML anomaly detection
- ESG reporting exports
- Real emission factor databases
- Kafka event streaming