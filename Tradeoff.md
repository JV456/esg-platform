# Tradeoffs And Limitations

## Simplified Emission Factors

The platform uses simplified emission multipliers.

Tradeoff:

- easier implementation
- reduced scientific accuracy

---

## No Real SAP APIs

The platform uses CSV ingestion instead of:

- SAP IDocs
- BAPIs
- OData services

Tradeoff:

- reduced integration realism
- simpler implementation

---

## No OCR-Based PDF Parsing

Utility ingestion uses CSV files instead of PDF bills.

Tradeoff:

- simpler ingestion
- less realistic document handling

---

## Synchronous Processing

Ingestion currently processes synchronously.

Tradeoff:

- simpler architecture
- lower scalability

Production systems would typically use:

- Celery
- Kafka
- RabbitMQ

---

## No Authentication Roles

The platform currently does not implement:

- analyst roles
- admin roles
- RBAC permissions

Tradeoff:

- simpler implementation
- weaker access control

---

## Simplified Anomaly Detection

Flagging logic currently uses rule-based thresholds.

Examples:

- unrealistic fuel quantities
- zero electricity usage
- invalid travel routes

Tradeoff:

- easier implementation
- limited anomaly sophistication