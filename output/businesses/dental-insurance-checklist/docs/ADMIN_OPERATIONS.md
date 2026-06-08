# Admin Operations — Dental Insurance Checklist Assistant

## Operating Cadence

### Daily

- Review verification queue aging.
- Check `exception` cases before the next business day schedule.
- Review AI-drafted notes for unsafe insurance guarantees or missing disclaimers.
- Confirm no demo workspace contains real patient identifiers.

### Weekly

- Compare pilot metrics against baseline: cases verified, minutes saved, blockers caught.
- Update payer-specific checklist templates from staff feedback.
- Review support tickets and group by confusion, bug, missing field or compliance concern.
- Export anonymized metrics for validation updates.

### Monthly

- Re-score go/no-go validation: willingness to pay, repeat usage and office manager urgency.
- Archive stale demo visits.
- Review access logs, MFA coverage and role assignments.
- Refresh public content with non-sensitive learnings.

## Admin Views Needed

- Practice workspace list.
- Queue health dashboard.
- Checklist template editor.
- Exception review board.
- Audit event explorer.
- Content/disclaimer settings.
- Demo data purge panel.

## Human Review Rules

- AI may draft but not finalize coverage determinations.
- Do not claim insurance payment is guaranteed.
- Do not store real patient data in prototype environments.
- Flag high-dollar procedures for extra review.
- Flag ambiguous frequency limits and waiting periods as `needs_human_review`.

## Support Playbook

| Issue | Response |
|---|---|
| Office asks for payer portal automation | Keep as future integration; MVP supports manual evidence capture only. |
| Staff enters real PHI in demo | Remove data, document incident internally, remind user of prototype limitations. |
| AI draft overstates coverage | Reject draft, tune template, add stronger disclaimer. |
| Checklist too long | Create procedure-specific compact template. |

## Pilot KPI Targets

- 3-5 dental offices agree to run a two-week checklist pilot.
- 50+ synthetic/demo verification cases processed in workflow tests.
- At least 2 offices state they would pay $99-$299/month if PMS notes and checklist templates are reliable.
- Staff report measurable reduction in repeated payer/patient follow-up tasks.
