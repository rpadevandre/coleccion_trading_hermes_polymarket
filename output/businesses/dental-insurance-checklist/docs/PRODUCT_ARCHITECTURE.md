# Product Architecture — Dental Insurance Checklist Assistant

    ## Sector

    Dental operations / insurance verification

    ## Frontend views

    - Patient pre-visit intake page
- Insurance card/photo upload page
- Benefits status page
- Treatment estimate explanation page
- Practice-facing validation landing

    ## Backend / motor

    The motor is the operational workflow layer. It does not try to be a generic chatbot; it converts messy inbound information into structured, reviewable, auditable work.

    - Collects patient insurance details before the visit
- Generates verification checklist for front desk staff
- Tracks missing eligibility/benefits fields
- Creates patient-friendly benefit summary drafts
- Flags high-risk denial/confusion cases for human review

    ## Admin panel views

    - Insurance verification queue
- Patient verification detail
- Missing information tracker
- Payer checklist templates
- Treatment coordinator notes view
- Compliance/audit log
