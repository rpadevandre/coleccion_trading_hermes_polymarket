# Product Architecture — Property Maintenance Triage

    ## Sector

    Property management / real estate operations

    ## Frontend views

    - Tenant maintenance request landing/form
- Photo/video upload guided intake
- Request status page
- Emergency instructions page
- Vendor-facing work order summary page

    ## Backend / motor

    The motor is the operational workflow layer. It does not try to be a generic chatbot; it converts messy inbound information into structured, reviewable, auditable work.

    - Captures tenant maintenance requests with structured prompts
- Requests missing photos/details automatically
- Classifies urgency: emergency, urgent, routine, duplicate, incomplete
- Maps issue type to vendor category and suggested next action
- Generates clean work orders and tenant response drafts

    ## Admin panel views

    - Maintenance inbox by urgency
- Request detail with tenant history and media
- Vendor routing board
- Property/unit directory
- SLA and response-time analytics
- Template/rules configuration
