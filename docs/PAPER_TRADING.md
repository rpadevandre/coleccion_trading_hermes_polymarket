# Paper trading interno — dinero ficticio

## Objetivo

Validar si las señales del scanner de Polymarket tienen utilidad práctica antes de arriesgar capital real.

Este sistema juega internamente con dinero ficticio:

```text
cron scan → señal → posición virtual → exposición simulada → historial → evaluación futura
```

## Regla máxima

```text
No wallets.
No private keys.
No órdenes reales.
No dinero real.
```

## Por qué esto importa

El objetivo estratégico es ganar dinero rápido pero sin destruir capital. Para eso, primero necesitamos saber si el agente tiene edge o si solo está encontrando mercados populares.

Paper trading permite medir:

- cuántas señales se abren;
- cuánto capital ficticio se expone;
- si el sistema sobreopera;
- si los scores altos realmente merecen atención;
- qué mercados son basura aunque parezcan atractivos.

## Configuración inicial

El módulo usa una bankroll ficticia conservadora:

```text
bankroll: $1,000 ficticios
min_score: 80/100
max_risk_per_trade: 2% del bankroll
max_total_exposure: 20% del bankroll
```

Traducción práctica:

```text
máximo $20 ficticios por posición
máximo $200 ficticios expuestos al mismo tiempo
```

## Tablas SQLite

La base `data/hermes_polymarket.db` ahora incluye:

```text
paper_positions
```

Campos clave:

- `market_id`
- `side`
- `entry_price`
- `stake`
- `shares`
- `score`
- `status`
- `opened_at`
- `exit_price`
- `pnl`

## Integración con scanner

Manual:

```bash
.venv/bin/python scripts/scan_markets.py --limit 10 --paper
```

Cron:

```bash
scripts/cron_polymarket_scan.sh
```

El cron ya activa paper trading por defecto.

## Output en reporte

Los reportes ahora incluyen una sección:

```text
## Paper trading interno
```

Incluye:

- bankroll ficticio;
- posiciones abiertas;
- exposición abierta;
- cash ficticio disponible;
- nuevas posiciones ficticias abiertas en ese scan.

## Política actual de entrada

Una posición ficticia se abre si:

1. `recommendation == RESEARCH_CANDIDATE`
2. `score >= 80`
3. no existe posición abierta para ese mercado;
4. precio YES está entre 0.02 y 0.98;
5. hay exposición disponible según risk caps.

## Medición de performance

El repo incluye un helper para medir el estado del portfolio ficticio:

```bash
.venv/bin/python scripts/paper_performance.py
```

Output esperado:

```text
Portfolio ficticio
Performance cerrada
ROI sobre stake cerrado
Win rate
```

Para cerrar manualmente una posición ficticia cuando ya se conoce la resolución:

```bash
.venv/bin/python scripts/paper_performance.py --close-market MARKET_ID --winning-side YES
```

o:

```bash
.venv/bin/python scripts/paper_performance.py --close-market MARKET_ID --winning-side NO
```

## Auto-resolución conservadora

El repo también incluye:

```bash
.venv/bin/python scripts/update_paper_positions.py
```

Hace lo siguiente:

1. lee posiciones ficticias abiertas;
2. consulta el mercado público por `slug` en Gamma;
3. solo cierra si el mercado está `closed=true`;
4. solo infiere ganador si los precios finales son claramente binarios:
   - YES ≈ 1.0 y NO ≈ 0.0;
   - o YES ≈ 0.0 y NO ≈ 1.0;
5. calcula P&L ficticio;
6. imprime performance.

Si el resultado es ambiguo, no toca la posición.

## Limitación actual

La fase actual abre posiciones ficticias y puede cerrarlas automáticamente solo cuando la resolución pública es clara. El siguiente paso es mejorar la cobertura de mercados ambiguos/múltiples:

```text
tracking de resolución → cerrar posición virtual → calcular P&L simulado
```

## Próximo paso técnico

Crear:

```text
scripts/update_paper_positions.py
```

Para:

1. revisar posiciones abiertas;
2. detectar mercados cerrados/resueltos con formatos no binarios;
3. identificar lado ganador con más fuentes;
4. cerrar posición;
5. calcular P&L;
6. generar resumen de performance.

## Criterio para avanzar a dinero real

No avanzar a dinero real hasta tener, como mínimo:

- 30 días de señales;
- al menos 50 posiciones ficticias;
- drawdown máximo aceptable;
- ROI positivo neto simulado;
- explicación clara de por qué hubo edge;
- aprobación humana explícita.
