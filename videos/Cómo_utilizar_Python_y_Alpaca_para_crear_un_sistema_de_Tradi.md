# 👉¿Cómo utilizar Python y Alpaca para crear un sistema de Trading Automático?

## Información General
- **Canal:** PythonIA
- **Duración:** 8m 23s
- **Idioma detectado:** Español
- **Transcripción fuente:** `Cómo_utilizar_Python_y_Alpaca_para_crear_un_sistema_de_Tradi.txt`

## Resumen Ejecutivo
El video explica cómo conectarse a la API de Alpaca Markets usando Python para extraer datos históricos de precios de activos financieros (acciones, criptomonedas). Se cubre el proceso completo desde la creación de la cuenta en Alpaca (modo Paper/demo), la obtención de las API Keys, hasta la instalación del SDK oficial `alpaca-trade-api`.

Una vez obtenidos los datos, se demuestra cómo estructurarlos en un DataFrame de Pandas con columnas OHLC (Open, High, Low, Close) y cómo visualizarlos mediante un gráfico de velas (candlestick chart) utilizando la librería Plotly. El ejemplo práctico usa el ticker de Apple (AAPL) con temporalidad diaria.

Todo el flujo se ejecuta en Google Colab, aunque se menciona que para la interactividad completa de los gráficos Plotly (zoom, pan) es necesario ejecutar el código en un entorno local como Visual Studio Code.

## Puntos Clave
- **Alpaca** ofrece una cuenta **Paper Trading** (demo) gratuita para operar sin dinero real, ideal para desarrollo y pruebas.
- Se necesitan **dos API Keys**: la clave pública (`API Key`) y la clave secreta (`API Secret`), obtenidas desde el panel de control de Alpaca.
- El **endpoint** (URL base) de la API es un parámetro requerido al inicializar el cliente.
- El SDK `alpaca-trade-api` simplifica las llamadas HTTP a la API REST de Alpaca.
- La función principal para obtener datos es **`get_bars()`**, que acepta: símbolo, timeframe, fecha de inicio y fecha de fin.
- Los timeframes disponibles incluyen: **diario, semanal**, y otros intervalos temporales.
- Los datos deben iterarse y cargarse manualmente en un **DataFrame de Pandas** con columnas: `Time`, `Open`, `High`, `Low`, `Close`.
- El índice del DataFrame debe establecerse en la columna `Time` con `set_index()` antes de graficar.
- **Plotly** se usa para renderizar el gráfico de candlesticks pasando las columnas OHLC como parámetros.
- La interactividad completa de Plotly requiere **ejecución local** (no funciona plenamente en Google Colab).

## Conceptos Técnicos Mencionados
- **Alpaca Markets** — Proveedor de datos financieros y broker con API REST para trading algorítmico; ofrece modo Paper Trading gratuito.
- **alpaca-trade-api** — SDK oficial de Python para interactuar con la API de Alpaca (datos de mercado y ejecución de órdenes).
- **API Key / API Secret** — Par de credenciales necesarias para autenticarse contra la API de Alpaca.
- **Paper Trading** — Modalidad de trading simulado sin dinero real; útil para testear estrategias.
- **get_bars()** — Función del SDK de Alpaca para obtener barras OHLCV históricas de un activo.
- **Timeframe** — Granularidad temporal de los datos de mercado (diario, semanal, intradía).
- **OHLC (Open, High, Low, Close)** — Estructura estándar de datos de precios de activos financieros.
- **Candlestick Chart** — Tipo de gráfico financiero que representa los cuatro precios principales de cada período.
- **Pandas DataFrame** — Estructura tabular de Python utilizada para almacenar y manipular los datos de precios.
- **Plotly** — Librería de visualización interactiva en Python; permite crear dashboards y gráficos financieros.
- **Google Colab** — Entorno de notebooks en la nube usado para el desarrollo en el video.
- **HTTP API / REST** — Alternativa al SDK para interactuar con Alpaca mediante peticiones HTTP directas.

## Fragmentos Relevantes
> *"Para poder operar en demo que es vamos a estar viendo en esta sesión vamos a operar usando la cuenta de Paper."*

> *"Necesitamos dos keys: una que es la Secret y otra que es la normal. Para poder crearlas tendríamos que dar a regenerate."*

> *"Podemos utilizar lo que es el SDK que es una especie de entorno de librería que nos facilita alpaca para trabajar con un lenguaje de programación, o podríamos utilizar una petición HTTP."*

> *"Vamos a extraer datos de Apple, le estoy diciendo que me quiero los datos en timeframe de un día, donde le estoy pasando un start_date y un end_date que tienen que ser de esta forma como string, donde ponemos el año, el mes y el día."*

> *"Importante esta línea: setear el set_index al Time, para definir en este caso el índice del DataFrame que va a ser el Time."*

> *"Para poder implementar un gráfico en Plotly que se vea bien, tendríamos que ejecutarlo en nuestro entorno local."*

## Conclusiones y Aprendizajes
- **Integración rápida con brokers vía SDK:** El patrón de autenticar con API Key + Secret y usar un SDK oficial es directamente aplicable a otros brokers/proveedores (Interactive Brokers, Binance, etc.).
- **Pipeline de datos financieros:** El flujo `API → iteración → DataFrame → visualización` es el esquema base para cualquier sistema de análisis cuantitativo.
- **Paper Trading como entorno de staging:** Usar la cuenta Paper equivale a tener un entorno de staging antes de pasar a producción real; es buena práctica antes de operar con capital real.
- **Plotly para dashboards financieros:** La librería es adecuada para construir interfaces de monitoreo de estrategias de trading con gráficos interactivos.
- **Separación de credenciales:** Las API Keys nunca deben hardcodearse en el código; se recomienda usar variables de entorno o archivos `.env` (el video las pone en variables de Python como paso introductorio).
- **Ejecución local para producción:** Google Colab es válido para prototipado, pero un sistema de trading automático real debe ejecutarse en un entorno local o servidor dedicado.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code