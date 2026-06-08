# Product Architecture — Construction Bid Inbox Copilot

    ## Sector

    Construction / preconstruction / subcontractors

    ## Frontend views

    - Product landing for estimators
- Bid inbox problem demo
- Deadline/addenda extraction demo
- Waitlist / request a bid-inbox audit form
- ROI page: missed bid deadlines and addenda risk

    ## Backend / motor

    The motor is the operational workflow layer. It does not try to be a generic chatbot; it converts messy inbound information into structured, reviewable, auditable work.

    - Ingests forwarded bid invite emails and attachments metadata
- Extracts bid due dates, pre-bid meetings, RFI deadlines, addenda and contacts
- Classifies project fit by trade, location, deadline and scope keywords
- Creates estimator task cards and addenda alerts
- Generates proposal checklist and response drafts

    ## Admin panel views

    - Bid pipeline dashboard
- Bid invite detail with extracted deadlines
- Addenda/change alert board
- Estimator assignment view
- Project fit rules editor
- Submission calendar
