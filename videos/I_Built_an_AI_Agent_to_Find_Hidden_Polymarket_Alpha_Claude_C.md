# I Built an AI Agent to Find Hidden Polymarket Alpha (Claude Code)

## Información General
- **Canal:** The Prediction Engineer
- **Duración:** 9m 52s
- **Idioma detectado:** English
- **Transcripción fuente:** `I_Built_an_AI_Agent_to_Find_Hidden_Polymarket_Alpha_Claude_C.txt`

## Resumen Ejecutivo
El video muestra cómo usar Claude Code (el agente de IA de Anthropic) para construir una herramienta de visualización de datos de mercados de predicción (Polymarket/Kalshi) que revela información oculta que las interfaces nativas no muestran. El problema central es que los gráficos oficiales de Polymarket agregan ("bucketean") los datos, ocultando movimientos de precio reales, picos de volatilidad y patrones de volumen que son críticos para tomar decisiones de trading informadas.

El autor demuestra en tiempo real cómo, con un único prompt en Claude Code, se genera un script Python (`visualize_market.py`) que consulta la API Gamma de Polymarket, obtiene cada trade individual sin agregar, y produce una visualización interactiva con scatter plot de precios (incluyendo VWAP) y barras de volumen diferenciadas por compra/venta. El resultado revela información que cambia completamente la lectura del mercado: por ejemplo, un mercado que parece haber ido directo a 100% en el gráfico nativo, en realidad tuvo swings de 50 a 77, bajó a 50 y luego subió progresivamente.

La conclusión clave es que, dado que los datos de Polymarket viven en blockchain y son públicos, cualquier trader puede construir estas herramientas con AI sin experiencia en programación, creando una ventaja informacional real sobre quienes solo usan la interfaz oficial.

## Puntos Clave
- Los gráficos nativos de Polymarket y Kalshi **agregan datos**, ocultando volatilidad real, picos de precio y estructura de mercado
- Claude Code puede generar un script funcional de visualización en **5-10 minutos** con un solo prompt, sin experiencia en programación
- El script usa la **API Gamma de Polymarket** para obtener trades individuales (no agregados)
- La visualización resultante incluye: scatter plot de precio YES con tamaño de círculo proporcional al volumen, VWAP, y panel de volumen compra/venta separado
- La interactividad (hover) permite verificar precios exactos en zonas congestionadas de datos
- En el ejemplo del mercado de Irán ($46M de volumen), el gráfico nativo mostraba un máximo de ~29%, mientras que los datos reales mostraban **un spike hasta 45%** — información accionable para estrategias contrarias
- Los datos de Polymarket son **on-chain y públicos**, democratizando el acceso para quien construya las herramientas
- El mismo problema existe en **Kalshi** y otros mercados de predicción

## Conceptos Técnicos Mencionados
- **Claude Code** — Agente de IA desarrollado por Anthropic, de pago, especializado en generación y ejecución de código; permite crear scripts funcionales con prompts en lenguaje natural
- **Polymarket Gamma API** — API de Polymarket que provee datos de trades individuales sin agregación; endpoint recomendado explícitamente en el prompt para evitar confusiones del agente
- **Polymarket** — Mercado de predicción descentralizado on-chain; sus datos son públicamente accesibles por estar en blockchain
- **Kalshi** — Mercado de predicción regulado (competidor de Polymarket) con las mismas limitaciones en su UI
- **visualize_market.py** — Script Python generado por Claude Code para visualizar datos de mercado
- **Scatter plot con tamaño variable** — Técnica de visualización donde el área del punto es proporcional al volumen del trade, permitiendo identificar trades grandes visualmente
- **VWAP (Volume Weighted Average Price)** — Indicador técnico calculado automáticamente por el script generado; precio promedio ponderado por volumen
- **Bucketed trades vs. individual trades** — Distinción entre datos agregados (que ocultan información) y trades granulares individuales; el prompt especifica explícitamente `not bucketed`
- **Vibe coding** — Metodología de desarrollo donde se describe la funcionalidad deseada en lenguaje natural a una IA y esta genera el código, sin escribir código manualmente
- **On-chain data** — Datos almacenados en blockchain, públicamente accesibles y verificables sin depender de APIs privadas

## Fragmentos Relevantes

> "If you're using the normal Polymarket graphs on the site, you might be missing a lot of alpha."

> "It started off in the 50s, bounced all the way to 77, then went all the way back down to 50, and then went up and chopped in the 90s until the settlement at the end of the market. And then there's also a big burst of volume right around this time [...] But, if you're using the normal Polymarket graphs, you would never know any of that."

> "Make sure to get every trade not bucketed. Because also sometimes it comes back with bucketed trades, meaning that it aggregates and we don't want that. We want every trade."

> "On the left-hand side on Polymarket, you can see it didn't even touch 30. Went up to basically 29-28 on the visualization. But, that's because they aggregate it. And the real data, you can see here it actually went all the way up to 45 and then went back down."

> "Because it's on the chain, you can just find the data and plot it. And then you can just find random patterns in data that really a lot of other people cannot get access to just because they don't go and build these scripts."

> "When something goes from, let's say, nine to 10, that's over a 10% gain [...] these are huge swings. Like it doesn't look like it's huge swings."

## Conclusiones y Aprendizajes
- **Prompting estratégico para APIs**: Especificar explícitamente el endpoint (`Gamma API`) y el formato de datos (`every trade not bucketed`) en el prompt evita que el agente tome atajos que degraden la calidad del output.
- **Visualización interactiva como herramienta de QA**: Incluir hover/tooltip en el requerimiento permite verificar que los datos son correctos, especialmente en zonas de alta densidad de puntos.
- **Patrón de desarrollo vibe-coding para herramientas de análisis**: Un prompt bien estructurado (fuente de datos + formato + tipo de gráfico + interactividad) es suficiente para obtener una herramienta funcional sin iteraciones múltiples.
- **Arbitraje de información**: Las ineficiencias de UI de plataformas establecidas crean oportunidades para traders técnicos; construir herramientas propias de visualización es una fuente de ventaja competitiva sostenible.
- **Aplicable a cualquier mercado con API pública**: La misma técnica funciona para Kalshi, mercados de opciones, o cualquier fuente de datos con trades individuales accesibles vía API.
- **Tamaño de círculo como encoding de volumen**: Mejor que barras separadas para detectar clusters de volumen en contexto de precio; técnica replicable en cualquier scatter plot financiero.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code