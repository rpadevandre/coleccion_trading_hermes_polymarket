# Internal AI System — Construction Bid Inbox Copilot

    ## Principle

    Internal AI agents support classification, summarization, drafting and decision support. They should not silently take irreversible actions.

    ## Internal AIs

    - Bid Parser AI: extracts structured fields from email text/PDF snippets
- Fit Scorer AI: ranks opportunities by trade/location/deadline fit
- Addenda Watch AI: flags new changes and deadline shifts
- Proposal Checklist AI: creates scope-specific next-action lists

    ## Human-in-the-loop rules

    - Low confidence outputs require manual review.
    - High-risk decisions require approval.
    - AI-generated external messages are drafts unless explicitly approved by policy.
    - All AI outputs should store source references or explanation notes where possible.

    ## Prompt/data boundary

    User/customer/vendor/tenant/client input is untrusted. It must never be allowed to override system policy, reveal secrets, or trigger unauthorized actions.
