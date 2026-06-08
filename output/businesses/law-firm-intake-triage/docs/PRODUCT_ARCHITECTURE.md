# Product Architecture — Law Firm Intake Triage

    ## Frontend views

    - Landing page for law firm intake bottlenecks
- Practice-area intake form demo
- After-hours inquiry capture page
- Case quality scoring explainer
- Consultation request CTA

    ## Backend / motor

    The motor converts messy inbound information into structured, reviewable, auditable work. It should make operators faster, not silently replace judgment.

    - Captures inquiry details with practice-area-specific questions
- Classifies practice area and urgency
- Flags missing facts, conflict-check needs and jurisdiction issues for human review
- Generates attorney-ready intake summaries
- Routes leads to intake specialist or attorney based on rules

    ## Admin panel views

    - Intake queue by urgency/practice area
- Lead detail and attorney summary
- Practice area routing rules
- Conflict checklist status
- Source/channel analytics
- Rejected/unqualified lead review
