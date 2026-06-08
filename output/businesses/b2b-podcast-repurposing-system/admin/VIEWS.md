# Admin Views — B2B Podcast Repurposing System

## Internal admin dashboard

### 1. Workspace Overview
- Workspace health: active episodes, failed ingest jobs, review backlog, exports this month.
- Commercial fields: plan, pilot status, renewal date, MRR, implementation owner.
- Risk flags: high claim-risk content, missing consent, overdue review, low transcription confidence.

### 2. Episode Operations Queue
- All jobs across customers with filters by status, workspace, owner, and failure type.
- Actions: retry ingest, rerun transcript, rerun extraction, pause workspace, escalate to human editor.
- Job detail includes source URL, file metadata, timestamps, model versions, cost estimate, and logs.

### 3. AI Output QA
- Sample AI drafts by asset type and workspace.
- Compare prompt/model version against output quality score.
- Mark issues: hallucinated claim, poor voice match, weak hook, quote mismatch, unsafe CTA.
- Create reusable prompt fix notes without editing customer content directly.

### 4. Brand Rule Manager
- View each customer's voice profile, glossary, forbidden claims, CTA library, and compliance notes.
- Change approval mode: customer-managed, internal-managed, or locked.
- Audit trail for every change.

### 5. User and Permission Admin
- Roles: Owner, Marketer, Editor, Viewer, Internal Operator.
- Invite/revoke users, reset MFA, inspect last login, export access audit.
- Customer support impersonation requires reason code and expires automatically.

### 6. Billing / Pilot Tracker
- Pilot pipeline: sample requested, sample delivered, paid pilot, monthly conversion, churn risk.
- Fields: pilot price, number of episodes, assets promised, assets delivered, outcome notes.
- Manual invoices only; no live payment integration in internal scaffold.

### 7. Security and Compliance
- Workspace data retention settings.
- Media deletion requests.
- Consent exceptions.
- Suspicious activity log.
- Export of audit events for a workspace.

## Admin safety rules

- Admins cannot publish to customer social channels from this system.
- Admins can regenerate drafts but cannot bypass customer approval on approved/exported labels.
- Raw media download should be disabled by default and time-limited if enabled.
- Every internal access to customer transcripts is logged with user, reason, and timestamp.
