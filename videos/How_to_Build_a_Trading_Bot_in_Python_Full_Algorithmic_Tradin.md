# How to Build a Trading Bot in Python | Full Algorithmic Trading Tutorial

## Información General
- **Canal:** Trading Steady
- **Duración:** 24m 17s
- **Idioma detectado:** en
- **Transcripción fuente:** `How_to_Build_a_Trading_Bot_in_Python_Full_Algorithmic_Tradin.txt`

## Resumen Ejecutivo
El video presenta un tutorial completo para construir un trading bot automatizado en Python desde cero, aplicable a stocks, forex y criptomonedas. El instructor utiliza el broker OANDA con su API oficial y el wrapper Python `oandapyV20` para establecer la conexión, descargar datos históricos de velas (OHLC), calcular indicadores técnicos y ejecutar órdenes de mercado de forma automática.

La estrategia implementada es un cruce de EMAs (5 y 8 períodos) con stop-loss basado en ATR (14 períodos) y take-profit con ratio 1.5:1. El bot detecta el cruce en las dos velas más recientes completas, calcula los niveles de entrada/stop/target y envía la orden directamente a la cuenta del broker mediante la API.

Para la automatización continua, el bot corre dentro de un bucle `while True` con lógica temporal basada en módulo para detectar el inicio de cada nueva vela (cada 15 minutos), evitando consultas redundantes a la API y controlando el ritmo con `time.sleep(1)`.

## Puntos Clave
- Configuración de credenciales en un archivo `config.py` separado (API key + Account ID)
- Uso del wrapper oficial de OANDA (`oandapyV20`) para simplificar llamadas a la API REST
- Descarga de datos de velas filtrando solo velas **completadas** (`complete == True`) para evitar repintado de indicadores
- Parsing de respuesta JSON a `pandas DataFrame` con columnas OHLC y timestamp en datetime
- Cálculo de EMA (5, 8) y ATR (14) usando la librería `pandas_ta`
- Detección de cruce de EMAs comparando los últimos dos índices (`-1` y `-2`) del DataFrame
- Cálculo dinámico de stop-loss (entrada - ATR) y take-profit (entrada + stop_distance × 1.5)
- Envío de órdenes de mercado con formato decimal correcto según el instrumento (3 decimales para GBP/JPY)
- Loop principal con detección de nuevo candle usando operador módulo sobre los minutos del reloj
- Uso de variable `last_checked` como flag para evitar múltiples ejecuciones en el mismo intervalo

## Conceptos Técnicos Mencionados

| Tecnología / Concepto | Descripción |
|---|---|
| **Python** | Lenguaje base del bot; se requiere instalación con "Add to PATH" |
| **VS Code** | Editor de código recomendado |
| **Jupyter Notebook** | Entorno usado para presentar el tutorial, ejecuta bloques de código independientes |
| **OANDA API** | API REST del broker OANDA para datos de mercado y ejecución de órdenes |
| **oandapyV20** | Wrapper Python oficial para la API de OANDA; instalable con `pip install opp` |
| **config.py** | Archivo de configuración para almacenar credenciales sensibles fuera del código principal |
| **pandas** | Librería para estructurar datos de velas en DataFrames |
| **pandas_ta** | Librería para cálculo de indicadores técnicos (EMA, ATR) sobre DataFrames |
| **EMA Crossover** | Estrategia de cruce de medias móviles exponenciales (5 y 8 períodos) como señal de entrada |
| **ATR (Average True Range)** | Indicador de volatilidad usado como base para calcular el stop-loss dinámico |
| **Market Order** | Tipo de orden ejecutada al precio actual de mercado |
| **Instruments Endpoint** | Endpoint de OANDA para solicitar datos históricos de velas (candlestick) |
| **Orders Endpoint** | Endpoint de OANDA para crear y gestionar órdenes |
| **datetime / timezone** | Módulos de Python para manejo de tiempo en el loop de automatización |
| **time.sleep()** | Control de frecuencia del bucle principal para no saturar la API |
| **Modulo operator (%)** | Usado para detectar inicio de nuevo intervalo temporal (e.g., `minute % 15 == 0`) |

## Fragmentos Relevantes

> *"I only need to check for new prices when a candle has closed. So, in my system, I'm trading on the 15-minute time frame. So, that means that I need to check every 15 minutes."*

> *"I check if this is a new 15-minute candle. And I do that by extracting the minute from the current time, dividing it by 15 using this modulo divider, which gives me the remainder. So if the remainder is zero, then that means that I'm either at 0, 15, 30, or 45 minutes past the hour."*

> *"You notice that the first key here is complete. And that says if it's true or false. What that's referring to is whether the very last candle that I received has completed or if it's still live. When working with this price data to calculate my indicators and entry and exit points, I need to use only the completed data. Otherwise, my indicators could repaint."*

> *"These index values allow me to work backwards from the end of a data frame. So if you use a negative value, it starts at the end and works backwards. Minus one is the very last value and then it goes minus2 minus3 and so on."*

> *"You'll notice that at the end I have this funny little bit of code. What this does is formats it to have three decimal points. The reason for that is because the instrument I'm trading is pound yen and that uses three decimal points... when I pass this data to the API, I need to make sure it matches the format of the instrument."*

## Conclusiones y Aprendizajes

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