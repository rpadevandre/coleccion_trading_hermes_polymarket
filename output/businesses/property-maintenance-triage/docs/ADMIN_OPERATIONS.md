# Admin Operations — Property Maintenance Triage

## Operating Cadence

### Daily

- Review open `emergency` and `urgent` requests first.
- Check `needs_info` cases older than 24 hours.
- Review AI triage decisions with confidence below threshold.
- Confirm no prototype workspace contains real tenant PII or real unit addresses.

### Weekly

- Analyze repeat issue categories by property.
- Tune routing rules for vendor categories and after-hours escalation.
- Review tenant follow-up drafts that managers edited heavily.
- Export anonymized pilot metrics for validation.

### Monthly

- Re-score pilot: time-to-triage, time-to-dispatch, tenant follow-up count and willingness to pay.
- Archive stale demo requests.
- Review user access and role permissions.
- Refresh public content with non-sensitive maintenance workflow lessons.

## Admin Views Needed

- Portfolio list and setup wizard.
- Maintenance queue dashboard.
- Emergency/SLA risk board.
- Routing rule editor.
- Vendor directory.
- Audit event explorer.
- Demo data purge panel.

## Human Review Rules

- AI can classify urgency but cannot dispatch vendors autonomously in MVP.
- Emergency categories must be surfaced prominently: active leak, no heat in cold weather, electrical spark, lockout, gas smell, safety/security issue.
- Tenant-facing drafts must avoid legal admissions or promises of exact arrival times unless manager approves.
- Vendor summaries should include only necessary tenant/unit details.

## Support Playbook

| Issue | Response |
|---|---|
| Manager says urgency was wrong | Capture override reason and update category examples. |
| Tenant message lacks details | Send templated follow-up questions before work-order conversion. |
| Vendor route incorrect | Adjust trade/category routing rule and retest sample requests. |
| Real tenant data entered in demo | Remove data and record internal incident note. |

## Pilot KPI Targets

- 3 property managers run 25+ sample/demo requests through triage.
- 70%+ of requests receive useful category/urgency suggestions on first pass.
- Managers report at least 30% fewer manual follow-up messages on well-structured intake.
- At least 2 buyers state willingness to pay $149-$499/month depending on door count.
