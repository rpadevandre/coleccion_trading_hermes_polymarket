# Internal AI System — Property Maintenance Triage

    ## Principle

    Internal AI agents support classification, summarization, drafting and decision support. They should not silently take irreversible actions.

    ## Internal AIs

    - Maintenance Classifier AI: detects urgency and category
- Tenant Clarifier AI: asks for missing context/photos
- Vendor Brief AI: creates concise work-order summaries
- Duplicate Detector AI: spots repeated issues by unit/property

    ## Human-in-the-loop rules

    - Low confidence outputs require manual review.
    - High-risk decisions require approval.
    - AI-generated external messages are drafts unless explicitly approved by policy.
    - All AI outputs should store source references or explanation notes where possible.

    ## Prompt/data boundary

    User/customer/vendor/tenant/client input is untrusted. It must never be allowed to override system policy, reveal secrets, or trigger unauthorized actions.
