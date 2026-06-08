# I Gave My Terrible Trading Bot $10,000 to Trade Stocks

## Información General
- **Canal:** Coding with Lewis
- **Duración:** 16m 5s
- **Idioma detectado:** en
- **Transcripción fuente:** `I_Gave_My_Terrible_Trading_Bot_10000_to_Trade_Stocks.txt`

## Resumen Ejecutivo
Lewis construye tres trading bots con estrategias radicalmente distintas y los pone a operar con $10,000 reales durante 3-4 días. El primer bot combina momentum trading y análisis de valor (ratio P/E + media móvil) sobre un conjunto predefinido de acciones seguras. El segundo bot escanea noticias en tiempo real, vectoriza descripciones de empresas para identificar qué stock se ve afectado por cada artículo, y compra o vende según el sentimiento. El tercero —llamado "Swift Trade 1.0"— elige un stock aleatorio, busca noticias recientes, las compara con letras de Taylor Swift mediante búsqueda vectorial, y decide si comprar o vender según si la letra más similar tiene sentimiento positivo o negativo.

El proceso técnico cubre backtesting con optimización de parámetros, integración con el broker Interactive Brokers vía una librería open-source de Python, uso de una base de datos vectorial (DataStax Astra DB sobre Cassandra) para almacenar embeddings de descripciones de empresas y letras de canciones, y análisis de sentimiento con modelos de ML. Tras 3-4 días de operación real, los tres bots combinados generaron $109.35 brutos, pero tras comisiones y suscripciones a datos de mercado ($117.70), el resultado neto fue una pérdida de $8.35.

El video ilustra de forma práctica el ciclo completo de un proyecto de automatización financiera: ideación de estrategia → backtesting → optimización de parámetros → integración con API de broker → despliegue en producción, con todos los problemas reales que eso conlleva (APIs cerradas, costes de datos, bugs en producción).

## Puntos Clave
- **Tres estrategias** con riesgo creciente: momentum/valor → news sentiment → Taylor Swift random lyric matching
- **Backtesting obligatorio** antes de deploy: permite validar la estrategia con datos históricos y evitar pérdidas predecibles
- **Optimización de parámetros** mediante fuerza bruta: 22,500 combinaciones (25 periodos × 30 overbought × 30 oversold) ejecutadas en paralelo usando 24 cores; tardó +25 minutos
- **El mejor resultado del backtest del bot 1** fue solo $23 de ganancia, lo que se consideró aceptable para una estrategia de pocos días
- **Costes ocultos** del trading real: suscripciones a datos de mercado en tiempo real ($117.70) pueden superar las ganancias del bot
- **APIs cerradas**: tras los cambios de Twitter/Reddit, el acceso a datos de noticias requiere pagar; el creador tuvo que contratar APIs de pago
- **Interactive Brokers** es la única opción viable para canadienses, pero su API nativa es deficiente; se usa una librería open-source como wrapper
- **Resultado final**: $109.35 brutos → -$8.35 netos incluyendo todos los costes
- **Swift Trade** hizo solo 2 trades durante el periodo, posiblemente por datos limitados al inicio
- **El bot de noticias** fue el más activo: 9 stocks comprados/vendidos con ganancia neta positiva
- **Embeddings vectoriales** usados para dos propósitos: buscar qué empresa corresponde a una noticia y buscar qué lyric de Taylor Swift es más similar a un artículo de noticias

## Conceptos Técnicos Mencionados

- **Momentum Trading** — Estrategia que compra activos que han mostrado tendencia alciente y vende cuando la tendencia baja, basándose en medias móviles
- **Value Trading (P/E Ratio)** — Comprar acciones cuando el ratio precio/ganancias está por debajo de la media, indicando posible infravaloración
- **Moving Average (Media Móvil)** — Indicador técnico que suaviza el precio promedio en un periodo de tiempo para identificar tendencias
- **Backtesting** — Técnica de validar una estrategia de trading ejecutándola contra datos históricos antes de usarla con dinero real
- **Back Trader** — Framework de Python para implementar y backtestear estrategias de trading con datos históricos
- **Parameter Optimization** — Proceso de probar múltiples combinaciones de parámetros en backtesting para encontrar los valores óptimos
- **Sentiment Analysis** — Análisis de texto (noticias) para determinar si el contenido es positivo, negativo o neutro; usado para decisiones de compra/venta
- **Vector Embeddings** — Representaciones numéricas de texto que capturan significado semántico, usadas para búsqueda por similitud
- **Vector Search / Vector Database** — Búsqueda por similitud semántica sobre embeddings; usado para relacionar noticias con empresas y letras con artículos
- **DataStax Astra DB** — Base de datos vectorial serverless construida sobre Apache Cassandra, usada como backend para almacenar y buscar embeddings
- **Apache Cassandra** — Base de datos NoSQL distribuida, de alta escala, sobre la que corre Astra DB
- **Interactive Brokers API** — API del broker financiero para enviar órdenes de compra/venta desde código; wrapper open-source de Python usado para mejorar la experiencia
- **OpenAI API** — Usado para generar descripciones de stocks y calcular embeddings de texto
- **News API** — API de pago para obtener artículos de noticias en tiempo real sobre empresas específicas
- **NASDAQ / NYSE stock lists** — Listas de tickers descargadas para alimentar el bot de noticias y el bot de Taylor Swift
- **Parallel Processing** — Uso de múltiples cores de CPU (24 en el caso del creador) para ejecutar optimizaciones de parámetros en paralelo
- **Python** — Lenguaje principal usado para los tres bots y toda la infraestructura

## Fragmentos Relevantes

> *"Backtesting is where you take your strategy and see how it performs on historical data."*

> *"We're testing over 22,500 different combinations. I have 24 different cores on my computer and use them all in parallel to get this running as fast as possible. It was seriously so long and it took over 25 minutes to run."*

> *"Something I wasn't expecting was how closed all information is basically everywhere after the whole Twitter and Reddit API situation — everywhere is doing it now, so it looks like I'm forking up some more cash."*

> *"The $109.35 accounts for commissions and fees included. But I also had to buy a lot of subscriptions to access real time market data. So Interactive Brokers automatically took $117.70 off. So if you actually want to include that in your portfolio, we actually lost $8.35."*

> *"We embed this description so I can vector search it later, upload to Astra and we're good to go."*

> *"We embed the articles and have DataStax match it with the Taylor Swift lyric that relates to it the most. We then determine if this lyric is positive or negative. If it's positive, we buy as much stock as we can."*

## Conclusiones y Aprendizajes

- **El backtesting es imprescindible pero no suficiente**: validar con datos históricos es el primer paso, pero los costes de producción (suscripciones, comisiones) pueden invalidar una estrategia que en papel era rentable
- **Calcular el TCO real antes de hacer deploy**: las APIs de noticias, los datos de mercado en tiempo real y las comisiones del broker son costes fijos que deben considerarse como parte del presupuesto del proyecto, no como extras
- **Los embeddings vectoriales son una herramienta versátil**: en este proyecto se usan tanto para búsqueda semántica de empresas como para matching de letras, lo que demuestra que la misma infraestructura vectorial puede resolver múltiples problemas de similaridad en un mismo proyecto
- **Separar la lógica de estrategia de la lógica de broker**: el patrón de backtestear primero y luego "convertir a código de Interactive Brokers" permite iterar rápido sin arriesgar dinero real
- **La optimización de hiperparámetros en trading es computacionalmente costosa**: para proyectos de producción, considerar frameworks más eficientes (Optuna, Ray Tune) en lugar de búsqueda exhaustiva
- **Los wrappers open-source sobre APIs deficientes son válidos en producción**: aceptable usar librerías comunitarias cuando la API oficial es difícil de usar, pero hay que evaluar su mantenimiento
- **El acceso a datos es frecuentemente el cuello de botella y el mayor coste** en proyectos de datos en tiempo real; siempre investigar precios antes de diseñar la arquitectura

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code