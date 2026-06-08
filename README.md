# Colección: Trading automático + Hermes Agent + Polymarket

Recopilación curada de toda la investigación reunida en esta sesión sobre bots
de trading en Python, frameworks de trading algorítmico, y la intersección
Hermes Agent + Polymarket (mercados de predicción) — pensada como insumo
directo para decidir qué construir.

Todo este contenido también vive en `outputs/summaries/` y forma parte del
índice general (`outputs/INDEX.md`); esta carpeta es solo una agrupación
temática para revisarlo de forma más cómoda.

---

## Estado actual del proyecto

Este repo ya no es solo una colección de research: ahora incluye la base de un **MVP read-only de investigación Polymarket**.

Documentos principales:

- [`PLAN_GENERAL.md`](PLAN_GENERAL.md) — plan maestro por fases.
- [`SPEC_MVP.md`](SPEC_MVP.md) — especificación del MVP read-only.
- [`ROADMAP.md`](ROADMAP.md) — roadmap de incubación técnica.
- [`docs/LECTURA_CONTEXTO_FUENTES.md`](docs/LECTURA_CONTEXTO_FUENTES.md) — lectura operativa de `repos/`, `videos/` y síntesis.
- [`docs/HERMES_CRON.md`](docs/HERMES_CRON.md) — diseño y registro del cronjob read-only de Hermes.
- [`docs/PAPER_TRADING.md`](docs/PAPER_TRADING.md) — simulación interna con dinero ficticio y risk caps.

Código inicial:

- `src/polymarket_research/` — paquete Python del agente de investigación.
- `scripts/scan_markets.py` — escaneo read-only de mercados activos.
- `scripts/cron_polymarket_scan.sh` — wrapper cron-friendly para entregar el reporte por Hermes/Telegram.
- `scripts/paper_performance.py` — medición/cierre manual de posiciones ficticias y P&L simulado.
- `src/polymarket_research/paper.py` — paper trading ficticio con bankroll y límites de riesgo.
- `tests/` — tests iniciales de modelos, scoring y SQLite WAL.

Uso local inicial:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m pytest tests -q
.venv/bin/python scripts/scan_markets.py --limit 5 --paper
```

Principio crítico:

```text
Este MVP no ejecuta trades, no toca wallets y no mueve dinero.
Solo investiga, puntúa, guarda y reporta señales.
```

---

## 🎯 Lo más relevante para tu objetivo (Hermes + Polymarket)

- **`videos/Using_the_New_Hermes_Agent_to_Track_Polymarket_Smart_Money.md`**
  — cómo usar Hermes para rastrear "smart money" en Polymarket
- **`videos/Se_LIBERÓ_Crea_un_TRADING_BOT_para_POLYMARKET_con_HERMES_Age.md`**
  — blueprint de un bot de trading para Polymarket con Hermes
- **`videos/5_Ways_I_Make_Money_With_Hermes_Agent.md`**
  — formas de monetizar con Hermes Agent
- **`videos/I_Built_an_AI_Agent_to_Find_Hidden_Polymarket_Alpha_Claude_C.md`**
  — agente para encontrar oportunidades ocultas en Polymarket
- **`videos/Polymarket_5_Min_Claude_Code_Bot_are_NUTS.md`**
  — bot rápido de Polymarket armado con Claude Code
- **`repos/DevvGwardo_polymarket-dashboard-skill.md`**
  — skill de Hermes para dashboard de Polymarket (referencia directa de cómo
  estructurar tus propios skills)
- **`repos/DFZinc_JANUS.md`** y
  **`repos/strongmandisabilitypayment539_hermes-geopolitical-market-sim.md`**
  — proyectos de simulación/agentes orientados a mercados de predicción

➡️ **Spec de síntesis que combina todo esto:**
`sintesis/20260608_agente_de_tradingpredicción_con_Hermes_y_Polymarke.md`

➡️ **Plan general accionable para construir el proyecto (pensado para que lo
ejecute un agente de IA vía `/goal`):**
[`PLAN_GENERAL.md`](PLAN_GENERAL.md) — toma la síntesis anterior y la
reordena en un MVP por fases con criterios de éxito verificables, mapa de
qué leer de esta colección para cada parte, y principios no-negociables
(human-in-the-loop, sin ejecución autónoma de trades).

---

## 🤖 Repos prácticos de trading automatizado (`repos/`)

| Repo | Por qué importa |
|---|---|
| `coding-kitties_investing-algorithm-framework` | Framework completo para construir/backtestear/desplegar algos — buena base reusable |
| `tudorelu_pyjuque` | Framework ligero para bots de cripto, foco en simplicidad |
| `TheFourGreatErrors_alpha-rptr` | Bot orientado a futuros de cripto con conexión a exchanges |
| `666ghj_MiroFish` | Motor multi-agente de "swarm intelligence" para forecasting financiero (65k★) — el que pediste agregar |
| `Fincept-Corporation_FinceptTerminal` | Alternativa open-source al Bloomberg Terminal con agentes de IA (26k★) |
| `PacktPublishing_Machine-Learning-...-Bots-with-Python` | Material educativo estructurado de ML aplicado a trading |
| `criss201x_...aprendizaje_automatico`, `TradeAIcode_BOT-DE-TRADING`, `josepobletem_cripto_trader` | Proyectos más pequeños/personales — útiles como ejemplos de implementación básica |

## 🎬 Videos — frameworks y tutoriales de trading (`videos/`)

Cubren: comparativa Freqtrade vs HummingBot vs Backtrader, introducción a
Backtrader, estrategias con indicadores técnicos (Supertrend/MACD/RSI),
overview de frameworks de algotrading, cómo desarrollar y testear estrategias
(permutation tests), tutoriales paso a paso con Python + Alpaca, y casos
reales (incluyendo uno donde alguien pone dinero real a operar con su bot, y
otro que usa IA para leer noticias y medir sentimiento de mercado).

## 🔮 Videos — Hermes Agent + Polymarket (`videos/`)

Ver sección "Lo más relevante" arriba — son los 5 videos que pediste
específicamente sobre la intersección Hermes + Polymarket.

## 📐 Síntesis (`sintesis/`)

Spec generada combinando las 10 fuentes más relevantes del índice (incluye
arquitectura dual de agentes análisis/ejecución, integración tipo skill,
smart money tracking, blueprint semi-autónomo con cron + Telegram, y patrones
de workflows multi-agente). Es el punto de partida recomendado si quieres
pasar de "investigar" a "construir" — p. ej. con
`/goal construye según outputs/synthesis/<spec>.md` desde Hermes.
