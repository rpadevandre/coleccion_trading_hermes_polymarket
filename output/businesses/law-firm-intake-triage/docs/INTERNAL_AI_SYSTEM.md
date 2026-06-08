# Internal AI System — Law Firm Intake Triage

    ## Principle

    Internal AIs classify, summarize, draft, prioritize and explain. They do not silently take irreversible or high-risk actions.

    ## Internal AIs

    - Practice Area AI: categorizes inquiry type
- Intake Summary AI: structures facts into attorney-readable notes
- Risk/Compliance AI: flags legal advice risk and missing disclaimers
- Lead Quality AI: scores urgency, fit and potential value

    ## Human-in-the-loop rules

    - Low-confidence outputs require manual review.
    - Outbound messages require approval unless explicitly configured otherwise.
    - High-risk/compliance-sensitive content stays draft-only.
    - AI outputs should preserve source references where possible.

    ## Prompt/data boundary

    Customer/user input is untrusted and cannot override system policy, reveal secrets, change permissions, or trigger unauthorized actions.
