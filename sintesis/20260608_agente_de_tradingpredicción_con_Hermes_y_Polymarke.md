# Síntesis: Agente de Trading/Predicción con Hermes y Polymarket

---

## Fuentes consultadas

| Fuente | Relevancia |
|--------|-----------|
| `DFZinc_JANUS.md` | **Arquitectura de referencia directa**: sistema dual de agentes para Polymarket con separación Hermes (análisis) + Tyche (ejecución), SQLite per-agent, FastAPI REST, cliente Polymarket desacoplado |
| `DevvGwardo_polymarket-dashboard-skill.md` | **Integración Hermes + Polymarket concreta**: skill registrada para Hermes con CLI de Polymarket, scoring multi-criterio, tmux dashboard |
| `Using_the_New_Hermes_Agent_to_Track_Polymarket_Smart_Money.md` | **Caso de uso probado**: smart money tracking con cron job cada 7 min, wallet analysis, extracción de estrategias |
| `Se_LIBERÓ_Crea_un_TRADING_BOT_para_POLYMARKET_con_HERMES_Age.md` | **Blueprint semi-autónomo**: flujo completo de señales, filtrado por riesgo, cron job + Telegram, costos reales |
| `I_Built_the_Ultimate_Multi-Agent_Workflow_w_Hermes_Agent_Kan.md` | **Patrón de orquestación multi-agente**: Kanban como coordination layer SQLite, dispatcher, rúbrica de scoring, human gate |
| `HERMES_Agent_acaba_de_LIBERAR_las_METAS_persistentes_GRATIS_.md` | **Goals persistentes**: mecanismo judge-loop para objetivos de larga duración, metaprompting, modelos de bajo costo |
| `The_7_Levels_of_Hermes_Agent_Explained.md` | **Infraestructura avanzada**: VPS setup, servidor MCP, memoria holográfica, gestión de skills con Curator |
| `El_Mejor_Agente_Open_Source_Actual_Hermes_Agent.md` | **Setup completo**: instalación VPS, cron jobs, perfiles, PM2, Tailscale |
| `Cut_Your_AI_API_Bill_by_93_with_Hermes_Agent_Claude_Gemini_O.md` | **Optimización de costos**: credential pooling OAuth, 93% reducción, estrategias de rotación |
| `Hermes_Kanban_Swarm_es_BRUTAL_Tutorial_Completo.md` | **Coordinación avanzada**: dispatcher, heartbeat, reclaim, workspaces, dependencias entre tareas |

---

## Patrones que se repiten en múltiples fuentes

### 1. Separación análisis / ejecución (3+ fuentes)
- `JANUS.md`: Hermes (análisis) + Tyche (ejecución), cada uno con DB propia
- `Se_LIBERÓ.md`: agente de investigación primero, segundo agente ejecutor como mejora planificada
- `Smart_Money.md`: análisis de wallets → señales → paper trading antes de producción

**Conclusión**: La arquitectura correcta es de dos fases separadas con un human gate entre ellas.

### 2. SQLite como fuente de verdad compartida (3 fuentes)
- `JANUS.md`: `hermes.db` + `tyche.db` con WAL mode
- `I_Built_Multi-Agent.md`: Kanban como SQLite único, bus de mensajes + audit log
- `Hermes_Kanban_Swarm.md`: 5 tablas (`tasks`, `task_links`, `comments`, `task_events`, `task_runs`)

**Conclusión**: SQLite con WAL es el persistence layer estándar para coordinación de agentes.

### 3. Cron job + Telegram como delivery (3 fuentes)
- `Smart_Money.md`: cron cada 7 minutos, actualizaciones por terminal
- `Se_LIBERÓ.md`: cron cada 6 horas, señales por Telegram
- `El_Mejor_Agente.md`: cron jobs conversacionales configurados en lenguaje natural

**Conclusión**: Cron + Telegram es el stack probado para notificación no-bloqueante de señales.

### 4. Scorer/rúbrica como filtro de calidad (3 fuentes)
- `JANUS.md`: `bettor_scorer.py` con scoring independiente de la lógica de ejecución
- `DevvGwardo.md`: Opportunity Score = f(Risk/Reward, Conviction Score, Volume Score)
- `I_Built_Multi-Agent.md`: rúbrica de 5 dimensiones, umbral 65/100 para avanzar

**Conclusión**: El scoring compuesto multi-criterio con umbral explícito es el patrón dominante para filtrado.

### 5. VPS + Hostinger + Tailscale (3 fuentes)
- `Se_LIBERÓ.md`, `El_Mejor_Agente.md`, `HERMES_Goals.md`: misma recomendación de infraestructura

**Conclusión**: Stack de deployment probado y repetido.

### 6. Human-in-the-loop como gate obligatorio antes de ejecución real (3 fuentes)
- `I_Built_Multi-Agent.md`: único gate vía Telegram antes del Builder
- `Se_LIBERÓ.md`: el agente no abre posiciones solo
- `Smart_Money.md`: backtesting/paper trading antes de producción

**Conclusión**: La autonomía total en ejecución es un anti-patrón; el human gate es un requisito de diseño.

### 7. Polymarket API pública (CLOB + Gamma) (2 fuentes)
- `DevvGwardo.md`: endpoints documentados en `references/api-endpoints.md`, `search`, `trending`, `analyze`, orderbook, trades
- `JANUS.md`: `polymarket_client.py` como adaptador, `polymarket_config.json`

---

## Arquitectura recomendada

```
┌─────────────────────────────────────────────────────────────┐
│                    HERMES AGENT VPS                          │
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │  CRON JOB    │───▶│  ANÁLISIS    │───▶│   SCORER     │  │
│  │  (6h/7min)   │    │  AGENT       │    │  (multi-     │  │
│  └──────────────┘    │  (Hermes)    │    │  criterio)   │  │
│                      └──────┬───────┘    └──────┬───────┘  │
│                             │                    │           │
│                      ┌──────▼───────┐    ┌──────▼───────┐  │
│                      │  hermes.db   │    │  FILTRADO     │  │
│                      │  (SQLite WAL)│    │  (threshold)  │  │
│                      └─────────────┘    └──────┬───────┘  │
│                                                  │           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────▼───────┐  │
│  │  EXECUTION   │◀───│  HUMAN GATE  │◀───│  TELEGRAM    │  │
│  │  AGENT       │    │  (approve/   │    │  NOTIFIER    │  │
│  │  (Tyche)     │    │  reject)     │    │              │  │
│  └──────┬───────┘    └─────────────┘    └─────────────┘  │
│         │                                                    │
│  ┌──────▼───────┐    ┌──────────────┐                      │
│  │  tyche.db    │    │ POLYMARKET   │                      │
│  │  (SQLite WAL)│    │ CLIENT       │                      │
│  └─────────────┘    │ (CLOB API)   │                      │
│                      └──────────────┘                      │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              FastAPI REST (server.py)                  │  │
│  │     /status  /signals  /positions  /approve            │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Decisiones de arquitectura justificadas

**1. Agente de análisis separado del agente de ejecución**
Fuente: `JANUS.md` (patrón Hermes/Tyche), `Se_LIBERÓ.md` (recomendación explícita de segundo agente). Permite pausar/modificar la lógica de ejecución sin tocar el análisis.

**2. Polymarket como Skill registrada en Hermes (no integración directa)**
Fuente: `DevvGwardo.md` (SKILL.md + estructura skill-first). El CLI de Polymarket (`polymarket.py`) se registra como skill, lo que permite que el agente lo invoque con lenguaje natural y Hermes Curator gestione su ciclo de vida.

**3. Kanban Board como coordination layer para flujos complejos**
Fuente: `I_Built_Multi-Agent.md`, `Hermes_Kanban_Swarm.md`. Para pipelines con múltiples pasos (scan → analyze → score → notify → approve → execute), el Kanban SQLite evita condiciones de carrera y provee audit log gratuito.

**4. Goals (/goal) para análisis de larga duración vs Cron para polling**
Fuente: `HERMES_Goals.md`. Los Goals son adecuados para investigación profunda de un mercado específico (puede correr 155+ horas). Los Cron Jobs son adecuados para el polling periódico del leaderboard/trending.

**5. FastAPI REST como capa de orquestación y control**
Fuente: `JANUS.md` (server.py). Permite integración externa, webhooks de Telegram, y endpoint `/approve` para el human gate.

**6. Memoria holográfica para contexto de mercados históricos**
Fuente: `The_7_Levels.md` (nivel 6). Almacena hechos estructurados sobre mercados, traders y estrategias sin enviar datos a la nube, esencial para el knowledge graph mencionado en `Se_LIBERÓ.md`.

---

## Stack sugerido

### Core
| Componente | Tecnología | Justificación |
|-----------|-----------|---------------|
| Framework agéntico | **Hermes Agent** (latest) | Fuente de todas las investigaciones; skills nativas, Kanban, Goals, cron jobs |
| LLM principal | **Claude Sonnet 3.7** | `Smart_Money.md`: Sonnet recomendado sobre Opus por rate limiting; `The_7_Levels.md`: modelos potentes son críticos |
| LLM económico (análisis masivo) | **Kimi 2.6 / Minimax** | `HERMES_Goals.md`: ventanas de tokens superiores a Claude/GPT para tareas largas a menor costo |
| Persistence | **SQLite + WAL mode** | `JANUS.md`, `I_Built_Multi-Agent.md`, `Hermes_Kanban_Swarm.md`: patrón repetido en 3 fuentes |
| API Gateway | **Open Router** | `The_7_Levels.md`: permite acceso a múltiples modelos con una sola key |

### Infraestructura
| Componente | Tecnología | Justificación |
|-----------|-----------|---------------|
| Servidor | **VPS Hostinger KVM2** (2 CPU, 8GB RAM) | `El_Mejor_Agente.md`, `Se_LIBERÓ.md`, `HERMES_Goals.md`: recomendación consistente en 3 fuentes |
| Acceso seguro | **Tailscale** | `Se_LIBERÓ.md`, `El_Mejor_Agente.md`: VPN para no exponer dashboard públicamente |
| Proceso persistente | **PM2** | `El_Mejor_Agente.md`: mantiene dashboard activo ante reinicios |
| Notificaciones | **Telegram Bot** | `Se_LIBERÓ.md`, `El_Mejor_Agente.md`, `I_Built_Multi-Agent.md`: canal estándar para human gate |

### Backend del trading bot
| Componente | Tecnología | Justificación |
|-----------|-----------|---------------|
| API server | **FastAPI** | `JANUS.md`: patrón establecido; `DevvGwardo.md`: control/monitoreo |
| ASGI server | **Uvicorn** | `JANUS.md`: dependencia declarada |
| HTTP cliente | **aiohttp** | `JANUS.md`: cliente asíncrono para Polymarket API |
| Polymarket API | **CLOB API + Gamma API** | `DevvGwardo.md`: endpoints documentados |
| Dashboard | **tmux multi-panel** | `DevvGwardo.md`: patrón probado con auto-refresh por panel |

### Reducción de costos (opcional)
| Componente | Tecnología | Justificación |
|-----------|-----------|---------------|
| Proxy OAuth | **Hermes local proxy** `localhost:4000` | `Cut_93_percent.md`: 93% reducción usando suscripciones en lugar de API keys |
| Modelos gratuitos | **Qwen3-235B via Alibaba** | `Cut_93_percent.md`: tier gratuito para análisis secundarios |

---

## Riesgos y anti-patrones identificados

### 1. ❌ Agente con ejecución totalmente autónoma
**Fuente**: `Se_LIBERÓ.md` ("el agente no abre posiciones por sí solo"), `I_Built_Multi-Agent.md` (human gate explícito), `Smart_Money.md` (paper trading primero).
**Riesgo**: pérdida financiera irreversible. **Mitigación**: siempre implementar `kanban_block` + Telegram approval antes de cualquier transacción on-chain.

### 2. ❌ Usar modelos pequeños/baratos para el agente orquestador
**Fuente**: `The_7_Levels.md` ("Los modelos pequeños y baratos degradan severamente la calidad en harnesses agénticos complejos").
**Riesgo**: decisiones de trading incorrectas por razonamiento pobre. **Mitigación**: Claude Sonnet o superior para el agente de análisis principal; modelos económicos solo para tareas de scraping/formatting.

### 3. ❌ Context rot por acumulación de skills sin uso
**Fuente**: `The_7_Levels.md` (Hermes Curator: skills marcadas stale a 30 días, eliminadas a 90 días).
**Riesgo**: consumo excesivo de tokens y degradación de calidad. **Mitigación**: activar Hermes Curator desde el inicio.

### 4. ❌ Exponer credenciales de wallet/API en el equipo local
**Fuente**: `Se_LIBERÓ.md` ("VPS en lugar de máquina local para evitar riesgos de seguridad con credenciales y cuentas bancarias").
**Riesgo**: compromiso de private keys. **Mitigación**: `.env` solo en VPS, Tailscale para acceso, nunca en repositorio.

### 5. ❌ Polling sin rate limiting contra la API de Polymarket
**Fuente**: `Smart_Money.md` (error 529 por rate limiting con Opus), `Cut_93_percent.md` (429 → retry + rotación).
**Riesgo**: ban de IP o degradación del servicio. **Mitigación**: exponential backoff, respetar headers de rate limit, cooldown de 24h en 402.

### 6. ❌ Comunicación directa entre agentes (sin coordination layer)
**Fuente**: `I_Built_Multi-Agent.md` ("Sin el Kanban: los agentes hacen trabajo duplicado, desperdician tokens y no tienen memoria compartida").
**Riesgo**: condiciones de carrera, trabajo duplicado, pérdida de estado. **Mitigación**: toda comunicación a través del Kanban SQLite.

### 7. ❌ Uso de OAuth de suscripción para producción financiera
**Fuente**: `Cut_93_percent.md` ("uso de credenciales OAuth de suscripción en apps de terceros puede estar fuera de los términos de servicio").
**Riesgo**: bloqueo de cuentas en momento crítico. **Mitigación**: usar API keys pagadas para el agente de ejecución de trades; OAuth solo para análisis.

### 8. ❌ Workspace temporal para artefactos persistentes
**Fuente**: `I_Built_Multi-Agent.md` (auto-healing: workspace temporal ya eliminado → regenerar en directorio persistente).
**Riesgo**: pérdida de señales o logs de trading. **Mitigación**: usar worktrees o directorios persistentes para todos los outputs del sistema.

---

## Spec de implementación

### Fase 0: Infraestructura base (Día 1-2)

**0.1 Provisionar VPS**
```bash
# Hostinger KVM2: 2 CPU, 8GB RAM, Ubuntu 22.04 LTS
# Crear usuario no-root ANTES de instalar Hermes
adduser hermesbot
usermod -aG sudo hermesbot
su - hermesbot
```
*Fuente*: `El_Mejor_Agente.md` (usuario no-root requerido)

**0.2 Instalar Hermes Agent**
```bash
# One-liner oficial
curl -sSL https://get.hermes.sh | bash

# Quick Setup interactivo:
# - Provider: Open Router (acceso multi-modelo)
# - Messaging: Telegram
# - Guardar API keys en .env (nunca en repositorio)
```

**0.3 Configurar Tailscale + PM2**
```bash
# Tailscale para acceso seguro
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up

# PM2 para dashboard persistente
npm install -g pm2
pm2 start hermes-dashboard --name hermes
pm2 save && pm2 startup
```
*Fuente*: `El_Mejor_Agente.md`, `Se_LIBERÓ.md`

**0.4 Activar Hermes Curator**
Hablarle al agente:
> "Install and configure Hermes Curator to mark unused skills as stale after 30 days and delete after 90 days"

*Fuente*: `The_7_Levels.md` (Nivel 3)

**0.5 Configurar memoria holográfica**
```bash
hermes memory setup
# Almacena hechos estructurados sobre mercados y traders en SQLite local
```
*Fuente*: `The_7_Levels.md` (Nivel 6)

---

### Fase 1: Polymarket Skill (Día 2-3)

**1.1 Crear estructura del skill**
```
skills/polymarket/
├── SKILL.md           # Descriptor para Hermes
├── polymarket.py      # CLI unificado
├── polymarket_client.py  # Adaptador API (aiohttp async)
├── polymarket_config.json  # Endpoints, umbrales
└── references/
    └── api-endpoints.md
```
*Fuente*: `DevvGwardo.md` (estructura exacta del repo)

**1.2 Implementar `polymarket_client.py`**
```python
# Endpoints a cubrir (Fuente: DevvGwardo.md - api-endpoints.md)
# CLOB API: https://clob.polymarket.com
#   - GET /markets (trending, search)
#   - GET /markets/{condition_id}/orderbook
#   - GET /trades (recent trades)
#
# Gamma API: https://gamma-api.polymarket.com
#   - GET /markets?active=true&closed=false
#   - GET /events (categorías)
#
# Subcomandos CLI:
#   polymarket.py search <query>
#   polymarket.py trending [--limit 20]
#   polymarket.py analyze <market_id>
#   polymarket.py orderbook <market_id>
#   polymarket.py leaderboard [--limit 50]
#   polymarket.py wallet <address>

import aiohttp
import asyncio

class PolymarketClient:
    CLOB_BASE = "https://clob.polymarket.com"
    GAMMA_BASE = "https://gamma-api.polymarket.com"
    
    async def get_trending(self, limit=20):
        """Top markets by volume - Fuente: DevvGwardo.md"""
        ...
    
    async def get_leaderboard(self, limit=50):
        """Profitable traders - Fuente: Smart_Money.md"""
        ...
    
    async def get_wallet_history(self, address: str):
        """Wallet trade history - Fuente: Smart_Money.md"""
        ...
```

**1.3 Implementar `bettor_scorer.py`**
```python
# Scoring multi-criterio (Fuente: DevvGwardo.md + I_Built_Multi-Agent.md)
# Dimensiones del score:
#   1. Risk/Reward ratio (0-25 pts)
#   2. Volume Score - liquidez (0-20 pts)  
#   3. Conviction Score - probabilidad implied vs estimada (0-20 pts)
#   4. Expected Value (0-20 pts)
#   5. Source reliability (0-15 pts)
# UMBRAL: >= 65/100 para generar señal
# Filtros de exclusión (Fuente: Se_LIBERÓ.md):
#   - liquidez < threshold → descartar
#   - fuente poco confiable → descartar
#   - mercado ambiguo → descartar

def calculate_opportunity_score(market_data: dict) -> dict:
    scores = {
        "risk_reward": _score_risk_reward(market_data),
        "volume": _score_volume(market_data),
        "conviction": _score_conviction(market_data),
        "expected_value": _score_ev(market_data),
        "source_reliability": _score_source(market_data),
    }
    total = sum(scores.values())
    return {
        "total": total,
        "breakdown": scores,
        "recommendation": "BUY" if total >= 65 else "SKIP",
        "market_id": market_data["conditionId"]
    }
```

**1.4 Registrar SKILL.md**
```markdown
# Polymarket Trading Intelligence Skill

## Capabilities
- Scan trending prediction markets by volume
- Analyze orderbook depth and liquidity
- Extract profitable wallet strategies from leaderboard
- Score opportunities with multi-criteria rubric (threshold: 65/100)
- Generate trading signals (NOT execute trades)

## Commands
- `polymarket trending` — Top 20 markets by volume
- `polymarket analyze <id>` — Deep analysis of specific market
- `polymarket leaderboard` — Top profitable traders
- `polymarket wallet <addr>` — Strategy extraction from wallet history
- `polymarket scan` — Full opportunity scan with scoring

## Usage
This skill provides RESEARCH and SIGNALS only.
Trade execution requires separate human approval gate.
```

---

### Fase 2: Base de datos y persistencia (Día 3-4)

**2.1 Schema SQLite con WAL mode**
```sql
-- hermes_trading.db (Fuente: JANUS.md - patrón hermes.db)
PRAGMA journal_mode=WAL;

CREATE TABLE markets (
    id TEXT PRIMARY KEY,
    condition_id TEXT UNIQUE,
    title TEXT,
    category TEXT,
    yes_price REAL,
    no_price REAL,
    volume_24h REAL,
    liquidity REAL,
    close_time INTEGER,
    last_updated INTEGER,
    created_at INTEGER DEFAULT (strftime('%s','now'))
);

CREATE TABLE signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    market_id TEXT REFERENCES markets(id),
    signal_type TEXT CHECK(signal_type IN ('YES', 'NO', 'SKIP')),
    score REAL,
    score_breakdown JSON,
    reasoning TEXT,  -- LLM explanation
    status TEXT DEFAULT 'pending' CHECK(status IN ('pending','approved','rejected','executed','expired')),
    created_at INTEGER DEFAULT (strftime('%s','now')),
    approved_at INTEGER,
    executed_at INTEGER
);

CREATE TABLE wallet_profiles (
    address TEXT PRIMARY KEY,
    total_profit REAL,
    monthly_profit REAL,
    win_rate REAL,
    strategy_summary TEXT,  -- LLM-extracted strategy
    last_analyzed INTEGER,
    created_at INTEGER DEFAULT (strftime('%s','now'))
);

CREATE TABLE executions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    signal_id INTEGER REFERENCES signals(id),
    amount REAL,
    outcome TEXT,
    pnl REAL,
    tx_hash TEXT,
    created_at INTEGER DEFAULT (strftime('%s','now'))
);

-- Kanban tasks table (Fuente: Hermes_Kanban_Swarm.md)
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    assigned_to TEXT,  -- agent profile name
    status TEXT DEFAULT 'triage' CHECK(status IN ('triage','todo','ready','in_progress','done','blocked','archived')),
    parent_id INTEGER REFERENCES tasks(id),
    workspace TEXT,
    retry_count INTEGER DEFAULT 0,
    last_heartbeat INTEGER,
    created_at INTEGER DEFAULT (strftime('%s','now')),
    updated_at INTEGER DEFAULT (strftime('%s','now'))
);
```

**2.2 Capa de acceso a datos**
```python
# db.py
import sqlite3
from contextlib import contextmanager

DB_PATH = "/home/hermesbot/hermes_trading.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
```

---

### Fase 3: Agente de análisis (Día 4-6)

**3.1 Crear perfil Hermes: "Polymarket Analyst"**

En el dashboard de Hermes, crear perfil con:
```
Name: polymarket-analyst
Model: claude-sonnet-3.7 (via Open Router)
System Prompt:
  You are a prediction market analyst specialized in Polymarket.
  Your job is to scan markets, extract profitable trading strategies
  from top wallets, and generate scored signals.
  
  You NEVER execute trades. You generate signals for human review.
  
  For each market analyzed:
  1. Assess implied probability vs your estimated probability
  2. Check liquidity and volume (minimum thresholds in config)
  3. Extract any smart money positioning from leaderboard
  4. Calculate opportunity score using bettor_scorer
  5. Write clear reasoning for the signal
  
  Output format: structured JSON compatible with signals table schema.
Skills: polymarket (required), web_search (optional), memory (required)
Workspace: /home/hermesbot/workspaces/analyst (persistent dir)
```
*Fuente*: `I_Built_Multi-Agent.md` (cada agente es un perfil con modelo propio), `JANUS.md` (hermes_agent.py separado)

**3.2 Crear Goal para análisis profundo de mercado**

Metaprompt previo (Fuente: `HERMES_Goals.md`):
> "Generate an optimized Goal for deep-analyzing a specific Polymarket prediction market. The goal should: research recent news, check smart money positioning, calculate expected value, compare to market implied probability, and produce a structured trading signal. Use polymarket skill and web_search. Include judge criteria: signal must have reasoning of >200 words, EV calculation shown, and score >= 65."

Goal resultante se guarda como template reutilizable.

**3.3 Configurar cron job de análisis**

Hablarle al agente:
> "Create a cron job that runs every 6 hours: 1) scan trending markets using polymarket skill, 2) score top 20 with bettor_scorer, 3) for signals scoring >= 65, run deep analysis Goal, 4) save results to hermes_trading.db signals table, 5) send summary to Telegram with pending approval buttons"

*Fuente*: `Se_LIBERÓ.md` (cada 6 horas, Telegram), `Smart_Money.md` (cada 7 min para leaderboard)

---

### Fase 4: Smart money tracking (Día 5-6)

**4.1 Cron job separado para wallet tracking**
```python
# wallet_tracker.py - runs every 7 minutes (Fuente: Smart_Money.md)
async def track_smart_money():
    async with PolymarketClient() as client:
        leaderboard = await client.get_leaderboard(limit=20)
        
        for trader in leaderboard:
            # Check if already analyzed recently
            with get_db() as db:
                existing = db.execute(
                    "SELECT last_analyzed FROM wallet_profiles WHERE address = ?",
                    (trader['address'],)
                ).fetchone()
                
                if existing and (time.time() - existing['last_analyzed']) < 3600:
                    continue
            
            # LLM strategy extraction (Fuente: Smart_Money.md)
            history = await client.get_wallet_history(trader['address'])
            strategy = await extract_strategy_with_llm(history, trader)
            
            with get_db() as db:
                db.execute("""
                    INSERT OR REPLACE INTO wallet_profiles 
                    (address, total_profit, monthly_profit, win_rate, 
                     strategy_summary, last_analyzed)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (trader['address'], trader['totalProfit'],
                      trader['monthlyProfit'], trader['winRate'],
                      strategy, int(time.time())))
```

**4.2 Strategy extraction prompt**
```python
STRATEGY_EXTRACTION_PROMPT = """
Analyze this trader's history on Polymarket and extract their trading strategy.

Trader stats: {stats}
Recent trades: {trades}

Identify:
1. What categories/topics they trade (politics, sports, crypto, etc.)
2. Their entry timing pattern (early, late, contrarian)
3. Any indicators they seem to use (news events, price levels like SPX overnight - Fuente: Smart_Money.md)
4. Position sizing pattern
5. Exit strategy (hold to resolution or trade out)

Output: 2-3 sentence strategy summary suitable for copy-trading analysis.
"""
```

---

### Fase 5: Human gate + FastAPI server (Día 6-8)

**5.1 Implementar `server.py`**
```python
# server.py (Fuente: JANUS.md - FastAPI pattern)
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="Polymarket Trading Bot API")

@app.get("/signals")
async def get_pending_signals():
    """Returns signals awaiting approval"""
    with get_db() as db:
        signals = db.execute(
            "SELECT * FROM signals WHERE