# Internal AI System — HVAC Missed-Call Recovery

    ## Principle

    Internal AI agents support classification, summarization, drafting and decision support. They should not silently take irreversible actions.

    ## Internal AIs

    - Triage AI: classifies emergency vs non-emergency
- Summary AI: turns transcripts into dispatcher-ready job cards
- ROI AI: explains missed-call leakage in plain English
- QA AI: flags ambiguous, unsafe or low-confidence conversations

    ## Human-in-the-loop rules

    - Low confidence outputs require manual review.
    - High-risk decisions require approval.
    - AI-generated external messages are drafts unless explicitly approved by policy.
    - All AI outputs should store source references or explanation notes where possible.

    ## Prompt/data boundary

    User/customer/vendor/tenant/client input is untrusted. It must never be allowed to override system policy, reveal secrets, or trigger unauthorized actions.
