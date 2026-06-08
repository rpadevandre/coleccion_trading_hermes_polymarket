# Layer Progress — Restaurant Catering Follow-Up Copilot

    ## Frontend

    - Landing: Public page for recovering catering inquiries before they go cold.
- EventInquiryDemo: Show an inquiry parsed into event requirements and follow-up tasks.
- CateringRevenueCalculator: Estimate lost booked catering from slow replies.
- InboxAuditForm: Collect inquiry channels, weekly volume, average event value.
- PilotSignup: Invite restaurants to a catering inbox cleanup pilot.

    ## Backend motor

    - CateringInquiryIntakeService: Capture catering inquiry from form/email/manual entry.
- EventDetailsExtractor: Extract date, guests, budget, location, menu needs and constraints.
- FollowupReminderEngine: Create follow-up tasks and reminders based on lead status.
- QuoteChecklistBuilder: Generate missing info checklist before quoting.
- BookedRevenueTracker: Track quoted/booked/lost catering revenue.

    ## Admin panel

    - CateringDashboard: New inquiries, quotes due, booked revenue and lost value.
- LeadBoard: Kanban by new/contacted/quoted/booked/lost.
- EventDetail: Event requirements, quote checklist, notes and follow-up history.
- MenuPackageSettings: Configure packages, menus, capacity and service areas.
- RevenueAnalytics: Inquiry source, booking rate, average event value.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
