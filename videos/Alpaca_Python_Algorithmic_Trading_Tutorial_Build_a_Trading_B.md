# Alpaca Python Algorithmic Trading Tutorial (Build a Trading Bot Step-by-Step)

## Información General
- **Canal:** Jonjo Wadwa
- **Duración:** 5m 14s
- **Idioma detectado:** en
- **Transcripción fuente:** `Alpaca_Python_Algorithmic_Trading_Tutorial_Build_a_Trading_B.txt`

## Resumen Ejecutivo
El video presenta una guía práctica paso a paso para ejecutar operaciones bursátiles algorítmicas usando la API de Alpaca Markets con Python. El autor argumenta que la principal barrera de entrada al trading algorítmico no es la complejidad estratégica, sino las fricciones técnicas de los brokers tradicionales (reautenticación frecuente, documentación obsoleta), y posiciona Alpaca como una solución moderna que simplifica este proceso.

El tutorial cubre desde el registro en Alpaca Markets y la generación de API keys hasta la ejecución de una orden de mercado real (en modo paper trading), pasando por la instalación de la librería `alpaca-py`, la conexión al cliente de trading, la inspección de detalles de cuenta y la consulta de activos. Todo el flujo se demuestra en menos de 5 minutos con código mínimo y funcional.

El enfoque es deliberadamente didáctico y orientado a la acción: cada bloque de código se muestra, se ejecuta en vivo y se verifica su output, lo que hace el tutorial especialmente útil para desarrolladores que quieren un punto de entrada rápido al trading programático sin configuraciones complejas.

## Puntos Clave
- **Alpaca soluciona la fricción de autenticación** que tienen otros brokers (no hay re-auth cada 24h)
- **Paper trading account** disponible gratis para pruebas sin dinero real; se pueden crear múltiples cuentas
- Las **API keys** (key + secret key) se generan desde el dashboard y deben guardarse de forma segura
- La librería se instala con `pip install alpaca-py`
- El cliente se inicializa con `TradingClient(api_key, secret_key, paper=True)` — el flag `paper=True` es crítico para no operar con dinero real
- Se puede inspeccionar el estado de la cuenta con `trading_client.get_account()`, accediendo a campos como `portfolio_value` o calcular el P&L diario comparando `equity` vs `equity_yesterday`
- Se pueden consultar activos por ticker con `trading_client.get_asset("QQQ")`
- Una orden de mercado se construye con `MarketOrderRequest(symbol, qty, side, time_in_force)` y se envía con `trading_client.submit_order(order_data)`
- `OrderSide` y `TimeInForce` son enums que parametrizan la dirección y vigencia de la orden

## Conceptos Técnicos Mencionados

- **Alpaca Markets** — Broker con API REST para trading algorítmico, orientado a desarrolladores, sin fricciones de autenticación
- **alpaca-py** — Librería oficial de Python para interactuar con la API de Alpaca (instalable via pip)
- **TradingClient** — Clase principal del SDK que gestiona la conexión autenticada a la API
- **Paper Trading** — Modo de simulación que replica el mercado real sin usar dinero real; Alpaca provee $100k virtuales por defecto
- **API Key / Secret Key** — Par de credenciales generadas desde el dashboard de Alpaca para autenticación
- **MarketOrderRequest** — Clase que encapsula los parámetros de una orden a precio de mercado (sin precio límite)
- **OrderSide** — Enum para indicar dirección de la operación (`BUY` / `SELL`)
- **TimeInForce** — Enum que define la vigencia de la orden (ej. `DAY`, `GTC`)
- **get_account()** — Método del cliente que retorna el estado completo de la cuenta (equity, portfolio value, etc.)
- **get_asset(symbol)** — Método para obtener metadatos de un activo financiero por su ticker
- **submit_order(order_request)** — Método para enviar una orden al mercado a través del cliente

## Fragmentos Relevantes

> *"Most people quit algorithmic trading before they've even had a chance to execute a trade. Not because strategies are difficult, but because brokers make it impossible for you to actually execute a trade."*

> *"We're going to set paper to true to ensure we're not trading with real money."*

> *"All we need to do is install Alpaca Pi. So we do that simply through pip install Alpaca Pi."*

> *"We can see that it returns all our account details... for example, we could look at the portfolio value. We can see that we've got $10,000 in there."*

> *"Here we're just looking at the equity of right now versus the equity yesterday... we just wrapped them in a float to make sure that we can perform some math to minus on them."*

> *"If we run this, we can see that we just submitted successfully... quantity of five... it's as simple as that."*

## Conclusiones y Aprendizajes

- **Setup en minutos:** Con solo ~15 líneas de Python se puede tener un bot funcional que ejecuta órdenes reales en mercados financieros; es un punto de partida sólido para proyectos de mayor complejidad.
- **Siempre usar `paper=True` en desarrollo:** El flag debe estar presente en cualquier entorno que no sea producción para evitar operaciones accidentales con dinero real.
- **Separación de credenciales:** Las API keys deben almacenarse en variables de entorno o un gestor de secretos, nunca hardcodeadas en el código fuente.
- **Patrón Request Object:** El SDK usa el patrón de objetos de solicitud (`MarketOrderRequest`) que facilita la validación antes de enviar, lo que es una buena práctica para extender a otros tipos de órdenes (limit, stop, etc.).
- **Inspección de cuenta útil para estrategias:** Los métodos `get_account()` y `get_asset()` permiten construir lógica condicional basada en estado del portafolio (ej. solo operar si el P&L del día supera X%).
- **Escalabilidad:** Este mismo patrón se puede extender para añadir estrategias, scheduling con `schedule` o `APScheduler`, y manejo de websockets para datos en tiempo real.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code