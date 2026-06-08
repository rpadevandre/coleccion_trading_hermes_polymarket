# Product Architecture — Chiropractic Patient Reactivation Engine

    ## Frontend views

    - Landing page for patient reactivation
- Recovered appointment value calculator
- Campaign preview/demo
- Free inactive-list audit request
- Pilot signup page

    ## Backend / motor

    The motor converts messy inbound information into structured, reviewable, auditable work. It should make operators faster, not silently replace judgment.

    - Imports inactive patient CSVs/manual lists
- Segments by recency, visit type and reactivation eligibility
- Drafts safe rebooking/nurture messages for staff approval
- Tracks reply status, booked appointment and no-show outcomes
- Reports recovered revenue and campaign performance

    ## Admin panel views

    - Inactive patient segments
- Campaign builder and approval queue
- Reply tracking inbox
- Appointment recovery analytics
- Message template library
- Compliance review log
