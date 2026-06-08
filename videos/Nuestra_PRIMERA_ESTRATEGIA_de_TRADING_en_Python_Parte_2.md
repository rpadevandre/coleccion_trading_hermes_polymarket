# Nuestra PRIMERA ESTRATEGIA de TRADING en Python (Parte 2)

## Información General
- **Canal:** De 0 a 100 - Trading, Algoritmos y Quant
- **Duración:** 18m 14s
- **Idioma detectado:** Español
- **Transcripción fuente:** `Nuestra_PRIMERA_ESTRATEGIA_de_TRADING_en_Python_Parte_2.txt`

## Resumen Ejecutivo
Este vídeo es el quinto de una serie en la que se construye un bot de trading algorítmico en Python. En esta entrega se introduce el análisis técnico automatizado, comenzando por el cálculo e interpretación de medias móviles como indicadores de tendencia. El presentador explica la lógica detrás de la estrategia más clásica basada en medias móviles: el Golden Cross y el Death Cross, y muestra cómo implementarla en código Python.

Se desarrolla un módulo separado (`medias_moviles.py`) que contiene funciones reutilizables para calcular los tres tipos de medias móviles (simple, exponencial y acumulativa), así como una función `golden_and_death_crosses` que detecta automáticamente los puntos de cruce entre la media móvil de corto y largo plazo. Los resultados se visualizan sobre el gráfico de precios con triángulos de colores que marcan cada señal alcista o bajista.

El presentador muestra ejemplos reales con Bitcoin, Ethereum y acciones como Microsoft, recalcando que la estrategia es útil pero no infalible, y que su potencia real emerge cuando se combina con otros indicadores técnicos como RSI, MACD, bandas de Bollinger o soportes y resistencias. El vídeo cierra estableciendo la hoja de ruta de los próximos episodios donde se irán añadiendo más herramientas de análisis técnico.

## Puntos Clave
- El bot analiza automáticamente una lista de activos definida en un fichero `scope.txt`
- Se implementan tres tipos de medias móviles: **simple (SMA)**, **exponencial (EMA)** y **acumulativa (CMA)**
- La estrategia **Golden Cross** ocurre cuando la media móvil corta cruza de abajo hacia arriba a la larga → señal **alcista**
- La estrategia **Death Cross** ocurre cuando la media móvil corta cruza de arriba hacia abajo a la larga → señal **bajista**
- Por defecto se usan las medias de **50 y 200 sesiones**, pero son configurables
- Las señales se visualizan como **triángulos verdes (alcista)** y **triángulos rojos (bajista)** sobre el gráfico de precios
- Los indicadores de medias móviles no tienen un acierto del 100%; se recomienda combinarlos con otros indicadores
- El código se organiza en módulos separados (p.ej. `medias_moviles.py`) importados desde el script principal
- La librería `yfinance` sigue siendo el origen de datos, descargando desde Yahoo Finance
- La librería `matplotlib` se usa para la visualización gráfica

## Conceptos Técnicos Mencionados
- **yfinance** — Librería Python para descargar datos históricos de precios desde Yahoo Finance
- **matplotlib** — Librería Python para visualización de datos y gráficos financieros
- **SMA (Simple Moving Average)** — Media móvil simple: promedio aritmético de los últimos N cierres
- **EMA (Exponential Moving Average)** — Media móvil exponencial: da más peso a los días más recientes
- **CMA (Cumulative Moving Average)** — Media móvil acumulativa: promedio de todos los datos hasta la fecha actual
- **Golden Cross** — Señal alcista generada cuando la SMA corta cruza hacia arriba a la SMA larga
- **Death Cross** — Señal bajista generada cuando la SMA corta cruza hacia abajo a la SMA larga
- **scope.txt** — Fichero de texto con la lista de activos a analizar (tickers)
- **medias_moviles.py** — Módulo Python propio que encapsula el cálculo de medias y la detección de cruces
- **RSI (Relative Strength Index)** — Oscilador mencionado como próximo indicador a implementar
- **MACD** — Indicador de convergencia/divergencia de medias móviles, mencionado como trabajo futuro
- **Bandas de Bollinger** — Indicador de volatilidad mencionado para próximos vídeos
- **Fibonacci** — Niveles de retroceso mencionados como próxima herramienta a incorporar
- **Soportes y resistencias** — Niveles de precio clave mencionados como futura funcionalidad del bot

## Fragmentos Relevantes
> "Cuando la media móvil corta cruza de abajo hacia arriba a la media móvil larga eso es una señal alcista. Porque si nos paramos a analizar el que la media móvil corta cruce a la larga significa que la tendencia de los últimos días es más alcista que de los días anteriores."

> "El caso contrario es el cruce de la muerte: es cuando la media móvil corta cruza de arriba hacia abajo a la media móvil larga, de forma que podemos interpretar que la tendencia de los últimos 200 días es más alcista que la que realmente están teniendo los últimos 50 días."

> "Este tipo de indicador se suele cumplir en una mayoría de los casos, pero por supuesto también falla."

> "Cuando muchas cosas indican lo mismo, las probabilidades de estar acertadas obviamente son más altas."

> "Si nosotros le decimos al Bot: cálculame todo esto y avísame si se cumple que el RSI está por encima de X punto y además está en una resistencia... rastreará todo el mercado y si se cumpliera eso nos va a mostrar el gráfico ya analizado."

## Conclusiones y Aprendizajes
- **Modularización del código**: separar los cálculos de indicadores en ficheros independientes (p.ej. `medias_moviles.py`) mejora la mantenibilidad y permite reutilizar funciones en distintas estrategias.
- **Parametrización de estrategias**: las funciones deben aceptar parámetros configurables (tipo de media, periodos corto/largo) para facilitar la experimentación sin modificar el código base.
- **No depender de un solo indicador**: arquitectura del bot diseñada para combinar múltiples señales antes de tomar decisiones, reduciendo falsos positivos.
- **Pipeline de análisis técnico**: el patrón `descargar datos → calcular indicadores → detectar señales → visualizar` es reutilizable para cualquier indicador técnico adicional.
- **Iteración sobre un universo de activos**: leer el scope desde un fichero externo permite cambiar los activos analizados sin tocar el código, lo que es una buena práctica para sistemas de screening.
- **Visualización como herramienta de validación**: representar gráficamente las señales generadas es clave para verificar que la lógica implementada es correcta antes de automatizar decisiones.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code