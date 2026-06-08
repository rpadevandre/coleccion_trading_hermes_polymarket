# BOT DE TRADING V5.0

## Información General
- **Repo:** `TradeAIcode/BOT-DE-TRADING`
- **URL:** https://github.com/TradeAIcode/BOT-DE-TRADING
- **Lenguaje principal:** Python
- **Stars:** 1
- **Última actualización:** 2025-04-28
- **Topics:** automated-trading-strategies, crypto, crypto-trading, cryptocurrency, market-bot, pyqt5, python, trading, tradingbot

## Propósito del Repo
BOT DE TRADING V5.0 es una aplicación de escritorio para trading automático de criptomonedas, diseñada para traders que desean automatizar sus operaciones sin necesidad de conocimientos de infraestructura avanzada. Combina una interfaz gráfica completa construida con PyQt5 con lógica de trading real a través de CCXT, permitiendo conectarse a múltiples exchanges, ejecutar estrategias predefinidas o personalizadas, y gestionar el riesgo mediante Stop Loss, Take Profit y Trailing Stop.

Lo que diferencia este proyecto es su enfoque en accesibilidad: incluye un editor de estrategias en vivo dentro de la propia GUI, donde el usuario puede escribir código Python directamente y activarlo sin reiniciar el bot. Es una solución todo-en-uno que va desde la configuración del exchange hasta la exportación del historial de operaciones a Excel.

## Arquitectura y Patrones Clave
El proyecto sigue una arquitectura modular por capas bien diferenciadas:

- **Capa UI** (`ui/`): Ventanas y tabs PyQt5, separadas por responsabilidad (tab principal, ventana principal, tab de estrategia personalizada).
- **Capa Core** (`core/`): Lógica de ejecución del bot — el worker que corre en background, gestión de stop loss, trailing stop y auto-profit.
- **Capa de Estrategias** (`strategies/`): Módulos independientes por estrategia, con un archivo `indicators.py` compartido. Permite añadir nuevas estrategias como plugins.
- **Capa Utils** (`utils/`): Servicios transversales — gestión de configuración, estado, base de datos, historial y configuración de API.

El patrón central es **Worker/Thread separado de la UI**: el trading corre en un hilo distinto (`core/worker.py`) para no bloquear la interfaz gráfica. La carga de estrategias personalizadas sugiere uso de `exec()`/`importlib` dinámico. La configuración se gestiona con managers dedicados, separando la config de API de la config operacional.

## Componentes Principales

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
- **`utils/config_manager.py`** — Configuración operacional: par, timeframe, capital, parámetros de estrategia
- **`utils/db_manager.py`** — Persistencia de historial de operaciones (SQLite presumiblemente)
- **`utils/history_utils.py`** — Exportación de historial a Excel con openpyxl
- **`utils/state_manager.py`** — Estado global del bot (running, posición abierta, métricas)

## Dependencias Clave

- **`ccxt`** — Librería multi-exchange: conecta con Binance, Bybit, Kraken, etc. para obtener datos OHLCV y ejecutar órdenes
- **`PyQt5`** — Framework de interfaz gráfica: ventanas, tabs, botones, logs en tiempo real
- **`pandas`** — Manipulación de DataFrames OHLCV y cálculo de indicadores técnicos
- **`matplotlib` + `mplfinance`** — Visualización de velas y gráficos de precio dentro de la GUI
- **`openpyxl`** — Exportación del historial de trades a archivos Excel (.xlsx)
- **`qdarkstyle`** — Tema oscuro profesional para la interfaz PyQt5

## Fragmentos de Código Relevantes

**1. Interfaz de una estrategia — contrato que deben cumplir todas:**
```python
def strategy_custom(df, position, config):
    if df['close'].iloc[-1] > df['open'].iloc[-1]:
        return {'action': 'long', 'reason': 'Vela alcista'}
    return None
```
Todas las estrategias reciben el DataFrame con OHLCV, el estado de posición actual y la configuración. Retornan un dict con `action` y `reason`, o `None` si no hay señal.

**2. Ejecución del bot:**
```bash
python main.py
```
La aplicación arranca como GUI de escritorio, sin servidores ni APIs REST propias.

**3. Instalación completa:**
```bash
pip install -r requirements.txt
# requirements: pyqt5, ccxt, pandas, matplotlib, openpyxl, qdarkstyle, mplfinance
```

## Conclusiones y Aprendizajes

- **Separación Worker/UI**: Correr la lógica de negocio en un `QThread` separado y comunicarse con la GUI mediante señales/slots de Qt es el patrón correcto para cualquier aplicación PyQt5 con procesamiento en background — evita congelar la interfaz.
- **Arquitectura de estrategias como plugins**: Definir un contrato simple `strategy(df, position, config) -> dict | None` permite añadir estrategias nuevas sin modificar el core. Es un patrón Strategy (GoF) muy limpio.
- **Separación de managers por responsabilidad**: Tener `api_config_manager`, `config_manager`, `state_manager` y `db_manager` como clases independientes facilita el testing y la sustitución de implementaciones (e.g., cambiar SQLite por PostgreSQL).
- **CCXT como abstracción de exchange**: Usar CCXT desde el inicio evita acoplarse a una sola API. El código de órdenes funciona igual en Binance, Bybit o cualquier exchange soportado.
- **Editor de código dinámico en GUI**: Permitir al usuario escribir y ejecutar estrategias en vivo (con `exec` o `importlib`) es una técnica poderosa para herramientas de backtesting o bots configurables, aunque requiere sandboxing cuidadoso en producción.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code