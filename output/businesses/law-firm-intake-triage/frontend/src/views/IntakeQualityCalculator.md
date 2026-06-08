# Frontend View — IntakeQualityCalculator

## Purpose

Estimate staff/attorney time lost on low-quality intake.

## Primary states

- Empty
- Loading
- Ready
- Needs review
- Error

## Data needed

- tenant_id/account context
- authenticated user role where private/admin
- item/list/query params relevant to this view/module

## UX / logic notes

- Keep actions explicit and reversible in MVP.
- Show confidence or status where AI is involved.
- Never hide human-review requirements behind automation language.
