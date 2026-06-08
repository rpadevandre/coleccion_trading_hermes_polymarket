# Technical Spec — MSP Security Reporting Copilot

## Repo pattern

This folder simulates 3 future repos:

- `backend/` — imports, report engine, AI summarization, audit logs, tenant isolation.
- `frontend/` — public landing and client-facing report preview.
- `admin/` — MSP internal report builder and approval workflow.

## Core entities

- MSPAccount
- ClientCompany
- ReportPeriod
- ImportedEvidence
- SecurityFinding
- RiskSummary
- ClientReport
- ApprovalEvent
- UserRole

## Backend initial responsibilities

- Import CSV/JSON/manual notes from ticket/security tools.
- Normalize events by client and month.
- Redact secrets/tokens/password-like strings.
- Generate draft executive report sections.
- Store report revisions and approval events.
- Export Markdown/PDF-ready report content later.

## Frontend initial responsibilities

- Landing page.
- Sample report preview.
- Free report cleanup/audit request CTA.
- Public explainer of the monthly reporting problem.

## Admin initial responsibilities

- Client list.
- Import review queue.
- Report builder.
- Risk register.
- Approval and export controls.

## Non-goals for MVP

- No direct production integration with security tools yet.
- No automated client sending.
- No handling real secrets or raw sensitive logs until security/compliance is validated.
