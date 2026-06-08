# Internal AI System — Dental Insurance Checklist Assistant

    ## Principle

    Internal AI agents support classification, summarization, drafting and decision support. They should not silently take irreversible actions.

    ## Internal AIs

    - Checklist AI: maps payer/procedure context to verification tasks
- Patient Explanation AI: drafts plain-English benefit summaries
- Risk Flag AI: detects missing fields or denial-risk signals
- Office Notes AI: formats PMS-ready human-reviewed notes

    ## Human-in-the-loop rules

    - Low confidence outputs require manual review.
    - High-risk decisions require approval.
    - AI-generated external messages are drafts unless explicitly approved by policy.
    - All AI outputs should store source references or explanation notes where possible.

    ## Prompt/data boundary

    User/customer/vendor/tenant/client input is untrusted. It must never be allowed to override system policy, reveal secrets, or trigger unauthorized actions.
