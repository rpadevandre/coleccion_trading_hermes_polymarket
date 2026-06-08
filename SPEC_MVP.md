# SPEC MVP — Agente read-only de investigación Polymarket con Hermes

## Decisión base

Este MVP no es un bot de trading autónomo. Es un **sistema read-only de investigación y scoring** para encontrar señales potenciales en Polymarket, guardarlas y notificarlas a Andre para evaluación manual.

```text
buscar mercados → normalizar datos → puntuar oportunidad → guardar señal → reportar → Andre decide
```

## Objetivo de negocio

Construir una base técnica segura para acercarse a ingresos reales en mercados de predicción sin saltarse validación:

1. Investigación y señales.
2. Paper trading.
3. Dinero real solo con aprobación humana explícita.

## No negociables

1. No ejecución autónoma de trades.
2. No credenciales reales en GitHub.
3. SQLite persistente con WAL.
4. Backoff/rate limiting desde el primer cliente API.
5. Scoring explicable, no caja negra.
6. Tests desde el inicio.
7. Output por Telegram/Hermes, no dashboard complejo al principio.

## Arquitectura MVP

```text
scripts/scan_markets.py
        ↓
src/polymarket_research/client.py        # Gamma/CLOB/Data API read-only
        ↓
src/polymarket_research/scorer.py        # opportunity score 0-100
        ↓
src/polymarket_research/db.py            # SQLite + WAL
        ↓
outputs/reports/*.md                     # reportes y señales para Andre
```

## Componentes

### 1. Cliente Polymarket read-only

Responsabilidad:

- listar mercados activos/trending;
- buscar mercados por query;
- obtener orderbook/midpoint/spread;
- normalizar campos double-encoded como `outcomes`, `outcomePrices`, `clobTokenIds`.

Endpoints base:

- Gamma: `https://gamma-api.polymarket.com`
- CLOB: `https://clob.polymarket.com`
- Data: `https://data-api.polymarket.com`

### 2. Modelos internos

Responsabilidad:

- representar mercado normalizado;
- representar desglose de score;
- representar señal generada.

### 3. Scorer

Dimensiones iniciales:

- liquidity/volume;
- spread/risk;
- price sanity;
- market activity;
- source reliability.

Umbral inicial:

```text
65/100 = WATCH o RESEARCH_CANDIDATE
```

En MVP read-only, `RESEARCH_CANDIDATE` significa “investigar/aprobar manualmente”, no ejecutar.

### 4. SQLite

Tablas mínimas:

- `markets`
- `signals`
- `wallet_profiles` — reservada para smart-money tracking futuro.

### 5. Reportes

Formato:

```text
outputs/reports/SCAN_YYYY-MM-DD_HHMM.md
```

Debe incluir:

- top mercados revisados;
- señales sobre umbral;
- razonamiento;
- riesgos;
- qué datos faltan;
- recomendación manual.

## Fases de implementación

### Fase 1 — Esqueleto probado

- paquete Python;
- tests de parsing;
- tests de scorer;
- tests de SQLite WAL;
- `.env.example`;
- scripts básicos.

### Fase 2 — Cliente real Gamma/CLOB

- `search`;
- `trending`;
- `market details`;
- retry/backoff;
- CLI simple.

### Fase 3 — Persistencia + reportes

- guardar mercados;
- guardar señales;
- generar Markdown report.

### Fase 4 — Cron Hermes

- script `scan_polymarket.sh`;
- cron cada 6h;
- entrega a Telegram;
- no-agent o agent según output deseado.

### Fase 5 — Paper trading

- registrar señales simuladas;
- medir P&L ficticio;
- decidir si hay edge.

## Criterio de éxito del MVP inicial

El MVP inicial se considera listo cuando:

```text
python scripts/scan_markets.py --limit 5
```

produce un reporte Markdown con datos reales de Polymarket, guarda señales en SQLite WAL y todos los tests pasan.

## Riesgo principal

El mayor riesgo no es técnico: es confundir “señales interesantes” con “edge real”. Por eso la etapa de paper trading es obligatoria antes de dinero real.
