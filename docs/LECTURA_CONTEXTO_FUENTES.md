# Lectura de contexto — repos y videos fuente

Este documento resume la lectura operativa de las fuentes incluidas en `repos/` y `videos/` antes de empezar a construir el MVP. No reemplaza los archivos originales; sirve como mapa de decisiones para implementación.

## Repos leídos

### `repos/666ghj_MiroFish.md`

**Propósito del Repo**

MiroFish es un motor de inteligencia de enjambre (swarm intelligence) de próxima generación que utiliza tecnología multi-agente para construir mundos digitales paralelos de alta fidelidad a partir de información semilla del mundo real (noticias, señales financieras, borradores de políticas). Miles de agentes con personalidades independientes, memoria a largo plazo y lógica conductual interactúan libremente para modelar evolución social y predecir trayectorias futuras. La propuesta de valor es permitir "ensayar el futuro en un sandbox digital".

Lo diferencia de otros sistemas de predicción su arquitectura de emergencia colectiva: en lugar de modelos estadísticos clásicos, captura el comportamiento emergente que surge de interacciones individuales a escala. Está diseñado tanto para analistas de decisiones (gobiernos, empresas) como para investigadores que quieran simular dinámica social, opinión pública, mercados financieros o incluso narrativas literarias.

**Arquitectura y Patrones Clave**

El sistema sigue una arquitectura **full-stack desacoplada**: backend Python (Flask/FastAPI) expuesto en el puerto 5001 y frontend Vue.js en el puerto 3000, orquestados mediante `concurrently` en modo desarrollo o Docker Compose en producción.

La capa de agentes combina tres patrones fundamentales:
- **Agent Memory con grafo de conocimiento**: integración con **Zep** para memoria persistente a largo plazo de cada agente, permitiendo que recuerden interacciones previas y mantengan coherencia temporal.
- **Simulación paralela**: el script `run_parallel_simulation.py` indica que múltiples agentes se ejecutan concurrentemente, probablemente con asyncio o threading.
- **LLM como motor de razonamiento**: cada agente usa un LLM (compatible con OpenAI SDK) para generar sus respuestas, con soporte para un LLM "boost" secundario para tareas de alta frecuencia.
- **Scripts de simulación especializados**: simulaciones dedicadas para Twitter, Reddit y casos generales, sugiriendo un patrón de estrategia para distintos dominios sociales.

**Componentes Principales**

- **`backend/app/api/`** — Endpoints REST que exponen las capacidades de simulación y predicción al frontend
- **`backend/app/models/`** — Modelos de datos para agentes, simulaciones y resultados
- **`backend/app/services/`** — Lógica de negocio: orquestación de agentes, integración LLM, gestión de memoria
- **`backend/app/utils/`** — Utilidades auxiliares (logging, helpers de API, procesamiento de datos)
- **`backend/scripts/run_parallel_simulation.py`** — Motor de simulación paralela principal
- **`backend/scripts/run_twitter_simulation.py`** — Simulación especializada para dinámicas de Twitter/X
- **`backend/scripts/run_reddit_simulation.py`** — Simulación especializada para dinámicas de Reddit
- **`backend/scripts/action_logger.py`** — Registro y trazabilidad de acciones de agentes
- **`frontend/src/views/`** — Vistas Vue.js para interfaz de usuario (configuración de simulación, dashboards)
- **`frontend/src/store/`** — Estado global Vuex/Pinia de la aplicación
- **`frontend/src/i18n/`** — Internacionalización (inglés y chino manifiesto en `locales/`)
- **`backend/app/config.py`** — Configuración centralizada que lee variables de entorno


### `repos/DFZinc_JANUS.md`

**Propósito del Repo**

JANUS es un sistema dual de agentes autónomos diseñado para operar en **Polymarket**, la plataforma de mercados de predicción descentralizados. El sistema implementa dos agentes diferenciados — **Hermes** y **Tyche** — que trabajan en conjunto para analizar, puntuar y ejecutar apuestas en mercados de predicción de forma automatizada.

El diseño dual sugiere una separación de responsabilidades clara: uno de los agentes probablemente se encarga de la recolección/análisis de datos e información del mercado (Hermes, mensajero), mientras el otro gestiona la estrategia de betting y gestión del riesgo (Tyche, diosa de la fortuna). Está orientado a traders algorítmicos y desarrolladores interesados en automatizar estrategias en mercados de predicción.

**Arquitectura y Patrones Clave**

El sistema sigue una arquitectura de **microservicios/agentes desacoplados** con las siguientes características notables:

- **Patrón Multi-Agent**: Dos agentes independientes (`hermes_agent.py`, `tyche_agent.py`) con bases de datos propias, lo que permite que operen con estado propio y ciclos de vida independientes.
- **Base de datos por agente**: Cada agente tiene su propia base de datos SQLite (`hermes.db`, `tyche.db`), siguiendo el patrón de **Database per Service**. Los archivos `-shm` y `-wal` indican uso de SQLite en modo **WAL (Write-Ahead Logging)**, optimizado para concurrencia.
- **API REST como capa de orquestación**: `server.py` expone endpoints FastAPI que probablemente coordinan o exponen el estado de ambos agentes.
- **Cliente de mercado desacoplado**: `polymarket_client.py` abstrae la comunicación con la API de Polymarket, siguiendo el patrón **Adapter/Client**.
- **Scorer independiente**: `bettor_scorer.py` separa la lógica de puntuación/evaluación de apuestas del resto del sistema.
- **Configuración externalizada**: `polymarket_config.json` sigue el principio de configuración separada del código.

**Componentes Principales**

- **`hermes_agent.py`** — Agente principal de análisis/inteligencia; probablemente consume datos de mercado y genera señales o evaluaciones.
- **`tyche_agent.py`** — Agente de ejecución de estrategia de betting; gestiona posiciones y decisiones de apuesta basándose en señales.
- **`hermes_db.py`** — Capa de acceso a datos y ORM para la base de datos de Hermes (SQLite).
- **`tyche_db.py`** — Capa de acceso a datos y ORM para la base de datos de Tyche (SQLite).
- **`polymarket_client.py`** — Cliente HTTP para interactuar con la API de Polymarket (mercados, precios, posiciones).
- **`bettor_scorer.py`** — Módulo de scoring que evalúa y puntúa oportunidades de apuesta o el rendimiento histórico.
- **`server.py`** — Servidor FastAPI que expone el sistema al exterior (API REST para control/monitoreo).
- **`polymarket_config.json`** — Configuración del sistema: credenciales, parámetros de mercado, umbrales.
- **`hermes.db` / `tyche.db`** — Bases de datos SQLite persistentes con WAL habilitado para cada agente.


### `repos/DevvGwardo_polymarket-dashboard-skill.md`

**Propósito del Repo**

Este repositorio implementa un dashboard terminal completo para monitorear mercados de predicción de Polymarket en tiempo real, diseñado específicamente como una "skill" para el agente de IA **Hermes**. Resuelve el problema de tener visibilidad consolidada sobre mercados de predicción: feeds en vivo, análisis estadístico y detección automatizada de oportunidades de beneficio, todo desde la terminal.

Está orientado a traders/analistas que operan con Polymarket y quieren integrar inteligencia de mercado en un flujo de trabajo basado en agentes de IA. Su diferencial es la arquitectura modular orientada a skills de agente: cada componente (live feed, stats, profit analyzer) puede correr independientemente o combinado en un panel tmux orquestado.

**Arquitectura y Patrones Clave**

El sistema sigue un patrón **multi-panel con orquestación tmux**: un script central (`launch-dashboard.sh`) crea una sesión tmux con múltiples paneles, cada uno ejecutando un script especializado con auto-refresh. Los componentes son:

- **Polling periódico**: cada panel tiene su propio ciclo de refresco (30s, 60s, 5min).
- **CLI como capa de abstracción**: `polymarket.py` actúa como cliente CLI unificado que encapsula llamadas a la API de Polymarket, exponiendo subcomandos (`search`, `trending`, `analyze`, etc.).
- **Skill-first design**: la estructura de directorios y el archivo `SKILL.md` indican que este repo está diseñado para ser consumido por el agente Hermes como una capability registrada.
- **Análisis por scoring compuesto**: el profit analyzer calcula métricas individuales (Risk/Reward, Conviction Score, Volume Score) y las combina en un Opportunity Score, patrón clásico de scoring multi-criterio.

**Componentes Principales**

- **`scripts/polymarket.py`** — Cliente CLI principal; encapsula las llamadas a la API de Polymarket con subcomandos para búsqueda, trending, historial de precios, orderbook, trades y análisis de oportunidades.
- **`scripts/launch-dashboard.sh`** — Orquestador tmux; crea la sesión completa del dashboard con múltiples paneles y gestiona el layout.
- **`scripts/live-feed.sh`** — Panel de feed en vivo; muestra mercados trending por volumen y trades recientes, con refresh cada 30s.
- **`scripts/stats-analysis.sh`** — Panel de análisis estadístico; realiza deep dives en mercados tracked, incluye gráficos ASCII de historial de precios y análisis de orderbook, refresh cada 60s.
- **`scripts/profit-analyzer.sh`** — Panel de detección de oportunidades; escanea los top 20 mercados, calcula métricas de riesgo/recompensa y expected value, refresh cada 5 min.
- **`scripts/setup.sh`** — Instalador; configura dependencias, rutas y registra el comando `polymarket-dashboard` en el sistema.
- **`references/api-endpoints.md`** — Documentación de referencia de los endpoints de la API de Polymarket usados.
- **`SKILL.md`** — Descriptor de la skill para el agente Hermes; define capacidades, comandos y contexto de uso.


### `repos/Fincept-Corporation_FinceptTerminal.md`

**Propósito del Repo**

Fincept Terminal es una aplicación de escritorio moderna orientada a finanzas, diseñada como alternativa open-source al Bloomberg Terminal. Ofrece herramientas de análisis de mercados, investigación de inversiones, datos económicos, trading algorítmico y agentes de IA, todo dentro de una interfaz gráfica interactiva construida con Qt6 y C++20, con Python como motor de scripting y análisis.

Está diseñado para traders, quants, analistas financieros e inversores individuales que necesitan acceso a capacidades de nivel institucional sin los costes prohibitivos de terminales comerciales. Su diferenciador clave es la combinación de un frontend nativo de alto rendimiento (C++/Qt6), un backend de scripting extensible (Python) y soporte nativo para agentes de IA, trading algorítmico y conexión a wallets cripto.

**Arquitectura y Patrones Clave**

La arquitectura es **híbrida C++/Python en capas**, con separación clara entre el core de la aplicación (C++20 + Qt6) y los scripts de análisis/agentes (Python). El frontend gráfico reside completamente en C++/Qt6, mientras que la lógica de dominio financiero compleja (AI agents, quantitative analysis, trading algorithms) se delega a scripts Python embebidos.

Patrones arquitectónicos notables:
- **Multi-stage Docker build**: construcción determinista y reproducible con soporte multi-arquitectura (amd64/arm64) usando BuildKit.
- **Separación por dominio**: cada funcionalidad financiera tiene su propio módulo (`algo_engine`, `datahub`, `trading`, `auth`, `mcp`), siguiendo principios de bajo acoplamiento.
- **Bridge C++/Python**: el directorio `src/python/` actúa como capa de integración entre el runtime C++ y los scripts Python.
- **ADR (Architecture Decision Records)**: el proyecto documenta decisiones arquitectónicas formalmente en `docs/adr/`.
- **CMake Presets**: configuración de build estandarizada con `CMakePresets.json` para diferentes entornos.
- **Packaging multiplataforma**: scripts dedicados para Flatpak (Linux), instaladores Windows/macOS, todos automatizados vía GitHub Actions.

**Componentes Principales**

- **`fincept-qt/src/app/`** — Punto de entrada de la aplicación Qt, inicialización del main window y ciclo de eventos
- **`fincept-qt/src/core/`** — Núcleo de la aplicación: gestión de estado, configuración y servicios fundamentales
- **`fincept-qt/src/screens/`** — Pantallas/vistas de la UI (dashboard, mercados, portfolio, etc.)
- **`fincept-qt/src/ui/`** — Componentes reutilizables de interfaz gráfica (widgets custom, layouts)
- **`fincept-qt/src/algo_engine/`** — Motor de trading algorítmico y backtesting
- **`fincept-qt/src/datahub/`** — Capa de ingesta y normalización de datos financieros de múltiples fuentes
- **`fincept-qt/src/trading/`** — Módulo de órdenes, ejecución y conexión a brokers (ej. AngelOne)
- **`fincept-qt/src/auth/`** — Autenticación y gestión de sesiones de usuario
- **`fincept-qt/src/mcp/`** — Implementación del protocolo MCP (Model Context Protocol) para agentes de IA
- **`fincept-qt/src/network/`** — Capa HTTP/WebSocket para llamadas a APIs externas
- **`fincept-qt/src/python/`** — Bridge de integración Python embebido en el runtime C++
- **`fincept-qt/src/services/`** — Servicios de aplicación (notificaciones, caché, persistencia)
- **`fincept-qt/src/storage/`** — Capa de almacenamiento local (SQLite u similar)
- **`fincept-qt/scripts/agents/`** — Agentes de IA para investigación y análisis autónomo
- **`fincept-qt/scripts/agno_trading/`** — Scripts de trading con el framework Agno
- **`fincept-qt/scripts/ai_quant_lab/`** — Laboratorio cuantitativo con ML/AI


### `repos/PacktPublishing_Machine-Learning-for-Algorithmic-Trading-Bots-with-Python.md`

**Propósito del Repo**

Este repositorio acompaña el curso de video de Packt Publishing *"Machine Learning for Algorithmic Trading Bots with Python"*. Su objetivo es enseñar a desarrolladores y científicos de datos con conocimientos básicos de Python cómo construir bots de trading algorítmico integrando técnicas de machine learning clásicas y modernas (Random Forests, Gradient Boosting, SVR, modelos bayesianos) sobre datos financieros reales de bolsa, forex y criptomonedas.

El repositorio se diferencia por combinar, de forma didáctica y progresiva, el flujo completo de un proyecto de trading cuantitativo: desde la obtención y análisis de datos hasta el backtesting con Zipline, la gestión de riesgo con VaR/CVaR y el despliegue de estrategias ejecutables. Está diseñado tanto para quienes buscan entrar al sector financiero como para profesionales que quieren automatizar estrategias de inversión con ML.

**Arquitectura y Patrones Clave**

El proyecto está organizado por **secciones del curso** (section 0001 a section 0006), cada una con notebooks Jupyter y, en las secciones avanzadas (5 y 6), scripts Python ejecutables desde Eclipse IDE. Las secciones reflejan una progresión pedagógica:

1. **Exploración y evaluación de estrategias base** (buy & hold, autocorrelación)
2. **Modelos supervisados progresivos**: Random Forest → Gradient Boosting → SVR
3. **Backtesting con Zipline**: los `Eclipse Projects` contienen `main.py` + `extension.py` con estrategias ejecutables en el motor de backtesting de Zipline
4. **Gestión de riesgo cuantitativo**: cálculo de VaR bayesiano y CVaR con modelos ML
5. **Persistencia de modelos**: uso de `joblib` para serializar estimadores entrenados (`rf_regressor.joblib`, `estimator.joblib`)

El patrón dominante es **script modular por estrategia**: cada estrategia vive en su propio archivo dentro de `strategies/` (e.g., `scalping.py`, `buy_and_hold.py`, `calendar.py`, `auto_correlation.py`) y se orquesta desde `main.py` mediante `run_zipline.py`.

**Componentes Principales**

- **`section 0001/`** — Notebooks de obtención de datos financieros y evaluación de estrategia base (buy & hold)
- **`section 0002/`** — Implementación y evaluación de Random Forest Regressor para predicción de precios; incluye modelo serializado (`rf_regressor.joblib`)
- **`section 0003/`** — Evaluación de estrategia con métricas de performance (`performance.csv`)
- **`section 0004/`** — Implementación de Gradient Boosting con Python
- **`section 0005/`** — Estrategia de scalping y su evaluación (`scalping.csv`)
- **`section 0006/`** — Sección avanzada: VaR bayesiano, CVaR con escalping, implementación de VaR con SVR; incluye modelo entrenado (`estimator.joblib`) y múltiples notebooks de evaluación
- **`section 0006/strategies/`** — Módulo de estrategias Zipline: `scalping.py`, `buy_and_hold.py`, `auto_correlation.py`, `calendar.py`, `run_zipline.py`
- **`Eclipse Projects/`** — Proyectos ejecutables por sección con `main.py` y `extension.py` para correr backtests en Zipline desde Eclipse
- **`buy_and_hold.py`** — Implementación standalone de la estrategia de referencia buy & hold
- **`Lecture Notebooks/`** — Copia alternativa de notebooks organizada como material de clase


### `repos/TheFourGreatErrors_alpha-rptr.md`

**Propósito del Repo**

alpha-rptr es un sistema de trading algorítmico automatizado diseñado para operar en múltiples exchanges de criptomonedas (Binance Futures, Bybit, BitMEX y FTX). Su objetivo central es minimizar las discrepancias entre los entornos simulados y el trading en vivo, permitiendo transiciones fluidas entre backtesting, paper trading y producción con cambios mínimos en el código de estrategia.

Está diseñado para traders algorítmicos con conocimientos básicos de trading que quieran desarrollar, testear y desplegar estrategias propias. Lo que lo diferencia es la unificación de múltiples modos de ejecución (backtest, hyperopt, stub/paper, demo y producción) bajo la misma interfaz de estrategia, junto con un extenso catálogo de indicadores técnicos y tipos de órdenes avanzados.

**Arquitectura y Patrones Clave**

El sistema utiliza un patrón **Factory + Strategy** bien definido: `src/factory.py` instancia el exchange y la estrategia correctos según la configuración, mientras que cada estrategia hereda de una clase base común definida en `src/bot.py`. Los exchanges se encapsulan como módulos independientes en `src/exchange/`, cada uno implementando la misma interfaz (órdenes, posiciones, cuenta), lo que permite intercambiarlos sin modificar la estrategia.

Para backtesting y paper trading existe un patrón **Adapter/Stub**: `src/exchange/backtest.py` y `src/exchange/stub.py` replican la interfaz de los exchanges reales, garantizando que el mismo código de estrategia funcione en todos los modos. La comunicación en tiempo real con los exchanges se realiza via **WebSocket**, y hay integración con **InfluxDB** para persistencia de métricas y monitorización. Se incluye un frontend HTML/JS (`html/`) para visualización de resultados.

**Componentes Principales**

- **`main.py`** — Punto de entrada; parsea argumentos CLI (modo, cuenta, exchange, par, estrategia) y arranca el bot
- **`src/bot.py`** — Clase base del bot; coordina el ciclo de vida, eventos de mercado y llamadas a la estrategia
- **`src/factory.py`** — Factory que instancia el exchange y la estrategia correctos según parámetros
- **`src/config.py`** — Gestión de configuración global (API keys, parámetros de sistema)
- **`src/exchange_config.py`** — Configuración específica por exchange (símbolos, apalancamiento, etc.)
- **`src/indicators.py`** — Biblioteca de indicadores técnicos: tendencia, volatilidad, momentum, medias móviles, bandas, regresión, normalización
- **`src/exchange/backtest.py`** — Implementación del exchange para modo backtest (replay de datos históricos)
- **`src/exchange/stub.py`** — Exchange simulado para paper trading en tiempo real
- **`src/exchange/binance_futures/`** — Conector específico para Binance Futures (WebSocket + REST)
- **`src/exchange/bitmex/`** — Conector para BitMEX
- **`src/exchange/bybit/`** — Conector para Bybit
- **`src/exchange/ftx/`** — Conector para FTX
- **`src/strategies/`** — Estrategias de referencia: `Sample`, `MACDLongOnly`, `Doten`, `Rci`, `SAR`, `SMA`, `SupertrendStrat`, `TV`, `OCC`, entre otras
- **`src/monitor.py`** — Monitorización en tiempo real de posiciones y órdenes
- **`src/gmail_sub.py`** — Integración con Gmail para recepción de señales externas
- **`html/`** — Dashboard web para visualización de resultados (HTML/JS/CSS con jQuery)
- **`tests/`** — Tests de integración para BitMEX, backtesting y WebSocket


### `repos/TradeAIcode_BOT-DE-TRADING.md`

**Propósito del Repo**

BOT DE TRADING V5.0 es una aplicación de escritorio para trading automático de criptomonedas, diseñada para traders que desean automatizar sus operaciones sin necesidad de conocimientos de infraestructura avanzada. Combina una interfaz gráfica completa construida con PyQt5 con lógica de trading real a través de CCXT, permitiendo conectarse a múltiples exchanges, ejecutar estrategias predefinidas o personalizadas, y gestionar el riesgo mediante Stop Loss, Take Profit y Trailing Stop.

Lo que diferencia este proyecto es su enfoque en accesibilidad: incluye un editor de estrategias en vivo dentro de la propia GUI, donde el usuario puede escribir código Python directamente y activarlo sin reiniciar el bot. Es una solución todo-en-uno que va desde la configuración del exchange hasta la exportación del historial de operaciones a Excel.

**Arquitectura y Patrones Clave**

El proyecto sigue una arquitectura modular por capas bien diferenciadas:

- **Capa UI** (`ui/`): Ventanas y tabs PyQt5, separadas por responsabilidad (tab principal, ventana principal, tab de estrategia personalizada).
- **Capa Core** (`core/`): Lógica de ejecución del bot — el worker que corre en background, gestión de stop loss, trailing stop y auto-profit.
- **Capa de Estrategias** (`strategies/`): Módulos independientes por estrategia, con un archivo `indicators.py` compartido. Permite añadir nuevas estrategias como plugins.
- **Capa Utils** (`utils/`): Servicios transversales — gestión de configuración, estado, base de datos, historial y configuración de API.

El patrón central es **Worker/Thread separado de la UI**: el trading corre en un hilo distinto (`core/worker.py`) para no bloquear la interfaz gráfica. La carga de estrategias personalizadas sugiere uso de `exec()`/`importlib` dinámico. La configuración se gestiona con managers dedicados, separando la config de API de la config operacional.

**Componentes Principales**

- **`main.py`** — Punto de entrada: inicializa la aplicación PyQt5 y lanza la ventana principal
- **`core/worker.py`** — Hilo de trading: bucle principal que ejecuta la estrategia activa y gestiona el ciclo de órdenes
- **`core/stop_loss.py`** — Lógica de Stop Loss fijo para protección de posiciones
- **`core/trailing_stop.py`** — Implementación de Trailing Stop dinámico que sigue el precio
- **`core/auto_profit.py`** — Lógica de toma de ganancias automática (Take Profit)
- **`core/exchange_utils.py`** — Abstracción sobre CCXT: conexión al exchange, colocación de órdenes, consulta de balance
- **`strategies/indicators.py`** — Cálculo de indicadores técnicos compartidos (RSI, EMA, etc.) usando pandas
- **`strategies/ema_cross_original.py`** — Estrategia de cruce de medias móviles exponenciales
- **`strategies/rsi_improved.py`** — Estrategia RSI mejorada con filtros adicionales
- **`strategies/ema_pullback.py`** — Estrategia de entrada en retrocesos sobre EMA
- **`strategies/bmsb_*.py`** — Familia de estrategias BMSB (variantes: close, invert, ontime)
- **`strategies/custom_strategy.py`** — Cargador dinámico de la estrategia escrita por el usuario en la GUI
- **`ui/main_window.py`** — Ventana principal PyQt5, organiza tabs y conecta señales
- **`ui/main_tab.py`** — Tab principal: controles de start/stop, selección de par y estrategia, logs en tiempo real
- **`ui/custom_strategy_tab.py`** — Editor de código Python integrado para estrategias personalizadas
- **`utils/api_config_manager.py`** — Gestión segura de credenciales API (claves de exchange)


### `repos/coding-kitties_investing-algorithm-framework.md`

**Propósito del Repo**

Investing Algorithm Framework es un framework completo para el ciclo de vida cuantitativo de trading: permite diseñar estrategias, hacer backtesting (vectorial y event-driven), comparar resultados en un dashboard unificado y desplegar el algoritmo ganador como bot en producción. Está orientado a quants y desarrolladores Python que quieren evitar reinventar infraestructura (gestión de órdenes, portafolios, datos, scheduling) y centrarse en la lógica de estrategia.

Lo que lo diferencia de alternativas como Backtrader o Zipline es que integra en un único paquete: gestión de portafolio persistente con SQLAlchemy, conectividad live via CCXT (criptomonedas), soporte para múltiples data providers (yfinance, Alpha Vantage, Polygon), storage en cloud (Azure Blob, S3), y un CLI para scaffolding y despliegue.

**Arquitectura y Patrones Clave**

El proyecto sigue una **arquitectura en capas** bien definida (Domain → Infrastructure → Services → App) típica de Domain-Driven Design:

- **Domain:** modelos de negocio puros, interfaces de servicios, lógica de backtesting y pipelines — sin dependencias externas.
- **Infrastructure:** implementaciones concretas (SQLAlchemy ORM, repositorios, proveedores de datos externos, ejecutores de órdenes vía CCXT).
- **Services:** orquestación entre domain e infrastructure (order service, trade service, portfolio service, backtest store, métricas).
- **App:** punto de entrada del usuario — algoritmo, reporting, API web Flask, modo stateless.

Se usa **Dependency Injection** (`dependency-injector`) para desacoplar capas y facilitar testing. El **patrón Repository** abstrae el acceso a datos. Los **pipelines** (domain/pipeline) permiten construir estrategias como grafos de pasos. El scheduling se maneja con `schedule`, y la exposición opcional de endpoints usa **Flask + Flask-Migrate**.

El storage de backtests usa **Polars** (DataFrames rápidos), **msgpack + zstandard** para serialización comprimida, y **PyArrow** para interoperabilidad columnar — decisión de rendimiento frente a pandas puro.

**Componentes Principales**

- **`investing_algorithm_framework/app/`** — Punto de entrada principal: clase `App`, gestión del algoritmo, reporting y API web
- **`investing_algorithm_framework/app/algorithm/`** — Motor de ejecución del algoritmo: scheduling, ciclo de vida run/stop
- **`investing_algorithm_framework/app/stateless/`** — Modo stateless para backtesting sin base de datos persistente
- **`investing_algorithm_framework/domain/`** — Modelos de negocio puros, interfaces, lógica de backtesting y pipeline
- **`investing_algorithm_framework/domain/models/`** — Entidades: Order, Trade, Position, Portfolio, Symbol, etc.
- **`investing_algorithm_framework/domain/pipeline/`** — Abstracción de pipelines de estrategia (grafos de transformación de datos)
- **`investing_algorithm_framework/domain/backtesting/`** — Motor de backtesting event-driven y vectorial
- **`investing_algorithm_framework/infrastructure/`** — Implementaciones concretas: ORM SQLAlchemy, CCXT, repositorios
- **`investing_algorithm_framework/infrastructure/data_providers/`** — Conectores a yfinance, Alpha Vantage, Polygon
- **`investing_algorithm_framework/infrastructure/order_executors/`** — Ejecución de órdenes real vía CCXT
- **`investing_algorithm_framework/services/`** — Capa de orquestación: order_service, trade_service, portfolio, backtest_store, métricas
- **`investing_algorithm_framework/services/backtest_store/`** — Persistencia y comparación de resultados de backtests
- **`investing_algorithm_framework/services/metrics/`** — Cálculo de métricas cuantitativas (Sharpe, drawdown, etc.)
- **`investing_algorithm_framework/cli/`** — CLI con templates para scaffolding de nuevos proyectos
- **`investing_algorithm_framework/notebook/`** — Integración Jupyter para análisis interactivo
- **`examples/strategies_showcase/`** — 26 estrategias de ejemplo: trend-following, mean-reversion, pairs trading, market making, HFT, opciones, etc.


### `repos/criss201x_Trading_inteligente_con_algoritmos_de_aprendizaje_automatico.md`

**Propósito del Repo**

Este repositorio implementa un pipeline completo de trading algorítmico inteligente que combina extracción de datos financieros, análisis estadístico y modelos de aprendizaje automático para apoyar la toma de decisiones de inversión. El proyecto cubre todo el flujo desde el web scraping de datos bursátiles hasta la aplicación de algoritmos como Montecarlo, K-Means, GMM, Filtro de Kalman y redes neuronales sobre series temporales de precios.

Está diseñado como un proyecto académico/educativo orientado a analistas financieros, estudiantes de ciencia de datos y desarrolladores interesados en la intersección entre ML y finanzas cuantitativas. Su diferenciación radica en cubrir múltiples etapas del pipeline de forma modular: extracción, procesamiento, análisis de correlación, análisis de sentimiento y modelado predictivo, todo en Python.

**Arquitectura y Patrones Clave**

El repositorio sigue una arquitectura de **pipeline ETL financiero por etapas**, donde cada carpeta representa una fase independiente del flujo de datos:

1. **Extracción** → scraping y descarga de datos históricos
2. **Preprocesamiento** → filtrado (Kalman), normalización
3. **Análisis** → correlación entre activos, análisis estadístico
4. **Modelado** → clustering (K-Means, GMM), simulación (Montecarlo), clasificación (redes neuronales)
5. **Señales** → análisis de sentimiento correlacionado con precios

El patrón dominante es el de **scripts independientes por técnica**, sin acoplamiento entre módulos, lo que facilita el estudio individual de cada algoritmo. No hay framework de orquestación; cada `.py` es autocontenido con sus propias cargas de datos.

**Componentes Principales**

- **`Extraccion de datos/Extraccion de datos.py`** — Descarga de datos históricos de acciones (probablemente via Yahoo Finance o similar)
- **`Extraccion de datos/filtro de kalman.py`** — Implementación del Filtro de Kalman para suavizado de series de precios y reducción de ruido
- **`Extraccion de datos/procesado de datos.py`** — Limpieza y transformación de datos crudos para consumo por modelos
- **`Analisis de correlacion/Finanzas_en_Wilkipedia.py`** — Web scraping de Wikipedia para obtener lista de empresas del S&P 500 y análisis de correlación entre activos
- **`Analisis de datos financieros/analisis de montecarlo.py`** — Simulación de Montecarlo para estimación de distribuciones de retornos futuros
- **`Analisis de datos financieros/Ejercicio de bolsa por clusterizacion.py`** — Agrupación de acciones por comportamiento usando clustering
- **`Modelos de machine learning aplicados al trading/k-means_aplicado_al_trading.py`** — K-Means para identificar regímenes de mercado o grupos de activos similares
- **`Modelos de machine learning aplicados al trading/gaussian_mixture_model_aplicado_al_trading.py`** — GMM para modelado probabilístico de estados de mercado
- **`Analisis de sentimiento/Analisis_de_sentimiento_basico.py`** — Análisis de sentimiento sobre tweets financieros
- **`Analisis de sentimiento/Analisis_de_sentimiento_y_correlacion.py`** — Correlación entre sentimiento de redes sociales y movimientos de precio
- **`Redes Neuronales/Clasificacion por redes neuronales.py`** — Clasificador neuronal para señales de compra/venta
- **`Redes Neuronales/Preprocesamiento de datos.py`** — Pipeline de features para alimentar la red neuronal
- **`Series temporales/entrenamiento_dataset.py`** — Preparación de datasets temporales con ventanas deslizantes


### `repos/josepobletem_cripto_trader.md`

**Propósito del Repo**

`cripto_trader` es un bot de trading automático de criptomonedas diseñado como plataforma educativa y de producción ligera. Combina la API de Binance para operar en mercados crypto, OpenAI (GPT-4) para explicar en lenguaje natural las decisiones de compra/venta, y FastAPI para exponer los endpoints de control. Su principal diferenciador es la integración de IA explicativa junto con una estrategia algorítmica clásica (cruce de EMAs), presentando todo en un stack completo con persistencia, observabilidad (Prometheus) y despliegue en nube mediante Terraform.

Está diseñado para desarrolladores que quieren iniciarse en trading algorítmico, aprender integración de APIs financieras y de IA, y tener una base sólida y auditable que puedan extender hacia un producto real o usarlo como portafolio técnico.

**Arquitectura y Patrones Clave**

El proyecto sigue una arquitectura de capas con separación clara de responsabilidades dentro del paquete `trading/`. El flujo principal es: el scheduler dispara la estrategia periódicamente → la estrategia consulta precios a Binance → decide BUY/SELL/HOLD → GPT genera una explicación → la operación se persiste en SQLite. FastAPI actúa como capa de control/observabilidad, exponiendo un webhook para ejecución manual.

Patrones técnicos destacados:
- **Scheduler-driven architecture**: APScheduler ejecuta la lógica de trading en intervalos configurables sin intervención manual.
- **Strategy Pattern**: La lógica de decisión está aislada en `strategy.py`, separada del cliente HTTP y la persistencia.
- **Repository Pattern ligero**: `db.py` encapsula todas las operaciones SQLAlchemy.
- **Decorator/Middleware de observabilidad**: Prometheus-client expone métricas en tiempo real.
- **IaC con Terraform**: Infraestructura reproducible para GCP (Cloud Run) y AWS (ECS/EC2).
- **CI/CD**: GitHub Actions en `.github/workflows/ci.yml` para lint, tests y validación automática.

**Componentes Principales**

- **`main.py`** — Punto de entrada FastAPI; define rutas (incluyendo `/webhook` para ejecución manual) y arranca el scheduler al iniciar.
- **`trading/binance_client.py`** — Wrapper sobre `python-binance`; obtiene precios OHLCV y ejecuta órdenes en el exchange.
- **`trading/strategy.py`** — Implementa la estrategia de cruce de EMAs (EMA corta vs EMA larga) para generar señales BUY/SELL/HOLD.
- **`trading/gpt_helper.py`** — Llama a la API de OpenAI para generar una explicación en lenguaje natural de cada decisión de trading.
- **`trading/scheduler.py`** — Configura y lanza APScheduler para ejecutar el ciclo de trading automáticamente.
- **`trading/db.py`** — Capa de persistencia con SQLAlchemy; guarda cada operación en SQLite (`trades.db`).
- **`trading/schemas.py`** — Modelos Pydantic para validación de datos de entrada/salida en FastAPI.
- **`trading/logger.py`** — Configuración centralizada de logging hacia `trading.log`.
- **`infra/gcp/` y `infra/aws/`** — Archivos Terraform para despliegue en GCP Cloud Run y AWS respectivamente.
- **`tests/`** — Suite de tests unitarios con pytest para cada módulo + tests de infraestructura simulada.


### `repos/strongmandisabilitypayment539_hermes-geopolitical-market-sim.md`

**Propósito del Repo**

⚠️ **ADVERTENCIA DE SEGURIDAD — Repositorio de distribución de malware potencial**

Este repositorio NO es un proyecto de software legítimo. Se trata de un repositorio señuelo ("lure repo") que distribuye un archivo ZIP de origen desconocido (`sim-market-hermes-geopolitical-2.4.zip`) bajo la apariencia de una herramienta de simulación geopolítica. El patrón es clásico de campañas de distribución de malware en GitHub: nombre de cuenta aleatoria con números, README genérico orientado a usuarios no técnicos, badge prominente de descarga, topics irrelevantes mezclados (bengali, palantir, clawdbot, moltbot) y un único activo binario sin código fuente visible ni licencia.

No existe código fuente auditable, no hay dependencias declaradas, no hay estructura de proyecto real. El "software" es exclusivamente un ZIP descargable sin verificación de integridad (sin checksums SHA256, sin firma GPG).

**Arquitectura y Patrones Clave**

No existe arquitectura técnica analizable. Los elementos observables son:

- **Estructura mínima:** Una carpeta `dustyfoot/` con únicamente un README y un archivo ZIP
- **Sin código fuente:** Cero archivos `.ts`, `.js`, `.py` u otro lenguaje pese a declarar TypeScript como topic
- **Táctica de ingeniería social:** README redactado para usuarios sin experiencia técnica ("You do not need coding experience"), instrucciones de "haz clic en Sí si Windows pide permiso" — texto diseñado para reducir fricción ante alertas de seguridad del SO
- **Topics inflados artificialmente:** Mezcla de términos de alto valor SEO (palantir, llm, chatgpt, hermes-engine) sin relación funcional para atraer búsquedas

**Componentes Principales**

| Elemento | Descripción |
|---|---|
| `dustyfoot/README.md` | Documento señuelo con instrucciones de descarga e instalación |
| `dustyfoot/sim-market-hermes-geopolitical-2.4.zip` | Archivo binario no auditable — **no descargar** |


### `repos/tudorelu_pyjuque.md`

**Propósito del Repo**

pyjuque (Python Juju Quant Engine) es un framework de trading algorítmico open source diseñado para ser un punto de partida estructurado para bots de trading en criptomonedas. Resuelve el problema de tener que construir desde cero la infraestructura básica de un bot (gestión de órdenes, persistencia, conexión a exchanges, backtesting) permitiendo al desarrollador centrarse en la lógica de la estrategia.

Está diseñado para traders-desarrolladores que quieren automatizar estrategias en exchanges como Binance, KuCoin u OKEx, con soporte multi-exchange vía CCXT. Su diferenciador es que combina en un solo paquete el ciclo completo: backtesting, simulación, ejecución live y plotting, con un template de estrategia que estandariza cómo se definen las señales de entrada/salida.

**Arquitectura y Patrones Clave**

El proyecto sigue una arquitectura en capas claramente separadas:
- **Capa de Exchange:** abstrae la comunicación con los exchanges mediante wrappers (Binance nativo + CcxtExchange genérico)
- **Capa de Engine:** contiene el BotController que orquesta el ciclo principal del bot, el OrderManager para gestión de órdenes, y modelos de base de datos vía SQLAlchemy (ORM)
- **Capa de Estrategia:** usa el patrón Template Method — `StrategyTemplate` define la interfaz (`setUp`, señales long/short) y el usuario implementa subclases
- **Capa de Backtesting:** motor separado que reutiliza las mismas estrategias para simulación histórica
- **Capa de Plotting:** visualización con Plotly

El patrón principal es **Template Method** para estrategias, **Adapter/Wrapper** para los exchanges, y **Repository** implícito con SQLAlchemy para persistencia de órdenes y posiciones. La configuración del bot se pasa como diccionario estructurado, lo que actúa como un patrón de **Builder declarativo**.

**Componentes Principales**

- **`pyjuque/Bot.py`** — Punto de entrada principal; configura y lanza el bot a partir de un diccionario de configuración
- **`pyjuque/Engine/BotController.py`** — Orquestador del ciclo de vida del bot: polling, evaluación de señales, emisión de órdenes
- **`pyjuque/Engine/OrderManager.py`** — Gestión del ciclo de vida de órdenes (apertura, seguimiento, cierre, stop-loss)
- **`pyjuque/Engine/Database.py`** — Configuración de SQLAlchemy, sesiones y conexión a BD
- **`pyjuque/Engine/Models/`** — Modelos ORM para Bot, Pair, Order
- **`pyjuque/Engine/GridBotController.py`** — Implementación especializada de bot tipo grid trading
- **`pyjuque/Exchanges/CcxtExchange.py`** — Wrapper genérico multi-exchange usando la librería CCXT
- **`pyjuque/Exchanges/Binance.py`** — Wrapper nativo específico para Binance REST API
- **`pyjuque/Exchanges/BinanceOrderBook.py`** — Gestión del order book local vía WebSocket para Binance
- **`pyjuque/Backtester/Backtester.py`** — Motor de backtesting que corre estrategias sobre datos históricos (CSV o exchange)
- **`pyjuque/Strategies/__init__.py`** — Define `StrategyTemplate`, la clase base que todas las estrategias deben extender
- **`pyjuque/Utils/Plotter.py`** — Visualización de resultados de backtesting con Plotly (velas, señales, líneas Fibonacci)
- **`examples/`** — Ejemplos funcionales de backtesting, bot live, simulación y estrategias custom


## Videos leídos

### `videos/5_Ways_I_Make_Money_With_Hermes_Agent.md`

**Conclusiones y Aprendizajes**

- **Diseña workflows, no fantasías**: Antes de usar Hermes en producción, identifica una función de negocio real (ventas, contenido, ops) y diseña el flujo completo con el agente como asistente, no como ejecutor autónomo.
- **Human-in-the-loop es obligatorio** para cualquier acción externa (enviar emails, ejecutar trades, responder clientes). El agente prepara, el humano valida.
- **Los prompts incluidos son plantillas reutilizables** para los cinco casos. Se pueden adaptar cambiando industria, keywords y umbrales (ej. % de movimiento de mercado).
- **Client ops es el caso más aplicable internamente**: cualquier equipo con llamadas de cliente puede implementar el flujo de "notas → follow-up + action items + reminders" de inmediato.
- **Recurring jobs = productized services**: si el agente puede ejecutar un reporte diario o semanal, ese reporte puede venderse como suscripción sin incremento de esfuerzo manual.
- **Guardrails en trading son críticos**: si se construye un agente de alertas de mercado, separar estrictamente la capa de lectura/alerta de la capa de ejecución de órdenes.
- **Repositorios open-source disponibles**: el autor ha publicado el agente de YouTube research y el de monitoreo de X/YouTube en GitHub, listos para importar como skills de Hermes.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video presenta un enfoque pragmático para monetizar el agente Hermes, rechazando explícitamente la narrativa de "dinero mágico con IA". El autor posiciona a Hermes como un **junior operator** —no un bot autónomo— capaz de investigar, monitorear, redactar, recordar y resumir, con el objetivo de eliminar el trabajo operativo repetitivo alrededor de oportunidades de negocio reales.

Los cinco casos de uso propuestos son: (1) generación de leads y outreach, (2) investigación de contenido, (3) scouting de tendencias en tiempo real, (4) alertas de mercados de predicción (Polymarket), y (5) operaciones con clientes (client ops). Cada caso incluye un prompt concreto y listo para usar, con énfasis en que el agente asiste y el humano decide antes de ejecutar cualquier acción externa.

El autor insiste en un principio central: **vender el resultado, nunca el método**. Los clientes no pagan por "outreach con IA", pagan por "un pipeline semanal de leads calificados con ángulos personalizados". Hermes es el motor invisible, no el producto.


### `videos/Algotrading_Frameworks_Overview.md`

**Conclusiones y Aprendizajes**

- **Elegir un framework antes de construir desde cero**: Para proyectos de algo trading que van a producción, frameworks como Freqtrade o Jesse Trade eliminan semanas de trabajo en infraestructura (DB, Docker, logging, UI).
- **Separar estrategia de infraestructura**: El patrón correcto es que la lógica de la estrategia esté aislada; el framework maneja todo lo demás. Esto aplica directamente al diseño de software en cualquier dominio.
- **Evaluar riesgo de abandono**: Antes de adoptar cualquier framework open-source, verificar actividad reciente en GitHub (commits, issues, mantenedores activos, número de contributors).
- **Documentación como señal de madurez**: Frameworks con buena documentación indican comunidad saludable; mala documentación es red flag de sostenibilidad.
- **Vendor lock-in en soluciones cloud**: Al evaluar QuantConnect u otras soluciones SaaS, considerar el costo de migración si el servicio cambia o desaparece.
- **Data pipeline como componente crítico**: El acceso a datos históricos de calidad (especialmente para stocks y opciones) es frecuentemente el cuello de botella y puede determinar qué framework usar.
- **Empezar con lo open-source**: Para experimentar y aprender, comenzar con Freqtrade o Jesse antes de comprometer presupuesto en soluciones comerciales.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video introduce una serie sobre frameworks open-source de algo trading, comparando varias opciones disponibles tanto para criptomonedas como para acciones/equities. El presentador muestra en vivo su instancia de Freqtrade corriendo en la nube, demostrando sus capacidades de monitoreo, logging y control vía Telegram, y anuncia tutoriales profundos para Freqtrade, Jesse Trade, Hummingbot, QuantConnect y las herramientas heredadas del ecosistema Quantopian (Zipline, Alphalens, Pyfolio).

El argumento central del video es que estos frameworks resuelven problemas comunes de infraestructura —fetching de datos, backtesting, trading en vivo, manejo de errores, logging, métricas de performance y UI— sin que el desarrollador tenga que reinventar la rueda. La analogía con frameworks web (Flask, Django, React, Vue.js) es central: adoptar un framework establece un lenguaje común y patrones de diseño compartidos con una comunidad, lo que facilita la colaboración y el debugging.

El video cierra con un análisis equilibrado de pros y contras entre soluciones comerciales (QuantConnect) y soluciones open-source gratuitas (Freqtrade, Jesse, Hummingbot), cubriendo aspectos como calidad de documentación, acceso a datos históricos, vendor lock-in, riesgo de abandono y costo mensual.


### `videos/Alpaca_Python_Algorithmic_Trading_Tutorial_Build_a_Trading_B.md`

**Conclusiones y Aprendizajes**

- **Setup en minutos:** Con solo ~15 líneas de Python se puede tener un bot funcional que ejecuta órdenes reales en mercados financieros; es un punto de partida sólido para proyectos de mayor complejidad.
- **Siempre usar `paper=True` en desarrollo:** El flag debe estar presente en cualquier entorno que no sea producción para evitar operaciones accidentales con dinero real.
- **Separación de credenciales:** Las API keys deben almacenarse en variables de entorno o un gestor de secretos, nunca hardcodeadas en el código fuente.
- **Patrón Request Object:** El SDK usa el patrón de objetos de solicitud (`MarketOrderRequest`) que facilita la validación antes de enviar, lo que es una buena práctica para extender a otros tipos de órdenes (limit, stop, etc.).
- **Inspección de cuenta útil para estrategias:** Los métodos `get_account()` y `get_asset()` permiten construir lógica condicional basada en estado del portafolio (ej. solo operar si el P&L del día supera X%).
- **Escalabilidad:** Este mismo patrón se puede extender para añadir estrategias, scheduling con `schedule` o `APScheduler`, y manejo de websockets para datos en tiempo real.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video presenta una guía práctica paso a paso para ejecutar operaciones bursátiles algorítmicas usando la API de Alpaca Markets con Python. El autor argumenta que la principal barrera de entrada al trading algorítmico no es la complejidad estratégica, sino las fricciones técnicas de los brokers tradicionales (reautenticación frecuente, documentación obsoleta), y posiciona Alpaca como una solución moderna que simplifica este proceso.

El tutorial cubre desde el registro en Alpaca Markets y la generación de API keys hasta la ejecución de una orden de mercado real (en modo paper trading), pasando por la instalación de la librería `alpaca-py`, la conexión al cliente de trading, la inspección de detalles de cuenta y la consulta de activos. Todo el flujo se demuestra en menos de 5 minutos con código mínimo y funcional.

El enfoque es deliberadamente didáctico y orientado a la acción: cada bloque de código se muestra, se ejecuta en vivo y se verifica su output, lo que hace el tutorial especialmente útil para desarrolladores que quieren un punto de entrada rápido al trading programático sin configuraciones complejas.


### `videos/Build_a_Python_Trading_Bot_for_Algorithmic_Trading_Using_AI_.md`

**Conclusiones y Aprendizajes**

**Arquitectura replicable para proyectos de trading automatizado:**
- El patrón **cloud notebook + túnel TCP + API broker local** es una arquitectura funcional para prototipos de trading sin infraestructura dedicada
- Separar la lógica en threads (data ingestion thread + trading listener thread + visualization) es fundamental para sistemas en tiempo real

**Sobre el uso de AI para generar código:**
- Los prompts funcionan bien para código estándar y secciones independientes, pero el código de integración compleja (WebSocket + threading + broker API) requiere un **proceso iterativo**, no generación de un solo shot
- Útil como copiloto, no como reemplazo: el autor terminó usando su propio código validado para las partes críticas

**Consideraciones de producción antes de usar dinero real:**
1. **Backtesting obligatorio** antes de ejecutar cualquier estrategia
2. **Modelar comisiones** en el backtesting — son deal-breakers en estrategias de alta frecuencia con bajo volumen
3. **Detección de outliers/spikes** en datos en tiempo real (el autor observa spikes anómalos en los precios de SPY)
4. **Cooldown periods** y `max_positions` como salvaguardas básicas de gestión de riesgo
5. **Datos de calidad** (tiempo real vs. end-of-day) determinan qué tipo de estrategia es viable

**Stack mínimo para replicar:**

**Resumen Ejecutivo**

El video es un tutorial práctico de extremo a extremo para construir un bot de trading algorítmico en Python usando paper trading (dinero simulado). El autor conecta un notebook en la nube (Datalure) con Interactive Brokers a través de su API (IB Insync), primero con datos históricos gratuitos y luego con datos en tiempo real a través de Polygon.io. La estrategia implementada es un **Moving Average Crossover** adaptado a distintas granularidades: 20/50 días para datos históricos y 20/50 segundos para datos en tiempo real.

El autor es transparente desde el inicio: esta es una prueba de concepto, no una estrategia validada para generar ganancias. El objetivo es demostrar que se puede construir la infraestructura completa (conexión API, lógica de señales, ejecución automatizada de órdenes) y dejarlo funcionando en un entorno paper trading. El sistema llega a ejecutar trades reales (en simulación) basándose en señales en vivo del mercado.

Un punto crítico que emerge al final es la viabilidad económica: con comisiones de ~$1 por operación sobre posiciones pequeñas (~$560 por acción de SPY), la estrategia de alta frecuencia con un solo share es matemáticamente perdedora (~2% de pérdida inmediata por trade). El autor reconoce esto y apunta a futuras iteraciones con mayor volumen, backtesting riguroso y posiblemente modelos de ML/AI para encontrar estrategias rentables.


### `videos/Cómo_Crear_un_BOT_de_Trading_AUTOMÁTICO_Guía_Completa.md`

**Conclusiones y Aprendizajes**

- **Separar la lógica de negocio del código:** La estrategia (qué hacer) debe estar validada estadísticamente antes de invertir tiempo en automatizarla. Primero backtesting largo, luego código.
- **Herramientas no-code como primer approach:** Constructores como Strategy Quant permiten iterar rápidamente sobre ideas de estrategia sin necesitar conocimientos de programación, y generan código exportable a plataformas reales.
- **IA generativa como copiloto de código:** ChatGPT puede generar Expert Advisors funcionales si se describe la lógica con precisión; válido como prototipo rápido antes de un programador profesional.
- **Infraestructura de despliegue:** Para cualquier bot de trading en producción, un VPS dedicado es imprescindible. El coste (~20 €/mes) es mínimo frente al riesgo de perder operaciones por caída del equipo local.
- **Conocer los costes operativos del activo:** Spread, comisiones y swap deben incluirse en el backtesting para que los resultados sean realistas y no optimistas.
- **Principio de un activo por estrategia:** El autor recomienda estrategias específicas para un solo activo en lugar de estrategias multi-activo genéricas, buscando mayor especialización y robustez.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video presenta una guía estructurada en cuatro pasos para crear un bot de trading automatizado desde cero. El autor cubre todo el ciclo de vida del robot: desde encontrar una estrategia rentable, definir el ecosistema operativo (activo, broker y plataforma), automatizar la estrategia mediante código o herramientas sin código, hasta desplegar el bot en un servidor VPS para garantizar disponibilidad continua.

El ejemplo práctico utilizado a lo largo del video es una estrategia de cruce de medias móviles (EMA 20 / EMA 50) sobre el par EUR/USD en timeframe de 1 hora, operada en MetaTrader 5 con el broker Darkness. Se demuestra cómo construir y hacer backtesting de la estrategia con Strategy Quant, exportar el código generado y cargarlo directamente en MT5 dentro de un VPS ya contratado.

El autor enfatiza que el mayor riesgo no está en la automatización sino en la calidad de la estrategia subyacente, y recomienda herramientas basadas en IA y fuerza bruta (constructores como Strategy Quant) como la vía más eficiente para encontrar estrategias robustas con historial de 10-20 años.


### `videos/Cómo_Hacer_un_BOT_de_TRADING_en_Python_Parte_1.md`

**Conclusiones y Aprendizajes**

**Aplicaciones directas en proyectos de software:**

1. **Bootstrap rápido de datos financieros**: Con menos de 10 líneas de Python se puede tener un pipeline funcional de descarga de datos OHLCV para cualquier activo disponible en Yahoo Finance, sin coste alguno.

2. **Patrón de configuración por archivo externo**: El uso de `scope.txt` es un patrón simple pero efectivo para desacoplar la configuración (universo de activos) del código, facilitando cambios sin tocar el script.

3. **Distinción crítica de formato de ticker**: Recordar siempre el sufijo `-USD` para criptomonedas en yfinance; omitirlo genera datos erróneos silenciosamente (el script no falla, pero los datos no tienen sentido).

4. **Limitaciones a considerar**: Yahoo Finance no garantiza completitud ni precisión; para backtesting serio con datos pre-2014 en cripto o datos intradiarios se necesitarán fuentes alternativas.

5. **Estructura base para un bot**: La combinación ticker → descarga histórico → almacenamiento en variables `precio` y `volumen` → iteración sobre scope, es la base sobre la que se construirán los módulos de análisis técnico y señales de trading en episodios posteriores.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

Este es el primer episodio de una serie orientada a construir un bot de trading automatizado en Python. El vídeo se centra exclusivamente en el primer paso fundamental: la descarga automática de datos históricos de precios y volumen de activos financieros (criptomonedas y acciones de bolsa) utilizando la librería gratuita `yfinance`, que extrae datos de Yahoo Finance.

El autor explica cómo usar el método `Ticker` y `history()` para obtener el histórico de precios de cierre (`Close`) y volumen (`Volume`) de cualquier activo, con distintos rangos temporales. También introduce el concepto de un archivo `scope.txt` que actúa como lista de activos a rastrear, permitiendo iterar sobre múltiples tickers de forma automatizada con muy pocas líneas de código.

El vídeo está intencionalmente simplificado por ser el primero de la serie con código. Se usa `matplotlib` únicamente para visualizar y verificar que los datos descargados son correctos. El siguiente episodio de la serie avanza hacia análisis técnico automático con medias móviles (cruce dorado y cruce de la muerte).


### `videos/Cómo_crear_tu_propio_robot_de_trading_en_Python_Fácil_y_en_m.md`

**Conclusiones y Aprendizajes**

- **Arquitectura mínima de un bot de trading**: separar la capa de datos (EODHD), la capa de lógica (cálculo de señales con pandas/SMA) y la capa de ejecución (Alpaca API) en funciones independientes facilita el mantenimiento y la extensibilidad.
- **Validar antes de producción**: crear un script de prueba que compruebe conexión, estado del mercado, posiciones y ejecución de órdenes es una práctica esencial antes de activar el bot con dinero real.
- **Gestión de posiciones duplicadas**: siempre verificar posiciones abiertas con `get_position` antes de emitir una nueva orden sobre el mismo símbolo.
- **Escalabilidad del enfoque**: el mismo esquema puede adaptarse a otros activos, otros indicadores técnicos o incluso modelos de ML/IA para generar señales más sofisticadas.
- **Paper Trading como entorno de staging**: usar cuentas de simulación equivale a tener un entorno de pruebas antes de desplegar en producción — un principio directamente análogo al desarrollo de software.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video muestra cómo construir un robot de trading básico en Python usando dos APIs externas: **EODHD** para obtener datos financieros históricos y **Alpaca** como broker para ejecutar órdenes de compra y venta. El caso de uso demostrado es el seguimiento de acciones de Apple (AAPL), aunque el enfoque es extrapolable a Forex, criptomonedas o cualquier otro activo financiero.

La lógica de trading implementada es el **cruce de medias móviles**: si la media móvil de 20 sesiones cruza por encima de la de 50, se compra; si ocurre lo contrario, se vende; si no hay cruce, no se ejecuta ninguna acción. Antes de abrir una posición, el bot verifica que no exista ya una operación abierta sobre el mismo símbolo, evitando duplicaciones.

El video también cubre el proceso de validación completo usando la cuenta de **Paper Trading** de Alpaca (capital ficticio), comprobando conexión con el broker, estado del mercado, consulta de posiciones abiertas y ejecución/cancelación de órdenes de prueba antes de lanzar el bot real.


### `videos/Cómo_utilizar_Python_y_Alpaca_para_crear_un_sistema_de_Tradi.md`

**Conclusiones y Aprendizajes**

- **Integración rápida con brokers vía SDK:** El patrón de autenticar con API Key + Secret y usar un SDK oficial es directamente aplicable a otros brokers/proveedores (Interactive Brokers, Binance, etc.).
- **Pipeline de datos financieros:** El flujo `API → iteración → DataFrame → visualización` es el esquema base para cualquier sistema de análisis cuantitativo.
- **Paper Trading como entorno de staging:** Usar la cuenta Paper equivale a tener un entorno de staging antes de pasar a producción real; es buena práctica antes de operar con capital real.
- **Plotly para dashboards financieros:** La librería es adecuada para construir interfaces de monitoreo de estrategias de trading con gráficos interactivos.
- **Separación de credenciales:** Las API Keys nunca deben hardcodearse en el código; se recomienda usar variables de entorno o archivos `.env` (el video las pone en variables de Python como paso introductorio).
- **Ejecución local para producción:** Google Colab es válido para prototipado, pero un sistema de trading automático real debe ejecutarse en un entorno local o servidor dedicado.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video explica cómo conectarse a la API de Alpaca Markets usando Python para extraer datos históricos de precios de activos financieros (acciones, criptomonedas). Se cubre el proceso completo desde la creación de la cuenta en Alpaca (modo Paper/demo), la obtención de las API Keys, hasta la instalación del SDK oficial `alpaca-trade-api`.

Una vez obtenidos los datos, se demuestra cómo estructurarlos en un DataFrame de Pandas con columnas OHLC (Open, High, Low, Close) y cómo visualizarlos mediante un gráfico de velas (candlestick chart) utilizando la librería Plotly. El ejemplo práctico usa el ticker de Apple (AAPL) con temporalidad diaria.

Todo el flujo se ejecuta en Google Colab, aunque se menciona que para la interactividad completa de los gráficos Plotly (zoom, pan) es necesario ejecutar el código en un entorno local como Visual Studio Code.


### `videos/Freqtrade_vs_HummingBot_vs_Backtrader_Review_2026_Backtestin.md`

**Conclusiones y Aprendizajes**

- **Para proyectos de trading sistemático en cripto con estrategias de tendencia:** Freqtrade es el punto de entrada más accesible; su base Python y su interfaz web permiten iterar rápidamente sin expertise avanzado.
- **Para sistemas de provisión de liquidez o arbitraje entre exchanges:** HummingBot es la opción técnicamente más adecuada, aunque requiere comprensión profunda de microestructura de mercado.
- **Para validación de estrategias antes de producción:** Backtrader debe usarse como entorno de laboratorio obligatorio; ninguna estrategia debería ir a live trading sin pasar por backtesting exhaustivo.
- **Principio de diseño aplicable:** separar la fase de investigación (Backtrader) de la fase de ejecución (Freqtrade/HummingBot) es una arquitectura de desarrollo de estrategias más robusta.
- **Gestión del riesgo técnico:** elegir una herramienta que el equipo pueda mantener y auditar es tan importante como su rendimiento teórico.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video presenta una comparativa de tres plataformas de trading automatizado —Freqtrade, HummingBot y Backtrader— orientada a ayudar al usuario a elegir la herramienta que mejor se adapta a su perfil y objetivos. El argumento central es que el trading automatizado ya no es una cuestión de suerte, sino de tener el sistema correcto que elimine las decisiones emocionales y ejecute estrategias con lógica y código.

Cada plataforma representa un arquetipo de trader distinto: Freqtrade para el seguidor de tendencias en cripto, HummingBot para el operador activo de alta frecuencia y arbitraje, y Backtrader para el investigador que necesita validar estrategias con datos históricos antes de arriesgar capital real. El video no profundiza técnicamente en ninguna de las tres, sino que ofrece una visión de alto nivel orientada al posicionamiento estratégico.

La conclusión principal es que no existe una herramienta universalmente superior: la elección correcta depende de la personalidad del trader, su tolerancia al riesgo, su conocimiento técnico y el mercado en el que opera. Se enfatiza aprender a fondo la herramienta elegida y probar las estrategias hasta que sean sólidas antes de operar con capital real.


### `videos/How_I_Develop_Trading_Strategies_Permutation_Tests_and_Tradi.md`

**Conclusiones y Aprendizajes**

**Aplicables directamente en proyectos de trading algorítmico:**

1. **Implementar bar-level returns como estándar:** En lugar de calcular métricas por trade, calcular retornos multiplicando el vector de posición por los retornos del siguiente bar. Esto estabiliza cualquier objective function.

2. **Implementar el pipeline de 4 pasos como checklist obligatorio** antes de considerar live trading cualquier estrategia: no avanzar al siguiente paso si el anterior falla.

3. **Codificar el bar permutation algorithm** como utilidad reutilizable: shuffle separado de intrabar quantities y gaps, preservando el open del primer bar y el close del último (tendencia general intacta).

4. **Usar P-value < 1% como filtro de entrada** para el in-sample permutation test, pero no como target a optimizar; si se manipula la estrategia para pasar el test, el test pierde validez.

5. **Separar el dataset de validación final y no tocarlo** hasta tener estrategias que pasaron ambos permutation tests; cada comparación sobre ese dataset acumula selection bias.

6. **En walk forward:** reoptimizar con la frecuencia máxima que permita el tiempo de cómputo; el autor usa 30 días con una ventana de entrenamiento de 4 años.

7. **Para estrategias con lookbacks:** en lugar de optimizar el lookback, buscar la zona de estabilidad del parámetro (donde un rango amplio funciona) y fijar un valor razonable dentro de esa zona.

**Resumen Ejecutivo**

El video presenta un framework de cuatro pasos para desarrollar y validar estrategias de trading algorítmico, usando como ejemplo la estrategia Donchian Channel Breakout sobre datos horarios de Bitcoin. Los cuatro pasos son: (1) excelencia in-sample, (2) in-sample Monte Carlo permutation test, (3) walk forward test, y (4) walk forward Monte Carlo permutation test. El autor enfatiza que este proceso es genérico y aplicable a casi cualquier estrategia, desde simples cruces de medias móviles hasta redes neuronales complejas.

El concepto central es el uso de **permutation tests** para distinguir si la buena performance in-sample de una estrategia proviene de patrones reales en los datos o simplemente de data mining bias. La idea clave: si una estrategia optimizada lo hace tan bien —o mejor— sobre datos permutados (ruido con propiedades estadísticas similares al original) como sobre los datos reales, entonces la estrategia probablemente es basura. El null hypothesis es que la estrategia no tiene valor, y el permutation test es el mecanismo para rechazarlo.

El autor también articula por qué no basta con probar en datos out-of-sample directamente: cada vez que se reutiliza un dataset de validación para comparar estrategias, se acumula selection bias, corrompiendo gradualmente lo que se considera "out of sample". El permutation test funciona como un filtro previo que consume resources computacionales pero preserva la integridad del dataset de validación real.


### `videos/How_to_Build_a_Trading_Bot_in_Python_Full_Algorithmic_Tradin.md`

**Conclusiones y Aprendizajes**

- **Separar credenciales del código**: usar `config.py` o variables de entorno es una práctica esencial antes de hacer cualquier commit o compartir el código.
- **Filtrar velas incompletas**: siempre verificar el flag `complete` al consumir datos en tiempo real; ignorarlo causa que los indicadores calculados sean incorrectos (repintado).
- **Índices negativos en pandas**: `df.iloc[-1]` y `df.iloc[-2]` son el patrón correcto para acceder a las últimas N filas sin conocer el tamaño del DataFrame.
- **Formateo de precios por instrumento**: cada par/activo tiene una precisión decimal diferente; el bot debe formatearla dinámicamente para evitar errores de la API.
- **Loop con módulo para sincronización temporal**: `datetime.now().minute % interval == 0` es un patrón reutilizable para ejecutar lógica en intervalos fijos sin usar schedulers externos.
- **Flag `last_checked`**: patrón simple para evitar ejecuciones duplicadas dentro del mismo intervalo temporal en un loop `while True`.
- **Arquitectura modular por funciones**: separar `get_candles()`, `calculate_indicators()`, `ema_crossover()`, `place_order()` y `run_bot()` facilita el testing, mantenimiento y extensión del bot.
- **Take-profit dinámico con ratio fijo**: calcular TP como `entry + (entry - stop_loss) × ratio` es un patrón escalable para cualquier estrategia con gestión de riesgo basada en R múltiplos.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video presenta un tutorial completo para construir un trading bot automatizado en Python desde cero, aplicable a stocks, forex y criptomonedas. El instructor utiliza el broker OANDA con su API oficial y el wrapper Python `oandapyV20` para establecer la conexión, descargar datos históricos de velas (OHLC), calcular indicadores técnicos y ejecutar órdenes de mercado de forma automática.

La estrategia implementada es un cruce de EMAs (5 y 8 períodos) con stop-loss basado en ATR (14 períodos) y take-profit con ratio 1.5:1. El bot detecta el cruce en las dos velas más recientes completas, calcula los niveles de entrada/stop/target y envía la orden directamente a la cuenta del broker mediante la API.

Para la automatización continua, el bot corre dentro de un bucle `while True` con lógica temporal basada en módulo para detectar el inicio de cada nueva vela (cada 15 minutos), evitando consultas redundantes a la API y controlando el ritmo con `time.sleep(1)`.


### `videos/I_Built_an_AI_Agent_to_Find_Hidden_Polymarket_Alpha_Claude_C.md`

**Conclusiones y Aprendizajes**

- **Prompting estratégico para APIs**: Especificar explícitamente el endpoint (`Gamma API`) y el formato de datos (`every trade not bucketed`) en el prompt evita que el agente tome atajos que degraden la calidad del output.
- **Visualización interactiva como herramienta de QA**: Incluir hover/tooltip en el requerimiento permite verificar que los datos son correctos, especialmente en zonas de alta densidad de puntos.
- **Patrón de desarrollo vibe-coding para herramientas de análisis**: Un prompt bien estructurado (fuente de datos + formato + tipo de gráfico + interactividad) es suficiente para obtener una herramienta funcional sin iteraciones múltiples.
- **Arbitraje de información**: Las ineficiencias de UI de plataformas establecidas crean oportunidades para traders técnicos; construir herramientas propias de visualización es una fuente de ventaja competitiva sostenible.
- **Aplicable a cualquier mercado con API pública**: La misma técnica funciona para Kalshi, mercados de opciones, o cualquier fuente de datos con trades individuales accesibles vía API.
- **Tamaño de círculo como encoding de volumen**: Mejor que barras separadas para detectar clusters de volumen en contexto de precio; técnica replicable en cualquier scatter plot financiero.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video muestra cómo usar Claude Code (el agente de IA de Anthropic) para construir una herramienta de visualización de datos de mercados de predicción (Polymarket/Kalshi) que revela información oculta que las interfaces nativas no muestran. El problema central es que los gráficos oficiales de Polymarket agregan ("bucketean") los datos, ocultando movimientos de precio reales, picos de volatilidad y patrones de volumen que son críticos para tomar decisiones de trading informadas.

El autor demuestra en tiempo real cómo, con un único prompt en Claude Code, se genera un script Python (`visualize_market.py`) que consulta la API Gamma de Polymarket, obtiene cada trade individual sin agregar, y produce una visualización interactiva con scatter plot de precios (incluyendo VWAP) y barras de volumen diferenciadas por compra/venta. El resultado revela información que cambia completamente la lectura del mercado: por ejemplo, un mercado que parece haber ido directo a 100% en el gráfico nativo, en realidad tuvo swings de 50 a 77, bajó a 50 y luego subió progresivamente.

La conclusión clave es que, dado que los datos de Polymarket viven en blockchain y son públicos, cualquier trader puede construir estas herramientas con AI sin experiencia en programación, creando una ventaja informacional real sobre quienes solo usan la interfaz oficial.


### `videos/I_Built_an_AI_Bot_That_Reads_Market_News_and_Predicts_Sentim.md`

**Conclusiones y Aprendizajes**

- **Pipeline replicable**: El flujo `queries → scraping Google → extracción de títulos → análisis NLP → score consolidado` es directo de implementar en cualquier proyecto de market intelligence.
- **Swap de modelos sin fricción**: La arquitectura separa la función `analyze_sentiment` del resto, lo que permite cambiar VADER por FinBERT (o cualquier LLM) sin tocar el pipeline principal.
- **Granularidad ajustable**: Analizar solo títulos es el modo rápido; escalar a contenido completo del artículo mejora la señal a costa de tiempo de scraping.
- **Extensible a múltiples activos**: Reemplazar los keywords de `queries` permite monitorizar oil, índices, crypto o acciones individuales sin cambiar ninguna otra lógica.
- **Automatización trivial**: Agregar un scheduler (APScheduler o cron) convierte el script en un sistema de alertas diarias de sentimiento de mercado.
- **Consideración de producción**: Para uso real, conviene manejar rate limits de Google scraping (usar APIs como NewsAPI o Alpha Vantage como alternativa más estable), y añadir deduplicación de artículos entre queries.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video presenta un bot en Python que realiza análisis de sentimiento sobre noticias financieras en tiempo real, orientado a traders que quieren cuantificar el tono del mercado antes de operar. El sistema busca artículos usando consultas predefinidas (ej: "gold market", "gold price"), extrae los títulos mediante web scraping con BeautifulSoup y Google RSS, y los procesa con dos modelos de NLP: VADER (léxico) y FinBERT (deep learning entrenado en datos financieros).

El resultado final es una distribución de frecuencias entre sentimientos positivos, negativos y neutrales, más un score numérico consolidado: valores positivos indican sesgo alcista y negativos indican sesgo bajista. En el ejemplo en vivo del video, de 70 artículos sobre oro, el 30% resultó positivo, 21% negativo y 48% neutral.

El bot está diseñado para ejecutarse de forma programada (ej: cron job diario) antes de sesiones de trading, actuando como señal auxiliar de decisión basada en el sentimiento colectivo de las noticias del día.


### `videos/I_Gave_My_Terrible_Trading_Bot_10000_to_Trade_Stocks.md`

**Conclusiones y Aprendizajes**

- **El backtesting es imprescindible pero no suficiente**: validar con datos históricos es el primer paso, pero los costes de producción (suscripciones, comisiones) pueden invalidar una estrategia que en papel era rentable
- **Calcular el TCO real antes de hacer deploy**: las APIs de noticias, los datos de mercado en tiempo real y las comisiones del broker son costes fijos que deben considerarse como parte del presupuesto del proyecto, no como extras
- **Los embeddings vectoriales son una herramienta versátil**: en este proyecto se usan tanto para búsqueda semántica de empresas como para matching de letras, lo que demuestra que la misma infraestructura vectorial puede resolver múltiples problemas de similaridad en un mismo proyecto
- **Separar la lógica de estrategia de la lógica de broker**: el patrón de backtestear primero y luego "convertir a código de Interactive Brokers" permite iterar rápido sin arriesgar dinero real
- **La optimización de hiperparámetros en trading es computacionalmente costosa**: para proyectos de producción, considerar frameworks más eficientes (Optuna, Ray Tune) en lugar de búsqueda exhaustiva
- **Los wrappers open-source sobre APIs deficientes son válidos en producción**: aceptable usar librerías comunitarias cuando la API oficial es difícil de usar, pero hay que evaluar su mantenimiento
- **El acceso a datos es frecuentemente el cuello de botella y el mayor coste** en proyectos de datos en tiempo real; siempre investigar precios antes de diseñar la arquitectura

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

Lewis construye tres trading bots con estrategias radicalmente distintas y los pone a operar con $10,000 reales durante 3-4 días. El primer bot combina momentum trading y análisis de valor (ratio P/E + media móvil) sobre un conjunto predefinido de acciones seguras. El segundo bot escanea noticias en tiempo real, vectoriza descripciones de empresas para identificar qué stock se ve afectado por cada artículo, y compra o vende según el sentimiento. El tercero —llamado "Swift Trade 1.0"— elige un stock aleatorio, busca noticias recientes, las compara con letras de Taylor Swift mediante búsqueda vectorial, y decide si comprar o vender según si la letra más similar tiene sentimiento positivo o negativo.

El proceso técnico cubre backtesting con optimización de parámetros, integración con el broker Interactive Brokers vía una librería open-source de Python, uso de una base de datos vectorial (DataStax Astra DB sobre Cassandra) para almacenar embeddings de descripciones de empresas y letras de canciones, y análisis de sentimiento con modelos de ML. Tras 3-4 días de operación real, los tres bots combinados generaron $109.35 brutos, pero tras comisiones y suscripciones a datos de mercado ($117.70), el resultado neto fue una pérdida de $8.35.

El video ilustra de forma práctica el ciclo completo de un proyecto de automatización financiera: ideación de estrategia → backtesting → optimización de parámetros → integración con API de broker → despliegue en producción, con todos los problemas reales que eso conlleva (APIs cerradas, costes de datos, bugs en producción).


### `videos/Introduction_to_BACKTRADER_Backtesting_Trading_Strategies_Li.md`

**Conclusiones y Aprendizajes**

- **Estructura mínima reproducible:** Para cualquier backtest en Backtrader se necesitan exactamente 4 pasos: `cerebro = bt.Cerebro()` → `cerebro.adddata()` → `cerebro.addstrategy()` → `cerebro.run()`. Esto es aplicable directamente en cualquier proyecto.
- **Gestión de posición desde el primer día:** Configurar un `PercentSizer` es trivial y tiene impacto enorme en los resultados; no hacerlo (quedándose con 1 acción por defecto) produce resultados engañosamente bajos.
- **Comisiones son obligatorias en backtest realistas:** Ignorarlas sobreestima el rendimiento; agregarlas con `setcommission` es una línea de código.
- **El patrón `notify_order` + `bar_executed`** es el mecanismo estándar para implementar lógica post-ejecución (stop-loss, take-profit, holding periods) y debe entenderse antes de construir estrategias más complejas.
- **Los Analyzers desacoplan la lógica de evaluación:** Permiten extraer métricas sin modificar la estrategia, facilitando la comparación entre estrategias.
- **Visualización automática:** `cerebro.plot()` genera gráficos con equity curve, señales de entrada/salida e indicadores sin configuración adicional, útil para validación rápida.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video es una introducción práctica a **Backtrader**, una librería de Python para hacer backtesting de estrategias de trading. El instructor parte desde cero: instalación, instanciación del objeto central (`Cerebro`), carga de datos con `yfinance`, y ejecución de una primera estrategia de cruce de medias móviles (SMA Crossover). Todo el código se trabaja en Jupyter Notebook con visualizaciones incluidas.

A lo largo del video se explican los bloques fundamentales de Backtrader: el objeto `Cerebro` como orquestador, las clases de estrategia que heredan de `bt.Strategy`, los métodos `__init__` (indicadores) y `next` (lógica de trading), los `Sizers` para gestión de posición, las comisiones del broker y los `Analyzers` para métricas como retorno anual. Se cubre también el ejemplo oficial del *quick start guide* de la documentación.

La parte más técnica del video explica cómo Backtrader trabaja con una lógica iterativa basada en "barras" (filas del DataFrame), lo que es crucial para entender el manejo de órdenes, el estado de ejecución (`order status`) y la implementación de períodos mínimos de tenencia de activos mediante el seguimiento del índice de barra actual.


### `videos/Nuestra_PRIMERA_ESTRATEGIA_de_TRADING_en_Python_Parte_2.md`

**Conclusiones y Aprendizajes**

- **Modularización del código**: separar los cálculos de indicadores en ficheros independientes (p.ej. `medias_moviles.py`) mejora la mantenibilidad y permite reutilizar funciones en distintas estrategias.
- **Parametrización de estrategias**: las funciones deben aceptar parámetros configurables (tipo de media, periodos corto/largo) para facilitar la experimentación sin modificar el código base.
- **No depender de un solo indicador**: arquitectura del bot diseñada para combinar múltiples señales antes de tomar decisiones, reduciendo falsos positivos.
- **Pipeline de análisis técnico**: el patrón `descargar datos → calcular indicadores → detectar señales → visualizar` es reutilizable para cualquier indicador técnico adicional.
- **Iteración sobre un universo de activos**: leer el scope desde un fichero externo permite cambiar los activos analizados sin tocar el código, lo que es una buena práctica para sistemas de screening.
- **Visualización como herramienta de validación**: representar gráficamente las señales generadas es clave para verificar que la lógica implementada es correcta antes de automatizar decisiones.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

Este vídeo es el quinto de una serie en la que se construye un bot de trading algorítmico en Python. En esta entrega se introduce el análisis técnico automatizado, comenzando por el cálculo e interpretación de medias móviles como indicadores de tendencia. El presentador explica la lógica detrás de la estrategia más clásica basada en medias móviles: el Golden Cross y el Death Cross, y muestra cómo implementarla en código Python.

Se desarrolla un módulo separado (`medias_moviles.py`) que contiene funciones reutilizables para calcular los tres tipos de medias móviles (simple, exponencial y acumulativa), así como una función `golden_and_death_crosses` que detecta automáticamente los puntos de cruce entre la media móvil de corto y largo plazo. Los resultados se visualizan sobre el gráfico de precios con triángulos de colores que marcan cada señal alcista o bajista.

El presentador muestra ejemplos reales con Bitcoin, Ethereum y acciones como Microsoft, recalcando que la estrategia es útil pero no infalible, y que su potencia real emerge cuando se combina con otros indicadores técnicos como RSI, MACD, bandas de Bollinger o soportes y resistencias. El vídeo cierra estableciendo la hoja de ruta de los próximos episodios donde se irán añadiendo más herramientas de análisis técnico.


### `videos/Polymarket_5_Min_Claude_Code_Bot_are_NUTS.md`

**Conclusiones y Aprendizajes**

1. **Framework de backtesting para mercados de ventana fija:** El patrón precio-inicio como benchmark es directo de implementar. En cualquier mercado con resolución por comparación de precio inicial vs final, el backtest se reduce a: obtener precio en T=0, obtener precio en T=N, comparar con la señal predicha.

2. **CVD como feature de ML/trading:** Implementar un acumulador de CVD sobre tick data es relativamente sencillo — iterar sobre trades, sumar volumen si es buy, restar si es sell. Puede usarse como feature adicional en modelos predictivos donde OHLCV no es suficiente.

3. **Tick data vs OHLCV:** Para estrategias de alta frecuencia (5 min o menos), considerar seriamente incorporar tick data como fuente de señales. La información intra-barra puede ser la diferencia entre una estrategia con edge real y una sin ella.

4. **Validación de estrategias:** El autor menciona explícitamente walk-forward y stress test además del backtest simple. En proyectos de bots, no basta con backtest in-sample; implementar validación out-of-sample es crítico antes de live trading.

5. **Alta frecuencia de señales = ventaja estadística:** 288 trades/día significa que una estrategia con 60% win rate tiene resultados estadísticamente significativos mucho más rápido que en mercados diarios. Esto hace que Polymarket 5-min sea un buen laboratorio de experimentación.

6. **Usar Claude Code para construcción rápida de bots:** El workflow mostrado (idea → backtest con Claude Code → automatización) es un pipeline replicable para cualquier proyecto de trading algorítmico.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video muestra cómo Moon Dev está construyendo bots de trading automatizados para los mercados de 5 minutos de Polymarket, utilizando Claude Code como asistente de desarrollo. El creador exhibe resultados de sus bots operando 24/7 con ganancias del 150% al 669% en operaciones individuales mientras dormía, destacando la ventaja de automatizar frente al trading emocional manual.

El punto central técnico del video es el descubrimiento de cómo hacer **backtesting en los mercados de 5 minutos de Polymarket**: la clave está en obtener datos de 1 minuto y usar el precio al inicio de cada ventana de 5 minutos como "precio a vencer", luego verificar si el precio al final del período lo superó o no. A partir de este framework, el autor probó múltiples estrategias y encontró tres con resultados positivos, entre ellas una basada en MACD (3, 15, 3) con 60% de win rate en 104,000 trades anuales.

El segundo concepto técnico relevante es el uso de **CVD (Cumulative Volume Delta)** calculado a partir de **tick data** (cada cambio de precio individual), en contraste con los típicos datos OHLCV de 1 o 5 minutos. El autor argumenta que toda la alpha real está en el tick data y en el análisis de flujo de órdenes, información que los datos de barras convencionales ocultan.


### `videos/Se_LIBERÓ_Crea_un_TRADING_BOT_para_POLYMARKET_con_HERMES_Age.md`

**Conclusiones y Aprendizajes**

- **Patrón de agente semi-autónomo**: separar la capa de análisis/investigación (automatizada) de la capa de ejecución (humana) es una arquitectura de bajo riesgo aplicable a cualquier dominio que requiera toma de decisiones con datos externos.
- **Deployment en VPS con Docker**: correr agentes LLM en contenedores aislados en un VPS es la práctica recomendada para proyectos que manejan credenciales sensibles o necesitan disponibilidad 24/7.
- **Cron job + Telegram como pipeline de entrega**: la combinación cron → script de análisis → Telegram bot es un patrón reutilizable para cualquier sistema de alertas o señales automatizadas.
- **Gestión de API keys**: nunca integrar claves directamente en el chat del agente; usar variables de entorno o gestores de secretos. El video menciona esto como punto de atención de seguridad.
- **Selección de modelo por tarea**: para tareas de análisis/filtrado con alto volumen de llamadas, GPT-4o mini ofrece un equilibrio óptimo; reservar modelos más potentes (GPT-5.5) para casos donde la calidad del razonamiento es crítica.
- **Tailscale como capa de seguridad**: alternativa a exponer SSH público, ideal para proyectos con acceso remoto frecuente a servidores personales.
- **Knowledge graph como memoria del agente**: añadir contexto histórico estructurado mejora significativamente la calidad de decisiones en agentes que operan sobre dominios repetitivos (mercados, tendencias, etc.).

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video muestra cómo integrar **Hermes Agent** (plataforma agéntica de IA de código abierto) con **Polymarket** (mercado de predicciones descentralizado) para construir un bot de trading inteligente sin necesidad de escribir código manualmente. El flujo consiste en usar Hermes como agente de investigación autónomo que escanea mercados públicos de Polymarket, analiza posiciones con un LLM (OpenAI GPT), filtra oportunidades de bajo riesgo y entrega señales al usuario para que sea él quien tome la decisión final de inversión.

El autor enfatiza que la arquitectura es deliberadamente semi-autónoma: el agente **no abre posiciones por sí solo**, sino que actúa como capa de inteligencia y filtrado para reducir incertidumbre. Para desplegar el sistema de forma segura y disponible 24/7, recomienda un VPS de Hostinger con Hermes corriendo en Docker, reforzado con Tailscale para acceso seguro. La entrega de señales se automatiza mediante un **cron job** que envía resultados vía Telegram cada 6 horas, eliminando la necesidad de estar frente al ordenador.

El video también menciona posibles mejoras como añadir un **knowledge graph** para contextualizar mercados históricos, la posibilidad de un segundo agente que ejecute las operaciones automáticamente, y la integración con otros modelos más potentes como GPT-4o, GPT-4 mini o GPT-5.5 según el balance entre coste y calidad de análisis.


### `videos/Supertrend_MACD_RSI_Strategy_Backtest_299_Profit_Using_Pytho.md`

**Conclusiones y Aprendizajes**

**Aplicables directamente a un proyecto de trading algorítmico:**

1. **Estructura de triple confirmación:** Implementar un sistema donde señales de múltiples indicadores deben coincidir reduce las entradas falsas. Patrón replicable con cualquier combinación de indicadores.

2. **Gestión de riesgo basada en estructura de mercado:** Colocar el stop-loss en swing highs/lows en lugar de porcentajes fijos adapta el riesgo a la volatilidad actual del activo.

3. **Pipeline de optimización riguroso:** El split in-sample/out-of-sample es una práctica fundamental para cualquier sistema backtestado; debe ser siempre la metodología base antes de considerar un sistema como válido.

4. **Filtro de tamaño de vela:** Añadir un filtro que descarte entradas en velas de gran tamaño es una técnica simple y efectiva para mejorar la calidad del entry.

5. **RSI como filtro de sesgo:** Usar el nivel 50 del RSI como filtro binario (bullish/bearish) es un uso no convencional pero limpio para alinear trades con el momentum dominante.

6. **Freqtrade como infraestructura:** Para proyectos de trading en Python, Freqtrade ofrece backtesting, optimización (HyperOpt) y ejecución en vivo en un solo framework open-source, eliminando la necesidad de construir esa infraestructura desde cero.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video presenta una estrategia de trading algorítmico que combina tres indicadores técnicos: Supertrend, MACD y RSI. La estrategia es codificada en Python e implementada sobre el framework Freqtrade (bot de trading crypto open-source), donde se optimizan sus parámetros mediante la funcionalidad HyperOpt para maximizar el rendimiento minimizando el drawdown.

El proceso de validación sigue una metodología in-sample/out-of-sample: 8 meses de datos históricos para optimización y 4 meses para validación en datos no vistos, buscando evitar overfitting. El backtest se ejecutó sobre DOT perpetual futures en timeframe de 1 hora con un período total de 1 año.

Los resultados reportados muestran un rendimiento del 299% de ganancia total durante un período en que el activo subyacente cayó un 55%, con un drawdown máximo del 23% y una curva de equity con tendencia alcista sostenida. La estrategia usa gestión de riesgo basada en swing points para stop-loss y un ratio riesgo/recompensa de 1.5:1 para take-profit.


### `videos/Using_the_New_Hermes_Agent_to_Track_Polymarket_Smart_Money.md`

**Conclusiones y Aprendizajes**

- **Agentes con transparencia de ejecución son más debuggeables**: Al construir pipelines de agentes, exponer los pasos intermedios (logs de acciones) facilita identificar fallos y comportamientos no deseados.
- **Memoria persistente como feature de producción**: Para tareas repetitivas o pipelines de trading, un agente que convierte instrucciones en skills reutilizables reduce la necesidad de re-prompting y mejora la fiabilidad.
- **Instalación y onboarding importan**: Hermes Agent demuestra que un buen script de instalación one-click puede ser un diferenciador real frente a alternativas más complejas.
- **Patrón de uso concreto aplicable**: Configurar un cron job dentro del agente para scraping periódico de datos públicos (leaderboards, wallets) + análisis + notificación es un pipeline replicable para cualquier fuente de datos pública con transparencia on-chain.
- **Gestión de rate limits**: Seleccionar el tier correcto del modelo (Sonnet vs Opus) según la carga de trabajo es crítico para evitar interrupciones en producción.
- **Flujo de investigación de estrategias**: Usar agentes para identificar → analizar → backtest → paper trade → producción es un framework aplicable a cualquier sistema de trading algorítmico.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code

**Resumen Ejecutivo**

El video presenta Hermes Agent, un agente de IA con ~21,000 estrellas en GitHub, utilizado para automatizar el seguimiento de traders rentables en Polymarket. El autor lo configura para analizar el leaderboard de Polymarket, extraer las estrategias de los wallets más rentables y enviar actualizaciones periódicas (cada 7 minutos) vía terminal, sin necesidad de revisar manualmente los trades.

Se compara Hermes Agent con su competidor principal Open Claw (presumiblemente Claude/Anthropic's Computer Use), destacando tres ventajas clave: mayor transparencia en la ejecución de pasos, mejor memoria persistente y mejora autónoma de habilidades, y mayor facilidad de instalación (5-10 minutos desde cero). El autor usa el modelo Sonnet de Anthropic como backend tras encontrar rate limiting con Opus (error 529).

El caso de uso concreto mostrado es un sistema de análisis de wallets de Polymarket que extrae la estrategia de trading de cada trader rentable, como el ejemplo de un trader que usa el precio overnight del SPX para decidir entradas y salidas, con ganancias de ~$25K totales y ~$15K en el último mes.


## Decisiones extraídas para el MVP

1. Construir primero un agente **read-only** de investigación; no ejecución autónoma.

2. Separar claramente cliente Polymarket, persistencia SQLite, scoring y notificación.

3. Usar SQLite con WAL desde el primer momento para señales, mercados y perfiles.

4. Implementar backoff/rate limiting incluso si los límites públicos son generosos.

5. Usar scoring multi-criterio explicable con umbral inicial conservador, no caja negra.

6. Diseñar para paper trading antes de dinero real.

7. Mantener human-in-the-loop para cualquier paso que pueda tocar capital.

8. No meter credenciales reales en repo; solo `.env.example`.

9. Crear tests desde el inicio para cliente parsing, DB y scoring.
