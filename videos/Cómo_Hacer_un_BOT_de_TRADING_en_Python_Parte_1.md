# Cómo Hacer un BOT de TRADING en Python (Parte 1)

## Información General
- **Canal:** De 0 a 100 - Trading, Algoritmos y Quant
- **Duración:** 21m 23s
- **Idioma detectado:** Español
- **Transcripción fuente:** `Cómo_Hacer_un_BOT_de_TRADING_en_Python_Parte_1.txt`

## Resumen Ejecutivo
Este es el primer episodio de una serie orientada a construir un bot de trading automatizado en Python. El vídeo se centra exclusivamente en el primer paso fundamental: la descarga automática de datos históricos de precios y volumen de activos financieros (criptomonedas y acciones de bolsa) utilizando la librería gratuita `yfinance`, que extrae datos de Yahoo Finance.

El autor explica cómo usar el método `Ticker` y `history()` para obtener el histórico de precios de cierre (`Close`) y volumen (`Volume`) de cualquier activo, con distintos rangos temporales. También introduce el concepto de un archivo `scope.txt` que actúa como lista de activos a rastrear, permitiendo iterar sobre múltiples tickers de forma automatizada con muy pocas líneas de código.

El vídeo está intencionalmente simplificado por ser el primero de la serie con código. Se usa `matplotlib` únicamente para visualizar y verificar que los datos descargados son correctos. El siguiente episodio de la serie avanza hacia análisis técnico automático con medias móviles (cruce dorado y cruce de la muerte).

## Puntos Clave
- Se usa `yfinance` como fuente de datos gratuita en lugar de APIs de pago (ej. 50-100€/mes)
- Los datos provienen de Yahoo Finance, que puede tener inconsistencias o datos incompletos
- Para **criptomonedas**: el ticker requiere el sufijo `-USD` (ej. `BTC-USD`, `ETH-USD`)
- Para **acciones**: solo el ticker sin sufijo (ej. `MSFT`, `AAPL`, `AMZN`)
- El parámetro `period` de `history()` acepta: `"max"`, `"2y"`, `"1y"`, `"6mo"`
- El dato más usado es el **precio de cierre** (`Close`); para criptos el precio de apertura/cierre es menos relevante por ser mercado continuo
- Se introduce el archivo `scope.txt` como lista de tickers a monitorizar, leído con `splitlines()`
- Bitcoin en Yahoo Finance tiene datos disponibles desde finales de 2014, no desde 2009
- Se itera sobre el scope con un bucle `for activo in scope` para descargar todos los activos automáticamente

## Conceptos Técnicos Mencionados
- **`yfinance`** — Librería Python que envuelve la API no oficial de Yahoo Finance para descargar datos históricos de precios y fundamentales
- **`yf.Ticker(symbol)`** — Clase principal de yfinance para representar un activo financiero
- **`.history(period="max")`** — Método que retorna un DataFrame con OHLCV histórico del activo
- **`DataFrame["Close"]`** — Acceso a la serie de precios de cierre desde el DataFrame de yfinance
- **`DataFrame["Volume"]`** — Acceso a la serie de volumen negociado
- **`matplotlib.pyplot`** — Librería de visualización usada para graficar el precio histórico
- **`plt.figure(figsize=(12,6))`** — Configuración del tamaño del gráfico en matplotlib
- **`open()` / `.read()` / `.splitlines()`** — Lectura de archivo de texto en Python para cargar la lista de tickers
- **`scope.txt`** — Archivo de configuración con lista de tickers (un ticker por línea) que define el universo de activos a rastrear
- **VS Code** — Editor de código utilizado en el tutorial
- **Backtesting** — Concepto mencionado como uso previsto de los datos históricos descargados
- **Medias móviles / Cruce dorado / Cruce de la muerte** — Estrategias de análisis técnico que se implementarán en el siguiente episodio

## Fragmentos Relevantes

> *"Para las criptomonedas hay que poner el ticker, por ejemplo BTC-USD [...] sin embargo para las acciones no es así, para las acciones simplemente tienes que poner el ticker, por ejemplo MSFT, que es Microsoft, pero no pones el guión USD."*

> *"Si queremos descargarnos el histórico de precios tenemos que hacer `.history()` y aquí hay que poner un campo que se llama `period`; si queremos descargarnos toda la información hay que poner `max`."*

> *"Lo que devuelve todo esto es un diccionario [...] nosotros nos vamos a quedar con el histórico de precios y con el histórico de volumen. El histórico de precios se coge con la clave `Close`."*

> *"Vamos a crear un fichero que se llame `scope.txt` que es la lista de activos que nosotros vamos a utilizar y con los que vamos a rastrear con nuestro bot de trading."*

> *"En el caso de bitcoin no están los precios desde 2009 sino únicamente desde finales de 2014."*

## Conclusiones y Aprendizajes

**Aplicaciones directas en proyectos de software:**

1. **Bootstrap rápido de datos financieros**: Con menos de 10 líneas de Python se puede tener un pipeline funcional de descarga de datos OHLCV para cualquier activo disponible en Yahoo Finance, sin coste alguno.

2. **Patrón de configuración por archivo externo**: El uso de `scope.txt` es un patrón simple pero efectivo para desacoplar la configuración (universo de activos) del código, facilitando cambios sin tocar el script.

3. **Distinción crítica de formato de ticker**: Recordar siempre el sufijo `-USD` para criptomonedas en yfinance; omitirlo genera datos erróneos silenciosamente (el script no falla, pero los datos no tienen sentido).

4. **Limitaciones a considerar**: Yahoo Finance no garantiza completitud ni precisión; para backtesting serio con datos pre-2014 en cripto o datos intradiarios se necesitarán fuentes alternativas.

5. **Estructura base para un bot**: La combinación ticker → descarga histórico → almacenamiento en variables `precio` y `volumen` → iteración sobre scope, es la base sobre la que se construirán los módulos de análisis técnico y señales de trading en episodios posteriores.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code