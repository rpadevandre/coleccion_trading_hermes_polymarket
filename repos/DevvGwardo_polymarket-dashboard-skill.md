# Polymarket Dashboard Skill

## Información General
- **Repo:** `DevvGwardo/polymarket-dashboard-skill`
- **URL:** https://github.com/DevvGwardo/polymarket-dashboard-skill
- **Lenguaje principal:** Python
- **Stars:** 0
- **Última actualización:** 2026-04-11
- **Topics:** analytics, cli, dashboard, hermes-agent, polymarket, prediction-markets, python, terminal, tmux, trading

## Propósito del Repo
Este repositorio implementa un dashboard terminal completo para monitorear mercados de predicción de Polymarket en tiempo real, diseñado específicamente como una "skill" para el agente de IA **Hermes**. Resuelve el problema de tener visibilidad consolidada sobre mercados de predicción: feeds en vivo, análisis estadístico y detección automatizada de oportunidades de beneficio, todo desde la terminal.

Está orientado a traders/analistas que operan con Polymarket y quieren integrar inteligencia de mercado en un flujo de trabajo basado en agentes de IA. Su diferencial es la arquitectura modular orientada a skills de agente: cada componente (live feed, stats, profit analyzer) puede correr independientemente o combinado en un panel tmux orquestado.

## Arquitectura y Patrones Clave

El sistema sigue un patrón **multi-panel con orquestación tmux**: un script central (`launch-dashboard.sh`) crea una sesión tmux con múltiples paneles, cada uno ejecutando un script especializado con auto-refresh. Los componentes son:

- **Polling periódico**: cada panel tiene su propio ciclo de refresco (30s, 60s, 5min).
- **CLI como capa de abstracción**: `polymarket.py` actúa como cliente CLI unificado que encapsula llamadas a la API de Polymarket, exponiendo subcomandos (`search`, `trending`, `analyze`, etc.).
- **Skill-first design**: la estructura de directorios y el archivo `SKILL.md` indican que este repo está diseñado para ser consumido por el agente Hermes como una capability registrada.
- **Análisis por scoring compuesto**: el profit analyzer calcula métricas individuales (Risk/Reward, Conviction Score, Volume Score) y las combina en un Opportunity Score, patrón clásico de scoring multi-criterio.

## Componentes Principales

- **`scripts/polymarket.py`** — Cliente CLI principal; encapsula las llamadas a la API de Polymarket con subcomandos para búsqueda, trending, historial de precios, orderbook, trades y análisis de oportunidades.
- **`scripts/launch-dashboard.sh`** — Orquestador tmux; crea la sesión completa del dashboard con múltiples paneles y gestiona el layout.
- **`scripts/live-feed.sh`** — Panel de feed en vivo; muestra mercados trending por volumen y trades recientes, con refresh cada 30s.
- **`scripts/stats-analysis.sh`** — Panel de análisis estadístico; realiza deep dives en mercados tracked, incluye gráficos ASCII de historial de precios y análisis de orderbook, refresh cada 60s.
- **`scripts/profit-analyzer.sh`** — Panel de detección de oportunidades; escanea los top 20 mercados, calcula métricas de riesgo/recompensa y expected value, refresh cada 5 min.
- **`scripts/setup.sh`** — Instalador; configura dependencias, rutas y registra el comando `polymarket-dashboard` en el sistema.
- **`references/api-endpoints.md`** — Documentación de referencia de los endpoints de la API de Polymarket usados.
- **`SKILL.md`** — Descriptor de la skill para el agente Hermes; define capacidades, comandos y contexto de uso.

## Dependencias Clave

- **Python 3.6+** — Lenguaje base del CLI; sin dependencias pesadas inferidas, compatible con entornos minimalistas.
- **tmux** — Motor de multiplexación de terminal para el dashboard multi-panel; requisito de sistema.
- **Polymarket API (CLOB/Gamma)** — API pública de Polymarket para datos de mercados, orderbook, trades e historial de precios.
- **bash** — Scripts de orquestación y paneles individuales implementados en shell.

*(El repo aparenta ser deliberadamente ligero en dependencias Python para facilitar su uso como skill embebida en un agente.)*

## Fragmentos de Código Relevantes

**1. CLI unificado con subcomandos (uso típico):**
```bash
# Buscar mercados
polymarket search "bitcoin"

# Analizar oportunidades de profit en top 20 mercados
polymarket analyze --limit 20

# Obtener historial de precios con intervalo y fidelidad
polymarket history "0xabc123..." --interval 1w --fidelity 50
```

**2. Métricas de scoring del Profit Analyzer:**
```
- Risk/Reward Ratio:  Profit potencial vs. costo de entrada
- Conviction Score:   Qué tan "mispriced" parece el mercado (-5 a +5)
- Volume Score:       Liquidez y facilidad de trading (0 a 5)
- Opportunity Score:  Métrica combinada de ranking (0 a 15+)
- Expected Value:     Edge matemático por cada $100 invertidos
```

**3. Lanzamiento del dashboard completo:**
```bash
# One-liner: clonar, instalar y lanzar
git clone https://github.com/yourusername/polymarket-dashboard-skill.git
cd polymarket-dashboard-skill
./scripts/setup.sh
polymarket-dashboard

# Componentes individuales
~/.hermes/skills/research/polymarket-dashboard/scripts/live-feed.sh
~/.hermes/skills/research/polymarket-dashboard/scripts/profit-analyzer.sh
```

## Conclusiones y Aprendizajes

1. **Patrón Skill-as-a-Directory**: estructurar tools de agente con un `SKILL.md` descriptor + scripts ejecutables + referencias de API es un patrón replicable para cualquier capability de agente de IA.
2. **Orquestación tmux como UI de terminal**: usar tmux programáticamente para crear dashboards multi-panel es una alternativa potente a TUIs complejas (como `curses`), especialmente para herramientas de monitoreo.
3. **Scoring multi-criterio compuesto**: el enfoque de calcular sub-scores (conviction, volume, risk/reward) y combinarlos en un score final de oportunidad es directamente adoptable para cualquier sistema de ranking de activos o alertas.
4. **CLI como capa de abstracción de API**: wrappear una API externa en un CLI con subcomandos bien definidos facilita tanto el uso humano como el consumo por agentes de IA.
5. **Auto-refresh por panel con periodos diferenciados**: asignar frecuencias de refresco distintas según la criticidad del dato (30s para trades vs 5min para análisis) es una buena práctica de gestión de rate limits y UX.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code