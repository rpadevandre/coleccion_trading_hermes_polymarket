# One-by-One Build Progress

Each business has explicit frontend routes/views, backend services/modules, and admin routes/views. The scheduled one-by-one frontend deepening pass should keep selecting exactly one business per run.

## Latest one-business frontend pass

- `msp-security-reporting` — Deepened React frontend prototype on 2026-06-08:
  - Rebuilt `App.tsx` with typed route metadata, sticky navigation, active validation context and CTA-driven user intent state.
  - Expanded `businessMeta.ts` with MSP buyer persona, no-secrets promise, guardrails, proof points, stack options, sample security evidence, report sections and qualification signals.
  - Rebuilt Landing, Report Before/After, Client Proof Demo, Stack Audit Form and Pilot Signup as MSP-specific React pages.
  - Added controlled forms, workload calculator, stack checkboxes, interactive approval timeline, disabled CTA states, loading/success/empty states and buyer-validation copy.
  - Replaced generic CSS with responsive cybersecurity/MSP visual polish for dark hero panels, cards, comparison grids, forms, steppers, status badges and guardrails.
  - Added React type dependencies, `vite-env.d.ts`, `typecheck` script and TypeScript module-resolution update; verified with `npm install`, `npm run typecheck` and `npm run build`.

## Previously deepened frontend passes

- `med-spa-lead-recovery` — Deepened React frontend prototype on 2026-06-08:
  - Typed App navigation/state around route metadata and active buyer-signal context.
  - Expanded `businessMeta.ts` with med-spa buyer, treatment values, lead sources, proof points, sample lead queue and compliance/no-PHI guardrails.
  - Rebuilt Landing, Lead Leak Calculator, Instagram DM Flow, Free Lead Audit Form and Pilot Signup as med-spa-specific React pages.
  - Added controlled calculator/form fields, disabled CTAs, empty/loading/success states, pilot qualification copy and human-approval flows.
  - Replaced generic CSS with responsive rose/pink med-spa visual polish for cards, forms, result panels, queues and guardrails.
  - Added React type dependencies and a `typecheck` script; verified with `npm install`, `npm run typecheck` and `npm run build`.

- `hvac-missed-call-recovery` — Deepened React frontend prototype on 2026-06-08:
  - Typed app navigation/state and active route context.
  - Expanded frontend data model with HVAC buyer-validation metadata, sample calls, proof points and risk copy.
  - Rebuilt Landing, ROI Calculator, Demo Call Flow, Free Audit Form and Pilot Signup with concrete CTA flows.
  - Added controlled inputs, empty/success/loading/error-state copy, disabled CTA states and no-PII buyer-validation guardrails.
  - Replaced generic CSS with responsive HVAC-branded visual polish.
  - Verified with `npx tsc --noEmit` and `npm run build`.

## Current inventory

- `hvac-missed-call-recovery` — frontend views: 5, backend modules: 5, admin views: 5; React frontend deeply improved and build-verified.
- `med-spa-lead-recovery` — frontend views: 5, backend modules: 5, admin views: 5; React frontend deeply improved and build-verified.
- `msp-security-reporting` — frontend views: 5, backend modules: 5, admin views: 5; React frontend deeply improved and build-verified.
- `property-maintenance-triage` — frontend views: 5, backend modules: 5, admin views: 5
- `construction-bid-inbox` — frontend views: 5, backend modules: 5, admin views: 5
- `dental-insurance-checklist` — frontend views: 5, backend modules: 5, admin views: 5
- `law-firm-intake-triage` — frontend views: 5, backend modules: 5, admin views: 5
- `chiropractic-reactivation-engine` — frontend views: 5, backend modules: 5, admin views: 5
- `restaurant-catering-followup` — frontend views: 5, backend modules: 5, admin views: 5
- `b2b-podcast-repurposing-system` — frontend views: 5, backend modules: 5, admin views: 5

## Next recommended frontend target

- `property-maintenance-triage` — next highest-priority business from Andre's preference list that has not yet received a deep React frontend pass in this progress log.
