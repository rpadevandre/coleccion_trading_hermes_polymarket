# Admin Views — Dental Insurance Checklist Assistant

## 1. Verification queue

Columns:

- Task ID.
- Appointment date/time.
- Patient mock ID.
- Appointment/procedure type.
- Payer.
- Status.
- Missing field count.
- Exception flags.
- Assigned staff member.
- Time until appointment.

Filters:

- Due today.
- Missing information.
- Ready for review.
- Waiting on patient.
- Pre-auth/pre-determination likely.
- Inactive/uncertain eligibility.

## 2. Task detail

Panels:

- Appointment context.
- Checklist template.
- Source payer notes.
- Extracted benefit fields.
- Missing fields.
- Exception flags.
- PMS-ready note draft.
- Patient missing-info draft.
- Approval/audit timeline.

Actions:

- Approve summary.
- Edit extracted field.
- Mark field unknown.
- Request patient info.
- Copy PMS note.
- Return to staff for payer recheck.
- Close task.

## 3. Checklist template manager

- Procedure template name.
- Required benefit fields.
- Suggested payer questions.
- Documentation reminders.
- Standard disclaimers.
- Version history.

## 4. Exception dashboard

Cards:

- Inactive/uncertain coverage.
- Missing subscriber details.
- Waiting period flagged.
- Frequency limitation flagged.
- Prior authorization/pre-determination likely.
- Annual max/deductible unclear.

## 5. Practice settings

- User roles: admin, office manager, coordinator, readonly.
- Human approval requirement toggles.
- PMS note style.
- Retention policy placeholder.
- PHI handling reminder.
- Approved patient message language.

## 6. Metrics

- Tasks/week.
- Average verification completion time.
- Completion before appointment.
- Rework rate.
- Missing info caught before appointment.
- Human override rate.
- Audit/pilot ROI estimate.

## 7. Audit log

- Field-level edit history.
- Source note reference.
- AI output version.
- Approver identity.
- Export/copy events.
- Patient-message approval events.
