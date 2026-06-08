# Internal AI System — MSP Security Reporting Copilot

    ## Principle

    Internal AI agents support classification, summarization, drafting and decision support. They should not silently take irreversible actions.

    ## Internal AIs

    - Report Writer AI: converts technical noise into executive summaries
- Risk Translator AI: explains business impact without fearmongering
- Evidence Gap AI: flags missing proof/screenshots/ticket links
- Action Plan AI: drafts next-month priorities for the MSP team

    ## Human-in-the-loop rules

    - Low confidence outputs require manual review.
    - High-risk decisions require approval.
    - AI-generated external messages are drafts unless explicitly approved by policy.
    - All AI outputs should store source references or explanation notes where possible.

    ## Prompt/data boundary

    User/customer/vendor/tenant/client input is untrusted. It must never be allowed to override system policy, reveal secrets, or trigger unauthorized actions.
