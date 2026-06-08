# Product Architecture — MSP Security Reporting Copilot

    ## Sector

    Managed IT / cybersecurity services

    ## Frontend views

    - Landing page for MSP monthly reporting pain
- Sample executive security report preview
- Client portal teaser
- Free report cleanup/audit request form
- Pricing/pilot page

    ## Backend / motor

    The motor is the operational workflow layer. It does not try to be a generic chatbot; it converts messy inbound information into structured, reviewable, auditable work.

    - Ingests exported alerts, tickets, endpoint/security metrics and manual notes
- Normalizes client/month/service categories
- Summarizes what happened, what was remediated and what remains risky
- Generates client-friendly executive reports and internal action lists
- Flags missing evidence, repeated issues and SLA gaps

    ## Admin panel views

    - Client reporting dashboard
- Monthly report builder
- Evidence/import review queue
- Risk register per client
- Template and tone settings
- Approval workflow before sending reports
