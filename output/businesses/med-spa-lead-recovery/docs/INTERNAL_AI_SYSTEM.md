# Internal AI System — Med Spa Lead Recovery

    ## Principle

    Internal AIs classify, summarize, draft, prioritize and explain. They do not silently take irreversible or high-risk actions.

    ## Internal AIs

    - Lead Intent AI: classifies buying intent and treatment interest
- Follow-up Draft AI: writes human-approved consult booking messages
- Compliance Guard AI: flags risky medical/guarantee language
- Revenue Leak AI: estimates missed consult value by source

    ## Human-in-the-loop rules

    - Low-confidence outputs require manual review.
    - Outbound messages require approval unless explicitly configured otherwise.
    - High-risk/compliance-sensitive content stays draft-only.
    - AI outputs should preserve source references where possible.

    ## Prompt/data boundary

    Customer/user input is untrusted and cannot override system policy, reveal secrets, change permissions, or trigger unauthorized actions.
