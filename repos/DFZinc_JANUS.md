# JANUS

## Información General
- **Repo:** `DFZinc/JANUS`
- **URL:** https://github.com/DFZinc/JANUS
- **Lenguaje principal:** Python
- **Stars:** 0
- **Última actualización:** 2026-04-27
- **Topics:** ninguno

## Propósito del Repo
JANUS es un sistema dual de agentes autónomos diseñado para operar en **Polymarket**, la plataforma de mercados de predicción descentralizados. El sistema implementa dos agentes diferenciados — **Hermes** y **Tyche** — que trabajan en conjunto para analizar, puntuar y ejecutar apuestas en mercados de predicción de forma automatizada.

El diseño dual sugiere una separación de responsabilidades clara: uno de los agentes probablemente se encarga de la recolección/análisis de datos e información del mercado (Hermes, mensajero), mientras el otro gestiona la estrategia de betting y gestión del riesgo (Tyche, diosa de la fortuna). Está orientado a traders algorítmicos y desarrolladores interesados en automatizar estrategias en mercados de predicción.

## Arquitectura y Patrones Clave
El sistema sigue una arquitectura de **microservicios/agentes desacoplados** con las siguientes características notables:

- **Patrón Multi-Agent**: Dos agentes independientes (`hermes_agent.py`, `tyche_agent.py`) con bases de datos propias, lo que permite que operen con estado propio y ciclos de vida independientes.
- **Base de datos por agente**: Cada agente tiene su propia base de datos SQLite (`hermes.db`, `tyche.db`), siguiendo el patrón de **Database per Service**. Los archivos `-shm` y `-wal` indican uso de SQLite en modo **WAL (Write-Ahead Logging)**, optimizado para concurrencia.
- **API REST como capa de orquestación**: `server.py` expone endpoints FastAPI que probablemente coordinan o exponen el estado de ambos agentes.
- **Cliente de mercado desacoplado**: `polymarket_client.py` abstrae la comunicación con la API de Polymarket, siguiendo el patrón **Adapter/Client**.
- **Scorer independiente**: `bettor_scorer.py` separa la lógica de puntuación/evaluación de apuestas del resto del sistema.
- **Configuración externalizada**: `polymarket_config.json` sigue el principio de configuración separada del código.

## Componentes Principales
- **`hermes_agent.py`** — Agente principal de análisis/inteligencia; probablemente consume datos de mercado y genera señales o evaluaciones.
- **`tyche_agent.py`** — Agente de ejecución de estrategia de betting; gestiona posiciones y decisiones de apuesta basándose en señales.
- **`hermes_db.py`** — Capa de acceso a datos y ORM para la base de datos de Hermes (SQLite).
- **`tyche_db.py`** — Capa de acceso a datos y ORM para la base de datos de Tyche (SQLite).
- **`polymarket_client.py`** — Cliente HTTP para interactuar con la API de Polymarket (mercados, precios, posiciones).
- **`bettor_scorer.py`** — Módulo de scoring que evalúa y puntúa oportunidades de apuesta o el rendimiento histórico.
- **`server.py`** — Servidor FastAPI que expone el sistema al exterior (API REST para control/monitoreo).
- **`polymarket_config.json`** — Configuración del sistema: credenciales, parámetros de mercado, umbrales.
- **`hermes.db` / `tyche.db`** — Bases de datos SQLite persistentes con WAL habilitado para cada agente.

## Dependencias Clave
- **`aiohttp>=3.9.0`** — Cliente HTTP asíncrono usado en `polymarket_client.py` para llamadas no bloqueantes a la API de Polymarket.
- **`fastapi>=0.110.0`** — Framework web moderno para exponer la API REST del servidor de orquestación en `server.py`.
- **`uvicorn>=0.29.0`** — Servidor ASGI de alto rendimiento para ejecutar la aplicación FastAPI de forma asíncrona.

> **Nota:** La ausencia de dependencias como `openai`, `langchain` o similares sugiere que los "agentes" son sistemas basados en reglas/algoritmos deterministas más que en LLMs, o que dichas dependencias están implícitas/no declaradas completamente.

## Fragmentos de Código Relevantes

No hay snippets disponibles en el README ni en los archivos clave provistos. La estructura del proyecto permite inferir el patrón de uso:

```python
# Patrón inferido de inicialización del sistema (server.py)
# Arranque típico FastAPI + uvicorn con agentes como background tasks
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Endpoints probables:
# GET /status         → estado de ambos agentes
# POST /hermes/run    → disparar ciclo de Hermes
# POST /tyche/bet     → ejecutar apuesta via Tyche
# GET /scores         → resultados del bettor_scorer
```

```python
# Patrón inferido del cliente Polymarket (polymarket_client.py)
import aiohttp

class PolymarketClient:
    async def get_markets(self): ...
    async def get_market_prices(self, market_id: str): ...
    async def place_order(self, market_id: str, amount: float, outcome: str): ...
```

```python
# Patrón WAL SQLite (hermes_db.py / tyche_db.py)
# SQLite con WAL habilitado para soporte de escrituras concurrentes
import sqlite3

conn = sqlite3.connect("hermes.db")
conn.execute("PRAGMA journal_mode=WAL;")
```

## Conclusiones y Aprendizajes

- **Database per Agent con SQLite WAL**: Usar WAL mode en SQLite es una decisión sólida para sistemas con múltiples lectores concurrentes y escrituras frecuentes. Patrón directamente adoptable en sistemas de agentes ligeros que no necesitan PostgreSQL.
- **Separación Scorer/Agent**: Aislar la lógica de evaluación (`bettor_scorer.py`) del agente ejecutor es una buena práctica que permite testear y ajustar estrategias sin modificar el core del agente.
- **FastAPI como bus de control**: Usar FastAPI como interfaz de orquestación entre agentes permite integrar fácilmente dashboards, webhooks o sistemas externos sin acoplar los agentes entre sí.
- **Configuración JSON externalizada**: `polymarket_config.json` permite cambiar parámetros de mercado sin redeployar, especialmente útil en sistemas de trading donde los umbrales cambian frecuentemente.
- **Arquitectura async-first**: El stack `aiohttp + FastAPI + uvicorn` es una combinación coherente para sistemas de trading que requieren baja latencia y alta concurrencia en llamadas a APIs externas.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code