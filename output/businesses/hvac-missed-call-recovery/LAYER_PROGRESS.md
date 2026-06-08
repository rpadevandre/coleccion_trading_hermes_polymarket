# Layer Progress — HVAC Missed-Call Recovery

## Frontend

- App navigation/state: upgraded to typed `RouteKey` navigation, accessible tab controls, active route context and cross-view CTA routing.
- Data model: expanded `businessMeta.ts` with HVAC-specific buyer promise, risk copy, validation questions, proof points, route metadata and sample missed-call queue items.
- Landing: replaced generic scaffold with buyer-validation messaging for owner-led HVAC teams, ROI/demo CTAs and no-PII guardrail copy.
- ROICalculator: implemented controlled inputs for missed calls/week, average ticket, job conversion rate and recovery rate with calculated monthly leakage/recovered-value outputs.
- DemoCallFlow: added capture/classify/route/prove workflow cards, explicit loading/error/empty/success state copy and sample owner review queue.
- FreeAuditForm: added non-sensitive operational qualification fields, required-field tracking, disabled CTA state and audit-to-pilot flow.
- PilotSignup: added pilot readiness selectors for buyer authority, success metric and timeline, including discovery-only disabled CTA state.
- Styling: replaced generic CSS with responsive HVAC-branded visual polish, sticky nav, hero cards, route context, calculator/result grids, queue cards, badges and mobile breakpoints.
- TypeScript/Vite support: added `src/vite-env.d.ts`, React type packages and Vite-compatible `moduleResolution: "Bundler"`.

## Backend motor

- CallIntakeService: Accept call transcript/manual entry, normalize caller/job/location/urgency fields.
- UrgencyClassifier: Classify emergency, next-day, maintenance, quote request, spam or needs-human-review.
- DispatchRouter: Route urgent jobs to owner/tech notification queues based on service area and rules.
- RevenueEstimator: Estimate saved/lost revenue and produce weekly recovery metrics.
- AuditLogService: Record every classification, human edit, notification and status transition.

## Admin panel

- OpsDashboard: KPIs: missed calls captured, urgent jobs, recovered revenue, response time.
- CallQueue: Review all inbound call items with AI classification and confidence.
- CallDetail: Transcript, extracted fields, dispatch decision, edit history and notes.
- RoutingRules: Configure service areas, emergency categories and notification recipients.
- Analytics: Weekly recovery trends, lead source breakdown and missed opportunity value.

## Verification

- `npx tsc --noEmit` — passed.
- `npm run build` — passed with Vite v8.0.16; output generated under `frontend/dist/`.

## Next implementation step

Continue one-business-at-a-time frontend deepening with `med-spa-lead-recovery` as the next recommended target from Andre's preference list. Do not deploy until Andre explicitly requests it.
