# Roadmap de incubación — Polymarket Research Agent

## Estado actual

El repo contiene una colección curada de investigación y una dirección clara para construir un agente read-only de señales Polymarket con Hermes.

## Fase 0 — Repo-first foundation

- [x] Acceso GitHub por Deploy Key.
- [x] Repo clonado en VPS Hermes.
- [x] Lectura de contexto inicial.
- [x] Documento de lectura de fuentes.
- [x] SPEC MVP read-only.
- [ ] Estructura Python mínima.
- [ ] Tests iniciales.
- [ ] Primer commit técnico.

## Fase 1 — Núcleo offline probado

- [ ] Modelos internos: `Market`, `ScoreBreakdown`, `Signal`.
- [ ] Parsing de campos double-encoded de Polymarket.
- [ ] Scorer determinista 0-100.
- [ ] SQLite con WAL.
- [ ] Tests verdes.

## Fase 2 — Cliente API read-only

- [ ] Gamma search.
- [ ] Gamma markets/trending.
- [ ] CLOB midpoint/spread/book.
- [ ] Backoff/retry.
- [ ] CLI `polymarket-research trending --limit 5`.

## Fase 3 — Reportes y señales

- [ ] Guardar mercados en DB.
- [ ] Guardar señales en DB.
- [ ] Generar reporte Markdown.
- [ ] Filtrar señales sobre umbral 65/100.

## Fase 4 — Hermes cron

- [ ] Script de escaneo cada 6h.
- [ ] Delivery Telegram.
- [ ] Resumen legible para Andre.
- [ ] Sin ejecución de trades.

## Fase 5 — Paper trading

- [ ] Registrar decisiones simuladas.
- [ ] Medir resultado después de cierre/resolución.
- [ ] Reporte semanal de P&L ficticio.
- [ ] Decidir si hay edge real.

## Fase 6 — Gate hacia dinero real

Solo considerar si paper trading muestra resultados sostenidos.

Requisitos:

- aprobación humana por operación;
- límites de riesgo;
- credenciales fuera del repo;
- auditoría de logs;
- modo kill-switch.
