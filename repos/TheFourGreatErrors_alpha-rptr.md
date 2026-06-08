# alpha-rptr

## Información General
- **Repo:** `TheFourGreatErrors/alpha-rptr`
- **URL:** https://github.com/TheFourGreatErrors/alpha-rptr
- **Lenguaje principal:** Python
- **Stars:** 669
- **Última actualización:** 2026-04-28
- **Topics:** algo, algorithmic-trading, binance, binance-futures, bitcoin, bitmex, bot, bybit, crypto, cryptocurrency, ftx, ftx-exchange, python, quantitative-trading, trading, trading-bot, trading-systems, websocket

## Propósito del Repo
alpha-rptr es un sistema de trading algorítmico automatizado diseñado para operar en múltiples exchanges de criptomonedas (Binance Futures, Bybit, BitMEX y FTX). Su objetivo central es minimizar las discrepancias entre los entornos simulados y el trading en vivo, permitiendo transiciones fluidas entre backtesting, paper trading y producción con cambios mínimos en el código de estrategia.

Está diseñado para traders algorítmicos con conocimientos básicos de trading que quieran desarrollar, testear y desplegar estrategias propias. Lo que lo diferencia es la unificación de múltiples modos de ejecución (backtest, hyperopt, stub/paper, demo y producción) bajo la misma interfaz de estrategia, junto con un extenso catálogo de indicadores técnicos y tipos de órdenes avanzados.

## Arquitectura y Patrones Clave
El sistema utiliza un patrón **Factory + Strategy** bien definido: `src/factory.py` instancia el exchange y la estrategia correctos según la configuración, mientras que cada estrategia hereda de una clase base común definida en `src/bot.py`. Los exchanges se encapsulan como módulos independientes en `src/exchange/`, cada uno implementando la misma interfaz (órdenes, posiciones, cuenta), lo que permite intercambiarlos sin modificar la estrategia.

Para backtesting y paper trading existe un patrón **Adapter/Stub**: `src/exchange/backtest.py` y `src/exchange/stub.py` replican la interfaz de los exchanges reales, garantizando que el mismo código de estrategia funcione en todos los modos. La comunicación en tiempo real con los exchanges se realiza via **WebSocket**, y hay integración con **InfluxDB** para persistencia de métricas y monitorización. Se incluye un frontend HTML/JS (`html/`) para visualización de resultados.

## Componentes Principales
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

## Dependencias Clave
- **`ta-lib`** — Biblioteca C de indicadores técnicos (envuelta en Python); núcleo del módulo `indicators.py`
- **`pandas` / `numpy`** — Manipulación de series temporales y cálculos vectorizados
- **`scipy` / `scikit-learn`** — Regresión, normalización y funciones estadísticas para indicadores avanzados
- **`hyperopt`** — Optimización bayesiana de hiperparámetros de estrategias (modo hyperopt)
- **`websocket-client`** — Conexiones WebSocket a los exchanges en tiempo real
- **`pybit`** — SDK oficial de Bybit para Python
- **`bravado`** — Cliente REST para la API de BitMEX (basado en Swagger)
- **`influxdb-client`** — Persistencia de métricas de trading en InfluxDB para monitorización
- **`discord-webhook`** — Notificaciones de eventos de trading vía Discord
- **`google-api-python-client` / `oauth2client`** — Integración con Gmail para recepción de señales
- **`matplotlib`** — Generación de gráficos (ej. plots de estrategias como `plt_MACDLongOnly.PNG`)
- **`PyQt6`** — Interfaz gráfica de escritorio (opcional)
- **`pycryptodome`** — Firma criptográfica de requests a los exchanges

## Fragmentos de Código Relevantes

**1. Comando de arranque (Dockerfile CMD) — muestra la interfaz CLI unificada:**
```bash
python3 main.py --test --account binanceaccount1 --exchange binance --pair BTCUSDT --strategy Sample
```
El mismo comando con `--live` ejecuta en producción; con `--backtest` ejecuta replay histórico. La estrategia no cambia.

**2. Estructura de modos de ejecución disponibles:**
```
Modos soportados por main.py:
  --production  → Trade Mode en vivo
  --demo        → Demo Trade Mode (cuenta demo del exchange)
  --test        → Stub Trade (paper trading con datos reales)
  --backtest    → Replay sobre datos históricos
  --hyperopt    → Optimización de hiperparámetros con hyperopt
```

**3. Stack de dependencias que refleja el diseño multicapa:**
```
# requirements.txt — capas del sistema
matplotlib, numpy, scipy          # cómputo numérico y visualización
ta-lib, pandas, pyti              # indicadores técnicos
scikit-learn, hyperopt            # ML y optimización
websocket-client, pybit, bravado  # conectores de exchange
influxdb-client                   # persistencia de métricas
discord-webhook, google-api       # notificaciones y señales externas
PyQt6                             # UI de escritorio opcional
```

## Conclusiones y Aprendizajes
1. **Patrón Strategy + Factory con interfaz unificada de exchange**: separar la lógica de negocio (estrategia) de la implementación del exchange mediante una interfaz común es el patrón central que permite reutilizar código entre backtest, paper y producción sin modificaciones.
2. **Stub/Adapter para simulación**: implementar un exchange "falso" (`stub.py`, `backtest.py`) que respeta la misma interfaz que los exchanges reales es una técnica directamente adoptable para testear sistemas event-driven sin dependencias externas.
3. **Modo hyperopt integrado**: incorporar optimización bayesiana de hiperparámetros como un modo más del CLI (no como herramienta separada) simplifica el flujo de desarrollo de estrategias y es una decisión de diseño replicable.
4. **Separación clara de configuración**: tener `config.py` (sistema) y `exchange_config.py` (por exchange) permite escalar a nuevos exchanges sin tocar la lógica central.
5. **WebSocket + monitorización persistente**: el uso de WebSocket para todos los exchanges con un módulo de monitor dedicado y InfluxDB como backend de métricas es un patrón maduro para sistemas de trading en tiempo real.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code