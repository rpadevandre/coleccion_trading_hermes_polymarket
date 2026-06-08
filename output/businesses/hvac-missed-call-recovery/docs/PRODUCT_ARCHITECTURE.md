# Product Architecture — HVAC Missed-Call Recovery

    ## Sector

    Home services / HVAC

    ## Frontend views

    - Landing page with missed-call ROI promise
- ROI calculator for missed HVAC calls
- Demo call-flow walkthrough
- Free missed-call leakage audit form
- Pricing/pilot request page

    ## Backend / motor

    The motor is the operational workflow layer. It does not try to be a generic chatbot; it converts messy inbound information into structured, reviewable, auditable work.

    - Ingests missed call, voicemail, SMS or web form events
- Normalizes customer/contact/location/equipment details
- Classifies urgency using HVAC-specific rules plus optional LLM summarization
- Routes emergencies to on-call contact and non-emergencies to morning queue
- Calculates estimated recovered revenue and operational SLA metrics

    ## Admin panel views

    - Lead recovery dashboard
- Emergency lead detail with transcript and summary
- Routing rules editor
- Service area and business hours settings
- Technician/on-call contacts manager
- Recovered revenue analytics
