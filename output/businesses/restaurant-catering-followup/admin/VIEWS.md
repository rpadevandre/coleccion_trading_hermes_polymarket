# Admin Views — Restaurant Catering Follow-Up Copilot

## Internal admin dashboard

### 1. Restaurant Workspace Overview
- Restaurant name, locations, plan, pilot dates, owner/operator contact.
- Catering pipeline metrics: leads imported, follow-ups due, drafts approved, recovered revenue entered.
- Risk flags: opt-out errors, high complaint sentiment, stale menu/pricing rules, failed imports.

### 2. Import Operations
- View all CSV/form/manual imports.
- Mapping status and validation errors.
- Duplicate review queue.
- Actions: remap columns, quarantine import, reprocess, download sanitized error report.
- Never display unnecessary full customer lists unless operator has support reason.

### 3. Follow-Up QA
- Sample drafts by restaurant and segment.
- Flags: inaccurate price/menu mention, unsafe allergy language, aggressive discounting, wrong event date, missing opt-out line.
- Admin can mark prompt/rule issue and request regeneration.
- Customer-facing drafts remain review-required after admin changes.

### 4. Pilot Tracker
- Tracks sales/validation progress for each restaurant:
  - audit requested,
  - data received,
  - first follow-up list delivered,
  - week 1 report,
  - recovered revenue proof,
  - monthly conversion decision.
- Stores pilot price, target recovered revenue, and notes for objections.

### 5. Account Suppression / Compliance
- Manage opt-outs, bounced emails, do-not-contact accounts, SMS quiet hours.
- Display audit trail for suppression changes.
- Bulk suppression upload for restaurants switching providers.

### 6. Template and Menu Rule Manager
- Internal library of message structures by event type and stage.
- Restaurant-specific caveats: delivery radius, minimum order, lead time, popular packages, unavailable items.
- Prompts can reference menu categories but should not invent prices or availability.

### 7. User Admin
- Roles: Owner, Manager, Staff, Viewer, Internal Operator.
- Invite/revoke staff.
- Reset MFA.
- Support impersonation with reason code and automatic expiry.

### 8. Audit Log
- Imports, exports, draft generation, approval actions, opt-out changes, admin access, and revenue attribution edits.
- Filter by workspace, actor, entity, date range, risk type.

## Admin operating rules

- No auto-send for customer outreach in the internal scaffold.
- No use of real restaurant customer data in demos.
- Complaint, refund, allergy, and legal language must route to staff review.
- Admin support access requires reason logging.
- Restaurant-level exports should exclude suppressed contacts by default.
