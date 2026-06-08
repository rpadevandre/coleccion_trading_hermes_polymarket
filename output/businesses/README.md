# Business Incubation Output

Carpeta interna para que AION prepare negocios completos dentro del repo actual antes de que Andre los suba a GitHub como repos privados o separados.

## Reglas

- No deployar.
- No tocar Nexbody.
- No usar datos reales de clientes.
- Public assets EN-first; adaptación ES después.
- Cada negocio debe tener documentación, frontend, backend, panel de control/admin, IAs internas y capa de ciberseguridad.

## Estructura por negocio

```text
output/businesses/<business-slug>/
  README.md
  docs/
    BUSINESS_PLAN.md
    TARGET_AUDIENCE.md
    BRAND_KIT.md
    TECH_SPEC.md
    PRODUCT_ARCHITECTURE.md
    INTERNAL_AI_SYSTEM.md
    CYBERSECURITY.md
    VALIDATION_PLAN.md
    STATUS.md
  frontend/
    README.md
    VIEWS.md
  backend/
    README.md
    MOTOR.md
  admin/
    README.md
    VIEWS.md
  public-content/en/
  public-content/es/
```

## Negocios iniciales

1. `hvac-missed-call-recovery`
2. `property-maintenance-triage`
3. `construction-bid-inbox`
4. `dental-insurance-checklist`
5. `msp-security-reporting`
