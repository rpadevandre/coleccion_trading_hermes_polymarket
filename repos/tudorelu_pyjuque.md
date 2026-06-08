# pyjuque

## Información General
- **Repo:** `tudorelu/pyjuque`
- **URL:** https://github.com/tudorelu/pyjuque
- **Lenguaje principal:** Python
- **Stars:** 457
- **Última actualización:** 2023-10-29
- **Topics:** algorithmic-trading, binance, bitcoin, bot, ccxt, cryptocurrencies, ethereum, kucoin, okex, plotting, python3, strategy, trading

## Propósito del Repo
pyjuque (Python Juju Quant Engine) es un framework de trading algorítmico open source diseñado para ser un punto de partida estructurado para bots de trading en criptomonedas. Resuelve el problema de tener que construir desde cero la infraestructura básica de un bot (gestión de órdenes, persistencia, conexión a exchanges, backtesting) permitiendo al desarrollador centrarse en la lógica de la estrategia.

Está diseñado para traders-desarrolladores que quieren automatizar estrategias en exchanges como Binance, KuCoin u OKEx, con soporte multi-exchange vía CCXT. Su diferenciador es que combina en un solo paquete el ciclo completo: backtesting, simulación, ejecución live y plotting, con un template de estrategia que estandariza cómo se definen las señales de entrada/salida.

## Arquitectura y Patrones Clave
El proyecto sigue una arquitectura en capas claramente separadas:
- **Capa de Exchange:** abstrae la comunicación con los exchanges mediante wrappers (Binance nativo + CcxtExchange genérico)
- **Capa de Engine:** contiene el BotController que orquesta el ciclo principal del bot, el OrderManager para gestión de órdenes, y modelos de base de datos vía SQLAlchemy (ORM)
- **Capa de Estrategia:** usa el patrón Template Method — `StrategyTemplate` define la interfaz (`setUp`, señales long/short) y el usuario implementa subclases
- **Capa de Backtesting:** motor separado que reutiliza las mismas estrategias para simulación histórica
- **Capa de Plotting:** visualización con Plotly

El patrón principal es **Template Method** para estrategias, **Adapter/Wrapper** para los exchanges, y **Repository** implícito con SQLAlchemy para persistencia de órdenes y posiciones. La configuración del bot se pasa como diccionario estructurado, lo que actúa como un patrón de **Builder declarativo**.

## Componentes Principales
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

## Dependencias Clave
- **`ccxt`** — Conexión a +100 exchanges de criptomonedas; usado en `CcxtExchange` como wrapper universal
- **`SQLAlchemy 1.3`** — ORM para persistir órdenes, pares y estado del bot en base de datos relacional
- **`pandas`** — Manipulación de DataFrames de velas (OHLCV); columna central del pipeline de estrategias
- **`numpy`** — Operaciones numéricas auxiliares en cálculos de estrategias
- **`plotly`** — Generación de gráficos interactivos de backtesting y señales de trading
- **`python-dotenv`** — Carga de credenciales de API desde archivo `.env`
- **`websocket-client`** — Conexión WebSocket para order book en tiempo real de Binance
- **`requests`** — Llamadas HTTP directas a la API REST de Binance en el wrapper nativo
- **`yaspin`** — Spinner visual en consola durante la ejecución del bot
- **`pyyaml`** — Parsing de archivos de configuración YAML

## Fragmentos de Código Relevantes

**1. Definición de estrategia con Template Method:**
```python
from pyjuque.Strategies import StrategyTemplate

class MomentumStrategy(StrategyTemplate):
    def __init__(self, momentum_period=3):
        self.momentum_period = momentum_period
        self.minimum_period = max(100, momentum_period)

    def setUp(self, df):
        long_signals = [0] * self.momentum_period
        short_signals = [0] * self.momentum_period
        close = df['close']
        for i in range(self.momentum_period, len(df)):
            all_increasing = all(close[j] > close[j-1] 
                                 for j in range(i + 1 - self.momentum_period, i + 1))
            all_decreasing = all(close[j] < close[j-1] 
                                 for j in range(i + 1 - self.momentum_period, i + 1))
            long_signals.append(int(all_increasing))
            short_signals.append(int(all_decreasing))
        df['long_signal'] = long_signals
        df['short_signal'] = short_signals
        return df
```

**2. Configuración declarativa del bot (patrón Builder dict):**
```python
bot_settings = {
    'name': 'my_bot',
    'starting_balance': 0.0005,
    'paper_trading': True,         # modo simulación sin dinero real
    'exchange': {
        'name': 'binance',
        'params': { 'api_key': '...', 'secret': '...' }
    },
    'strategy': MomentumStrategy(momentum_period=3),
    'symbols': [{
        'symbol': 'BTC/USDT',
        'timeframe': '1h',
        'trade_against': 'USDT',
        'stop_loss_value': 0.02,     # 2% stop loss
    }]
}
```

**3. Backtesting con datos CSV o live:**
```python
from pyjuque.Backtester import Backtester
from pyjuque.Exchanges.CcxtExchange import CcxtExchange

exchange = CcxtExchange('binance', {'enableRateLimit': True})
backtester = Backtester(
    strategy=MomentumStrategy(momentum_period=3),
    exchange=exchange,
    symbol='BTC/USDT',
    timeframe='1h',
    start_date='2021-01-01',
)
backtester.run()
backtester.plot()
```

## Conclusiones y Aprendizajes
- **Template Method para estrategias** es un patrón muy efectivo en sistemas de trading: definir `setUp(df) -> df` como contrato permite que el engine sea agnóstico a la lógica de negocio mientras reutiliza todo el pipeline de ejecución y backtesting.
- **Configuración como diccionario estructurado** (en lugar de herencia o subclases de Bot) reduce la barrera de entrada y permite instanciar múltiples bots con configuraciones distintas sin código adicional — patrón aplicable a cualquier sistema de workers configurable.
- **Separar el wrapper de exchange de la lógica del bot** via Adapter es crítico para testabilidad: permite mockear el exchange y correr pruebas sin llamadas reales a APIs.
- **Modo paper trading integrado** como flag en la configuración (no como clase separada) simplifica el flujo de desarrollo: misma lógica, diferente modo de ejecución.
- **SQLAlchemy como capa de persistencia** permite cambiar fácilmente entre SQLite (desarrollo/test) y PostgreSQL/MySQL (producción) sin cambiar código de negocio — patrón recomendable para cualquier bot que necesite estado persistente entre reinicios.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code