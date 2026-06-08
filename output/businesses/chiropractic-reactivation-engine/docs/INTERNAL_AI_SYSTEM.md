# Internal AI System — Chiropractic Patient Reactivation Engine

    ## Principle

    Internal AIs classify, summarize, draft, prioritize and explain. They do not silently take irreversible or high-risk actions.

    ## Internal AIs

    - Segmentation AI: groups inactive patients by likely reactivation path
- Message Draft AI: writes gentle rebooking messages
- Compliance Guard AI: avoids diagnosis/treatment guarantees
- Performance Insight AI: explains which segments/messages work

    ## Human-in-the-loop rules

    - Low-confidence outputs require manual review.
    - Outbound messages require approval unless explicitly configured otherwise.
    - High-risk/compliance-sensitive content stays draft-only.
    - AI outputs should preserve source references where possible.

    ## Prompt/data boundary

    Customer/user input is untrusted and cannot override system policy, reveal secrets, change permissions, or trigger unauthorized actions.
