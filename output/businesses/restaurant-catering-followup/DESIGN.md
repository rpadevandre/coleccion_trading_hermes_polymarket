---
version: alpha
name: Restaurant Catering Follow-Up Copilot
description: restaurant revenue recovery: warm hospitality, catering follow-up, practical sales operations.
colors:
  background: "#F8FAFC"
  surface: "#FFFFFF"
  surfaceAlt: "#EEF2F7"
  primary: "#EA580C"
  secondary: "#1F2937"
  accent: "#dc2626"
  text: "#0F172A"
  muted: "#64748B"
  border: "#D8E0EA"
  success: "#16A34A"
  warning: "#F59E0B"
  danger: "#DC2626"
typography:
  h1:
    fontFamily: Inter
    fontSize: 3.5rem
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: "-0.04em"
  h2:
    fontFamily: Inter
    fontSize: 2.25rem
    fontWeight: 750
    lineHeight: 1.12
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.65
rounded:
  sm: 8px
  md: 16px
  lg: 28px
spacing:
  sm: 8px
  md: 16px
  lg: 32px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#FFFFFF"
    rounded: "{rounded.md}"
    padding: 14px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.md}"
    padding: 14px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 24px
---

## Overview

Restaurant Catering Follow-Up Copilot should feel like a credible, revenue-oriented B2B SaaS validation product. Direction: restaurant revenue recovery: warm hospitality, catering follow-up, practical sales operations.

## Colors

- **Primary (#EA580C):** main CTA and active states.
- **Secondary (#1F2937):** navigation, headings, strong structure.
- **Accent (#dc2626):** conversion highlights, urgency, badges, metrics.
- **Background (#F8FAFC):** clean SaaS page background.
- **Surface (#FFFFFF):** cards, dashboards, forms, admin panels.

## Typography

Use Inter or a close system sans. Headlines should be commercial and compact; body copy should be clear, practical, and buyer-focused.

## Layout

Frontend: header, admin-editable hero carousel, proof/features, CTA/contact/payment path, footer. Admin: sidebar/topbar, carousel editor, lead/content controls, status metrics.

## Components

Use the same tokens across frontend, admin, image prompts, and placeholder backgrounds. Do not introduce random palette choices per section.

## Do's and Don'ts

Do keep all UI and images aligned with this file. Do not ship generic placeholder visuals without `IMAGE_REQUIREMENTS.md` and `contextoparalaimagenconcepto.md`.
