# One-by-One Build Progress

Each business has explicit frontend routes/views, backend services/modules, and admin routes/views. The scheduled one-by-one frontend deepening pass should keep selecting exactly one business per run.

## Latest one-business frontend pass

- `hvac-missed-call-recovery` — Deepened React frontend prototype on 2026-06-08:
  - Typed app navigation/state and active route context.
  - Expanded frontend data model with HVAC buyer-validation metadata, sample calls, proof points and risk copy.
  - Rebuilt Landing, ROI Calculator, Demo Call Flow, Free Audit Form and Pilot Signup with concrete CTA flows.
  - Added controlled inputs, empty/success/loading/error-state copy, disabled CTA states and no-PII buyer-validation guardrails.
  - Replaced generic CSS with responsive HVAC-branded visual polish.
  - Verified with `npx tsc --noEmit` and `npm run build`.

## Current inventory

- `hvac-missed-call-recovery` — frontend views: 5, backend modules: 5, admin views: 5; React frontend deeply improved and build-verified.
- `property-maintenance-triage` — frontend views: 5, backend modules: 5, admin views: 5
- `construction-bid-inbox` — frontend views: 5, backend modules: 5, admin views: 5
- `dental-insurance-checklist` — frontend views: 5, backend modules: 5, admin views: 5
- `msp-security-reporting` — frontend views: 5, backend modules: 5, admin views: 5
- `med-spa-lead-recovery` — frontend views: 5, backend modules: 5, admin views: 5
- `law-firm-intake-triage` — frontend views: 5, backend modules: 5, admin views: 5
- `chiropractic-reactivation-engine` — frontend views: 5, backend modules: 5, admin views: 5
- `restaurant-catering-followup` — frontend views: 5, backend modules: 5, admin views: 5
- `b2b-podcast-repurposing-system` — frontend views: 5, backend modules: 5, admin views: 5

## Next recommended frontend target

- `med-spa-lead-recovery` — next highest-priority business from Andre's preference list that has not yet received a deep React frontend pass in this progress log.
