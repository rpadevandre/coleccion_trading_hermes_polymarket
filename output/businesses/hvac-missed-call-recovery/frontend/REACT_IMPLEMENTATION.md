# React Implementation — HVAC Missed-Call Recovery

This frontend is a Vite + React + TypeScript prototype scaffold for internal incubation. It is local-only under `output/businesses` and is not deployed.

## Latest frontend pass

- Reworked `src/App.tsx` from generic button tabs into typed `RouteKey` navigation with active-view context, accessible tab labels and cross-view CTA state.
- Expanded `src/businessMeta.ts` into a real buyer-validation data model with route metadata, HVAC-specific proof points, sample calls, validation questions, risk copy and pilot promise copy.
- Rebuilt all five page components with HVAC-specific content and interactive states:
  - `src/views/Landing.tsx` — Problem/market landing page with ROI/demo CTAs and no-PII validation copy.
  - `src/views/ROICalculator.tsx` — Controlled calculator for missed calls, average ticket, close rate and recovery rate, including empty/success states.
  - `src/views/DemoCallFlow.tsx` — Four-step capture/classify/route/prove workflow with loading/error/empty/success state copy and sample owner queue.
  - `src/views/FreeAuditForm.tsx` — No-PII operational audit form with required-field readiness state and disabled submit until qualified.
  - `src/views/PilotSignup.tsx` — Pilot readiness page with decision-maker, success metric, timeline state and disabled CTA for discovery-only buyers.
- Replaced `src/styles.css` with responsive visual polish: sticky nav, brand system, hero cards, route context, calculator results, queue cards, form states and mobile breakpoints.
- Added `src/vite-env.d.ts` and dev React type packages so CSS imports and JSX are TypeScript-compatible with current Vite/TS.
- Updated `tsconfig.json` module resolution to `Bundler` for current Vite/TypeScript compatibility.

## Verification

```bash
npx tsc --noEmit
npm run build
```

Result: both passed. Build output included `dist/index.html`, `dist/assets/index-sqX_pA2x.css`, and `dist/assets/index-BpDDF3fO.js`.

## Current limitation

This remains prototype code only. It has no production API connection, telephony connection, CRM integration, SMS sending, secrets or real customer data.
