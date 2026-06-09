# React Implementation — Med Spa Lead Recovery

This frontend is a Vite + React + TypeScript prototype scaffold for internal incubation. The 2026-06-08 deepening pass converted the generic scaffold into a buyer-validation prototype focused on med-spa consult recovery.

## Views implemented

- `src/App.tsx` — Typed in-app navigation for all prototype routes with active buyer-signal context.
- `src/businessMeta.ts` — Expanded business model with route metadata, lead sources, treatment-line values, proof points, sample leads and compliance copy.
- `src/views/Landing.tsx` — Public validation page with pain framing, treatment-value examples, proof-point cards and audit CTA.
- `src/views/LeadLeakCalculator.tsx` — Controlled revenue calculator for weekly leads, miss rate, consult value and recovery target; includes empty state and treatment presets.
- `src/views/InstagramDMFlow.tsx` — No-real-data demo queue showing sample DMs/forms/missed calls, risk level, estimated value and human-approved draft flow.
- `src/views/FreeLeadAuditForm.tsx` — Controlled audit intake with required fields, disabled CTA, loading state, success state and no-PHI guardrail copy.
- `src/views/PilotSignup.tsx` — 14-day pilot conversion page with pilot timeline, controlled signup fields, guardrail checkbox and success summary.
- `src/styles.css` — Responsive med-spa visual polish: sticky navigation, pink/rose brand system, cards, forms, result panels, empty/success states and mobile grids.

## Local run after repo split

```bash
npm install
npm run dev
```

## Verification

```bash
npm install
npm run typecheck
npm run build
```

Latest run on 2026-06-08 succeeded: TypeScript passed and Vite produced `dist/index.html`, CSS and JS assets.

## Current limitation

This is intentionally local/prototype code under `output/businesses`. It is not deployed and has no production API connection yet. Form submissions are local UI states only and must not collect PHI or real patient/customer data.
