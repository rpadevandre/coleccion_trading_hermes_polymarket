# I Built an AI Bot That Reads Market News and Predicts Sentiment Instantly [Free Python Script]

## Información General
- **Canal:** CodeTrading
- **Duración:** 8m 40s
- **Idioma detectado:** English
- **Transcripción fuente:** `I_Built_an_AI_Bot_That_Reads_Market_News_and_Predicts_Sentim.txt`

## Resumen Ejecutivo
El video presenta un bot en Python que realiza análisis de sentimiento sobre noticias financieras en tiempo real, orientado a traders que quieren cuantificar el tono del mercado antes de operar. El sistema busca artículos usando consultas predefinidas (ej: "gold market", "gold price"), extrae los títulos mediante web scraping con BeautifulSoup y Google RSS, y los procesa con dos modelos de NLP: VADER (léxico) y FinBERT (deep learning entrenado en datos financieros).

El resultado final es una distribución de frecuencias entre sentimientos positivos, negativos y neutrales, más un score numérico consolidado: valores positivos indican sesgo alcista y negativos indican sesgo bajista. En el ejemplo en vivo del video, de 70 artículos sobre oro, el 30% resultó positivo, 21% negativo y 48% neutral.

El bot está diseñado para ejecutarse de forma programada (ej: cron job diario) antes de sesiones de trading, actuando como señal auxiliar de decisión basada en el sentimiento colectivo de las noticias del día.

## Puntos Clave
- Se usan múltiples queries por activo (`gold market`, `gold price`, `gold news`, `gold trends`) para ampliar la cobertura de noticias
- Se obtienen los top 10 resultados de Google por query, concatenando todos en una lista maestra (`all_articles`)
- El análisis se aplica sobre el **título** del artículo (no el cuerpo completo), por simplicidad y velocidad
- **VADER** usa umbrales de polaridad: > 0.05 = positivo, < -0.05 = negativo, entre ambos = neutral
- **FinBERT** es el modelo preferido por estar entrenado específicamente en noticias y reportes financieros reales
- La función `summarize_sentiments` genera frecuencias y porcentajes de las tres categorías
- El script puede adaptarse a cualquier activo (oil, tech stocks) cambiando los keywords
- Se recomienda usar un **cron scheduler** para automatizar la ejecución diaria
- Scores positivos = sesgo bullish, negativos = sesgo bearish

## Conceptos Técnicos Mencionados
- **FinBERT** — Modelo de deep learning basado en BERT, preentrenado en datos financieros (noticias, reportes); disponible en Hugging Face
- **VADER (Valence Aware Dictionary and sEntiment Reasoner)** — Modelo léxico de análisis de sentimiento, basado en reglas y diccionario; rápido y sin GPU requerida
- **Hugging Face Transformers** — Librería usada para cargar el modelo FinBERT y su tokenizer
- **BeautifulSoup** — Librería Python de web scraping para extraer contenido de páginas web a partir de URLs
- **Google RSS / Search scraping** — Método para obtener los top 10 resultados de búsqueda por query como fuente de noticias
- **RSS Feeds** — Formato de sindicación de contenido usado como fuente alternativa de headlines financieros
- **Cron Job / Scheduler** — Mecanismo de automatización para ejecutar el script en horarios definidos (ej: antes de apertura de sesión)
- **Polarity Score** — Métrica numérica que resume el sentimiento: positivo (bullish) vs negativo (bearish)
- **Sentiment Analysis (NLP)** — Técnica de procesamiento de lenguaje natural para clasificar texto como positivo, negativo o neutral
- **Virtual Environment (Python)** — Entorno aislado para gestión de dependencias del proyecto

## Fragmentos Relevantes

> *"FinBERT was trained on real financial reports and news data, it actually understands the difference between a sentence like 'Apple beats earnings' and 'Apple under investigation'."*

> *"Positive numbers indicate bullish market sentiment and negative numbers indicate a bearish sentiment bias."*

> *"Major price movements are often preceded by news events. If we can quantify the tone of news stories in real time... we might detect early clues about where the market is heading in the next few hours."*

> *"Vader uses a threshold, a probability threshold. For example, if the polarity is above 0.05... that's a positive indicator. If the polarity is less than -0.05, that's a negative sentiment. Anything in between is neutral."*

> *"You can add a small cron scheduler. Run it once per day, for example, at the beginning or at the end of a certain session. Check the news and the sentiments. You get your sentiments before the trading session and you trade based on these news."*

> *"We have a positive frequency of 21. The total articles analyzed 70 and 30% are positive, 21% are negative and 48% are neutral."*

## Conclusiones y Aprendizajes
- **Pipeline replicable**: El flujo `queries → scraping Google → extracción de títulos → análisis NLP → score consolidado` es directo de implementar en cualquier proyecto de market intelligence.
- **Swap de modelos sin fricción**: La arquitectura separa la función `analyze_sentiment` del resto, lo que permite cambiar VADER por FinBERT (o cualquier LLM) sin tocar el pipeline principal.
- **Granularidad ajustable**: Analizar solo títulos es el modo rápido; escalar a contenido completo del artículo mejora la señal a costa de tiempo de scraping.
- **Extensible a múltiples activos**: Reemplazar los keywords de `queries` permite monitorizar oil, índices, crypto o acciones individuales sin cambiar ninguna otra lógica.
- **Automatización trivial**: Agregar un scheduler (APScheduler o cron) convierte el script en un sistema de alertas diarias de sentimiento de mercado.
- **Consideración de producción**: Para uso real, conviene manejar rate limits de Google scraping (usar APIs como NewsAPI o Alpha Vantage como alternativa más estable), y añadir deduplicación de artículos entre queries.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code