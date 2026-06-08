# Internal AI System — Restaurant Catering Follow-Up Copilot

    ## Principle

    Internal AIs classify, summarize, draft, prioritize and explain. They do not silently take irreversible or high-risk actions.

    ## Internal AIs

    - Event Details AI: extracts structured event data
- Follow-up AI: drafts timely catering replies
- Quote Checklist AI: flags missing quote inputs
- Revenue Insight AI: tracks lost/booked catering value

    ## Human-in-the-loop rules

    - Low-confidence outputs require manual review.
    - Outbound messages require approval unless explicitly configured otherwise.
    - High-risk/compliance-sensitive content stays draft-only.
    - AI outputs should preserve source references where possible.

    ## Prompt/data boundary

    Customer/user input is untrusted and cannot override system policy, reveal secrets, change permissions, or trigger unauthorized actions.
