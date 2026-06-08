# Polymarket 5 Min Claude Code Bot are NUTS

## Información General
- **Canal:** Moon Dev
- **Duración:** 12m 5s
- **Idioma detectado:** Inglés
- **Transcripción fuente:** `Polymarket_5_Min_Claude_Code_Bot_are_NUTS.txt`

## Resumen Ejecutivo
El video muestra cómo Moon Dev está construyendo bots de trading automatizados para los mercados de 5 minutos de Polymarket, utilizando Claude Code como asistente de desarrollo. El creador exhibe resultados de sus bots operando 24/7 con ganancias del 150% al 669% en operaciones individuales mientras dormía, destacando la ventaja de automatizar frente al trading emocional manual.

El punto central técnico del video es el descubrimiento de cómo hacer **backtesting en los mercados de 5 minutos de Polymarket**: la clave está en obtener datos de 1 minuto y usar el precio al inicio de cada ventana de 5 minutos como "precio a vencer", luego verificar si el precio al final del período lo superó o no. A partir de este framework, el autor probó múltiples estrategias y encontró tres con resultados positivos, entre ellas una basada en MACD (3, 15, 3) con 60% de win rate en 104,000 trades anuales.

El segundo concepto técnico relevante es el uso de **CVD (Cumulative Volume Delta)** calculado a partir de **tick data** (cada cambio de precio individual), en contraste con los típicos datos OHLCV de 1 o 5 minutos. El autor argumenta que toda la alpha real está en el tick data y en el análisis de flujo de órdenes, información que los datos de barras convencionales ocultan.

## Puntos Clave
- Los bots de 5 minutos en Polymarket operan 288 veces por día, lo que da una enorme cantidad de señales estadísticas
- **Cómo hacer backtest en Polymarket mercados de 5 min:** tomar el precio al inicio de la ventana de 5 minutos como benchmark y comparar con el precio al cierre de esa misma ventana
- Se necesita **datos de 1 minuto** para poder hacer backtesting en estos mercados
- Estrategia MACD (3, 15, 3) mostró 60% de win rate (~287 trades/día) — posiblemente overfitted
- Se realizó stress test, walk-forward analysis y validación adicional sobre las 3 estrategias encontradas
- **CVD (Cumulative Volume Delta)** calculado sobre tick data es un indicador de presión de flujo de órdenes que no se puede ver con datos OHLCV
- El tick data registra cada trade individual con su lado (compra/venta) y tamaño
- Una CVD ascendente indica compradores agresivos levantando el ask; descendente indica vendedores golpeando el bid
- El autor afirma pagar 0% de fees y solo comprar en deals (vs. ~3% round trip en la interfaz normal)
- El código del bot CVD de 5 minutos se comparte al final del video (scrolling)

## Conceptos Técnicos Mencionados

- **Polymarket 5-minute markets** — Mercados de predicción con ventanas de resolución de 5 minutos, 288 por día en Bitcoin
- **Claude Code** — Herramienta de IA de Anthropic usada para construir y automatizar los bots de trading
- **Backtesting** — Proceso de validar una estrategia de trading contra datos históricos antes de operar en vivo
- **Walk-forward analysis** — Técnica de validación de estrategias que evita overfitting testeando en períodos fuera de muestra de forma secuencial
- **Stress testing** — Prueba de robustez de una estrategia bajo condiciones extremas o variaciones de parámetros
- **MACD (3, 15, 3)** — Moving Average Convergence Divergence con parámetros cortos, usado como señal de entrada en uno de los bots
- **CVD (Cumulative Volume Delta)** — Indicador que acumula la diferencia entre volumen comprador y vendedor a lo largo del tiempo; revela presión de flujo de órdenes
- **Tick data** — Datos de cada transacción individual (precio, tamaño, lado buy/sell), más granulares que cualquier barra OHLCV
- **Intra-bar data** — Información que ocurre dentro de una barra de tiempo (ej. dentro del minuto), no visible en datos OHLCV estándar
- **Order flow** — Análisis de la dirección y agresividad de las órdenes en el mercado, derivado del tick data
- **OHLCV data** — Open, High, Low, Close, Volume; formato estándar de datos de mercado considerado insuficiente para capturar alpha en tick level
- **HyperLiquid API** — Plataforma/API usada para obtener tick data en tiempo real
- **1-minute data** — Datos de velas de 1 minuto, mínimo necesario para backtesting de mercados de 5 minutos en Polymarket

## Fragmentos Relevantes

> *"The way these work is at 12:15, what happens at the price it is at 12:15, it starts that price. That's the price to beat. Okay, if you know the price to beat at 12:15, well, all you need is 1-minute data."*

> *"CVD is cumulative volume delta — is a total of difference between buying volume and selling volume over time. When a trade executes at the ask price, it's counted as a buy. At the bid, it's a sell."*

> *"A rising CVD means buyers are more aggressive lifting the ask while a falling CVD means sellers are hitting the bid. It reveals order flow pressure that price alone doesn't show."*

> *"MACD 3 15 and 3 — you can see the win rate is 60%. 60% on a market that is trading 288 times a day is dirty."*

> *"All the big head quants out there, they're not going to tell you this. They're not going to tell you that all the alpha is actually in the tick data."*

> *"If there's 288 trades a day and it's taking 287, that's crazy. That's probably overfit."*

## Conclusiones y Aprendizajes

1. **Framework de backtesting para mercados de ventana fija:** El patrón precio-inicio como benchmark es directo de implementar. En cualquier mercado con resolución por comparación de precio inicial vs final, el backtest se reduce a: obtener precio en T=0, obtener precio en T=N, comparar con la señal predicha.

2. **CVD como feature de ML/trading:** Implementar un acumulador de CVD sobre tick data es relativamente sencillo — iterar sobre trades, sumar volumen si es buy, restar si es sell. Puede usarse como feature adicional en modelos predictivos donde OHLCV no es suficiente.

3. **Tick data vs OHLCV:** Para estrategias de alta frecuencia (5 min o menos), considerar seriamente incorporar tick data como fuente de señales. La información intra-barra puede ser la diferencia entre una estrategia con edge real y una sin ella.

4. **Validación de estrategias:** El autor menciona explícitamente walk-forward y stress test además del backtest simple. En proyectos de bots, no basta con backtest in-sample; implementar validación out-of-sample es crítico antes de live trading.

5. **Alta frecuencia de señales = ventaja estadística:** 288 trades/día significa que una estrategia con 60% win rate tiene resultados estadísticamente significativos mucho más rápido que en mercados diarios. Esto hace que Polymarket 5-min sea un buen laboratorio de experimentación.

6. **Usar Claude Code para construcción rápida de bots:** El workflow mostrado (idea → backtest con Claude Code → automatización) es un pipeline replicable para cualquier proyecto de trading algorítmico.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code