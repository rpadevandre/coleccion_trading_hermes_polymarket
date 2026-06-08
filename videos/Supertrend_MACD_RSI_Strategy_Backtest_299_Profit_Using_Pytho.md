# Supertrend + MACD + RSI Strategy | Backtest 299% Profit Using Python & Freqtrade

## Información General
- **Canal:** Quant Tactics
- **Duración:** 8m 10s
- **Idioma detectado:** en
- **Transcripción fuente:** `Supertrend_MACD_RSI_Strategy_Backtest_299_Profit_Using_Pytho.txt`

## Resumen Ejecutivo
El video presenta una estrategia de trading algorítmico que combina tres indicadores técnicos: Supertrend, MACD y RSI. La estrategia es codificada en Python e implementada sobre el framework Freqtrade (bot de trading crypto open-source), donde se optimizan sus parámetros mediante la funcionalidad HyperOpt para maximizar el rendimiento minimizando el drawdown.

El proceso de validación sigue una metodología in-sample/out-of-sample: 8 meses de datos históricos para optimización y 4 meses para validación en datos no vistos, buscando evitar overfitting. El backtest se ejecutó sobre DOT perpetual futures en timeframe de 1 hora con un período total de 1 año.

Los resultados reportados muestran un rendimiento del 299% de ganancia total durante un período en que el activo subyacente cayó un 55%, con un drawdown máximo del 23% y una curva de equity con tendencia alcista sostenida. La estrategia usa gestión de riesgo basada en swing points para stop-loss y un ratio riesgo/recompensa de 1.5:1 para take-profit.

## Puntos Clave
- **Triple confirmación de señal:** Las entradas (long o short) requieren que los tres indicadores estén alineados simultáneamente antes de ejecutar la operación
- **Entry diferido:** La entrada se ejecuta en la siguiente vela tras confirmarse las condiciones, no en la vela de señal
- **Stop-loss dinámico:** Basado en swing lows (long) o swing highs (short) recientes, no en porcentaje fijo
- **Take-profit fijo:** Ratio riesgo/recompensa de 1.5:1 calculado desde la distancia entry-stoploss
- **Optimización con HyperOpt:** Freqtrade busca la combinación óptima de parámetros sobre datos in-sample
- **Validación out-of-sample:** 4 meses de datos no vistos para verificar que los parámetros no están sobreajustados
- **Filtro de vela grande:** Se evitan entradas cuando el tamaño de la vela es excesivo (máximo candle size parameter)
- **RSI como filtro de momentum:** Se usa el nivel 50 como separador bullish/bearish, no los clásicos 30/70

## Conceptos Técnicos Mencionados

| Concepto | Descripción |
|---|---|
| **Supertrend** | Indicador de seguimiento de tendencia que combina precio y volatilidad (ATR); dibuja línea por encima/debajo del precio |
| **MACD** | Moving Average Convergence Divergence; compara dos medias móviles para medir fuerza y dirección del momentum |
| **RSI (Relative Strength Index)** | Oscilador de momentum que mide la fuerza de movimientos recientes; usado aquí con nivel 50 como umbral |
| **Supertrend Length** | Parámetro que define el período de cálculo del Supertrend |
| **Supertrend Multiplier** | Factor multiplicador del ATR en el cálculo del Supertrend |
| **Swing Point Lookback** | Número de velas hacia atrás para identificar swing highs/lows usados como referencia de stop-loss |
| **Risk/Reward Ratio** | Relación entre ganancia objetivo y pérdida máxima aceptada; en esta estrategia 1.5:1 |
| **Freqtrade** | Bot de trading crypto open-source escrito en Python, soporta backtesting, optimización y trading en vivo |
| **HyperOpt** | Feature de Freqtrade para optimización bayesiana/grid search de parámetros de estrategia |
| **In-sample / Out-of-sample split** | Técnica de validación que separa datos históricos en entrenamiento y prueba para detectar overfitting |
| **Perpetual Futures** | Contratos derivados de crypto sin fecha de vencimiento, usados aquí sobre DOT (Polkadot) |
| **Maximum Drawdown** | Caída máxima desde el pico hasta el valle en la curva de equity; reportado en 23% |
| **Equity Curve** | Representación gráfica del capital acumulado a lo largo del tiempo de backtesting |

## Fragmentos Relevantes

> *"When the price closes above the super trend line, it signals that the market might be entering or continuing an uptrend. This is generally considered a bullish signal and could be a good time to look for buy opportunities."*

> *"To enter a long trade, all of the following conditions must be met. One, the closing price must be above the super trend line. Two, the RSI should be above the 50 level, suggesting bullish momentum. Three, the MACD line must be above the MACD signal line, confirming upward momentum."*

> *"To manage risk, we set a stop loss just below the most recent swing low. This helps protect the trade while giving it enough space to breathe through normal market fluctuations. For take profit, we apply a 1.5 to 1 risk-reward ratio."*

> *"We'll test the strategy on a 1-hour time frame and split our historical data into two parts. In sample data, 8 months [...] tested on four months of out-of-sample data to ensure that it performs well on unseen data and is not overfitting to past trends."*

> *"The strategy delivered a total profit of 299%. During the same period, the market itself declined by 55%. Highlighting the strength and effectiveness of this approach in bearish conditions. The maximum drawdown was 23%."*

> *"We're going to optimize several key parameters: Super trend length and super trend multiplier, RSI threshold, testing values like 50, 55, and 60. Maximum candle size [...] Swing point look back [...] Risk-reward ratio."*

## Conclusiones y Aprendizajes

**Aplicables directamente a un proyecto de trading algorítmico:**

1. **Estructura de triple confirmación:** Implementar un sistema donde señales de múltiples indicadores deben coincidir reduce las entradas falsas. Patrón replicable con cualquier combinación de indicadores.

2. **Gestión de riesgo basada en estructura de mercado:** Colocar el stop-loss en swing highs/lows en lugar de porcentajes fijos adapta el riesgo a la volatilidad actual del activo.

3. **Pipeline de optimización riguroso:** El split in-sample/out-of-sample es una práctica fundamental para cualquier sistema backtestado; debe ser siempre la metodología base antes de considerar un sistema como válido.

4. **Filtro de tamaño de vela:** Añadir un filtro que descarte entradas en velas de gran tamaño es una técnica simple y efectiva para mejorar la calidad del entry.

5. **RSI como filtro de sesgo:** Usar el nivel 50 del RSI como filtro binario (bullish/bearish) es un uso no convencional pero limpio para alinear trades con el momentum dominante.

6. **Freqtrade como infraestructura:** Para proyectos de trading en Python, Freqtrade ofrece backtesting, optimización (HyperOpt) y ejecución en vivo en un solo framework open-source, eliminando la necesidad de construir esa infraestructura desde cero.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code