# Hermes cron — Polymarket Research Scan

## Propósito

Este documento registra el primer cronjob operativo recomendado para el proyecto:

```text
polymarket-research-scan
```

Su función es ejecutar un escaneo read-only de mercados públicos de Polymarket y entregar un reporte por Telegram.

## Principio de seguridad

```text
Este cronjob NO ejecuta trades.
Este cronjob NO toca wallets.
Este cronjob NO mueve dinero real.
Este cronjob solo investiga, puntúa, guarda y reporta señales.
```

## Script usado

```text
scripts/cron_polymarket_scan.sh
```

Este script:

1. entra al root del repo;
2. crea `.venv` si no existe;
3. instala dependencias del paquete si hace falta;
4. ejecuta `scripts/update_paper_positions.py` para intentar cerrar posiciones ficticias ya resueltas;
5. ejecuta `scripts/scan_markets.py`;
6. activa paper trading ficticio con risk caps;
7. genera un reporte en `outputs/reports/`;
8. imprime update + reporte completo para delivery por Hermes.

## Variables soportadas

```bash
POLYMARKET_SCAN_LIMIT=10
POLYMARKET_SIGNAL_THRESHOLD=65
```

Defaults:

```text
limit: 10 mercados
threshold: 65/100
```

## Ejecución manual

```bash
scripts/cron_polymarket_scan.sh
```

## Output esperado

El output empieza con:

```text
# Polymarket Research Scan

Repo: rpadevandre/coleccion_trading_hermes_polymarket
Modo: read-only research — no trades, no wallets, no dinero real.
Reporte generado: outputs/reports/SCAN_YYYY-MM-DD_HHMMSS_UTC.md
```

Luego incluye:

- señales sobre umbral;
- paper trading interno con dinero ficticio;
- score;
- recomendación `RESEARCH_CANDIDATE`, `WATCH` o `SKIP`;
- razonamiento explicable;
- lista de mercados revisados.

## Recomendación de scheduling

```text
cada 6 horas
```

Razonamiento:

- suficiente para detectar mercados activos;
- no demasiado agresivo para APIs públicas;
- útil para crear historial de señales;
- ideal antes de pasar a paper trading.

## Estado esperado del cronjob Hermes

```text
name: polymarket-research-scan
job_id: c8486b714789
schedule: every 6h
mode: no_agent
script wrapper: ~/.hermes/scripts/polymarket_research_scan.sh
repo script: /home/hermes/coleccion_trading_hermes_polymarket/scripts/cron_polymarket_scan.sh
deliver: origin
```

## Próxima evolución

Después de varios días de señales, el siguiente paso es crear paper trading:

```text
signal generated → virtual position → resolution tracking → simulated P&L
```

No avanzar a dinero real hasta tener evidencia de edge.
