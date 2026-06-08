# How I Develop Trading Strategies | Permutation Tests and Trading Strategy Development with Python

## Información General
- **Canal:** neurotrader
- **Duración:** 21m 54s
- **Idioma detectado:** English
- **Transcripción fuente:** `How_I_Develop_Trading_Strategies_Permutation_Tests_and_Tradi.txt`

## Resumen Ejecutivo

El video presenta un framework de cuatro pasos para desarrollar y validar estrategias de trading algorítmico, usando como ejemplo la estrategia Donchian Channel Breakout sobre datos horarios de Bitcoin. Los cuatro pasos son: (1) excelencia in-sample, (2) in-sample Monte Carlo permutation test, (3) walk forward test, y (4) walk forward Monte Carlo permutation test. El autor enfatiza que este proceso es genérico y aplicable a casi cualquier estrategia, desde simples cruces de medias móviles hasta redes neuronales complejas.

El concepto central es el uso de **permutation tests** para distinguir si la buena performance in-sample de una estrategia proviene de patrones reales en los datos o simplemente de data mining bias. La idea clave: si una estrategia optimizada lo hace tan bien —o mejor— sobre datos permutados (ruido con propiedades estadísticas similares al original) como sobre los datos reales, entonces la estrategia probablemente es basura. El null hypothesis es que la estrategia no tiene valor, y el permutation test es el mecanismo para rechazarlo.

El autor también articula por qué no basta con probar en datos out-of-sample directamente: cada vez que se reutiliza un dataset de validación para comparar estrategias, se acumula selection bias, corrompiendo gradualmente lo que se considera "out of sample". El permutation test funciona como un filtro previo que consume resources computacionales pero preserva la integridad del dataset de validación real.

## Puntos Clave

- **4 pasos obligatorios:** in-sample excellence → in-sample permutation test → walk forward test → walk forward permutation test
- **Bar-level returns vs trade-level returns:** usar retornos granulares por barra (no por trade) hace que los objective functions sean más estables y estén alimentados con más datos
- **Null hypothesis:** la estrategia es basura; el permutation test intenta refutarlo
- **P-value thresholds:** < 1% para in-sample permutation test; < 5% para walk forward sobre 1 año de datos; < 1% para walk forward sobre 2+ años
- **Mínimo de permutaciones:** 1,000 para in-sample; 200 para walk forward (es computacionalmente costoso)
- **El permutation test preserva propiedades estadísticas:** mismo mean, std, skew y kurtosis en los retornos; preserva correlación entre mercados si se permutar juntos
- **Flaw del algoritmo de permutación:** destruye volatility clustering y long memory, lo que puede generar un optimistic bias; si la estrategia depende de esas propiedades, hay que tenerlo en cuenta
- **Optimizar lookbacks rara vez generaliza bien:** el autor prefiere encontrar un "stable lookback" donde un rango amplio de valores funcione decentemente, y fijarlo
- **El out-of-sample se corrompe con el uso:** una vez que usas un dataset para comparar estrategias, ya no es verdaderamente out-of-sample; es un validation set con selection bias acumulado
- **Donchian Channel con lookback optimizado falló el walk forward permutation test:** P-value de 22%, lo que indica que los resultados podrían ser azar
- **Decision tree sobreajustado:** pasó el in-sample pero falló el permutation test de forma contundente, demostrando que el test detecta overfitting severo

## Conceptos Técnicos Mencionados

- **Donchian Channel Breakout:** Estrategia de trend-following que va long cuando el close es el máximo del lookback y short cuando es el mínimo; captura breakouts de rango
- **Moving Average Crossover:** Estrategia baseline mencionada como ejemplo inicial, descartada por ser "mediocre"
- **Profit Factor:** Objective function principal usado (suma de ganancias / suma de pérdidas); más estable que Sharpe cuando se computa sobre retornos por barra
- **Sharpe Ratio:** Mencionado como alternativa de objective function para evaluar estrategias
- **Bar-level returns:** Retornos calculados a la granularidad de cada barra (no por trade), obtenidos multiplicando el signal de posición por los retornos desplazados un bar forward
- **Monte Carlo Permutation Test:** Técnica estadística para generar distribución de resultados bajo null hypothesis, optimizando la estrategia sobre múltiples permutaciones del precio
- **Walk Forward Test / Walk Forward Optimization:** Metodología donde se reoptimiza la estrategia periódicamente (cada 30 días en el ejemplo) usando solo datos pasados, y se evalúa en datos futuros no vistos
- **Walk Forward Permutation Test:** Variante del permutation test aplicada después del primer training fold; solo permuta los datos posteriores al período de entrenamiento inicial
- **Grid Search / Parameter Optimization:** Búsqueda exhaustiva del mejor valor de lookback (o cualquier hiperparámetro) sobre los datos de entrenamiento
- **Decision Tree Classifier:** Modelo de ML usado como ejemplo de estrategia sobreajustada; con `min_samples_leaf` muy bajo garantiza overfitting
- **Log Returns / Log Prices:** Uso de logaritmos para retornos, permitiendo sumar returns acumulados en lugar de multiplicarlos
- **Cumulative Sum of Log Returns:** Aproximación de backtest acumulativo como suma de retornos logarítmicos por barra
- **Bar permutation algorithm:** Función que shuffle intrabar quantities (high/low/close relativo al open) y gaps (open relativo al close anterior) de forma separada, preservando propiedades estadísticas mientras destruye estructura temporal
- **Volatility Clustering:** Propiedad de precios reales (varianza no constante en el tiempo) que el algoritmo de permutación destruye
- **Long Memory:** Propiedad de series financieras reales (autocorrelaciones persistentes) también destruida por la permutación
- **Selection Bias / Data Mining Bias:** Sesgos estadísticos producidos por seleccionar el mejor resultado entre múltiples configuraciones o estrategias
- **Quasi P-value:** Proporción de permutaciones que logran igual o mejor objective function que la estrategia real; interpretado como probabilidad de que los resultados sean por azar

## Fragmentos Relevantes

> *"by having a return for each bar instead of each trade objective functions are fed much more data and the calculations and results are much more stable"*

> *"our null hypothesis is that our strategy is garbage. We will use the in-sample Monte Carlo permutation test to disprove our null hypothesis"*

> *"if our strategy is trash then its in-sample performance will be entirely due to data mining bias"*

> *"once out-of-sample data is used even once it is no longer truly out of sample"*

> *"every time we reuse out-of-sample data or rather validation data the selection bias is adding up. This is why we use the in-sample permutation test — we can detect that our idea is bad before we waste the out-of-sample data"*

> *"don't treat that like a target. This is a measure — if a measure becomes a target it is no longer a good measure"*

> *"I will not use a trading strategy if it did not have very low P values for both the in-sample and walk forward permutation test"*

> *"when dealing with strategies that require a look back I find a stable look back value meaning a large variety of look backs have decent performance then I pick a reasonable look back value and stick with it"*

> *"no process is bulletproof — if you are irresponsible with your development process no amount of fancy tests can save you"*

## Conclusiones y Aprendizajes

**Aplicables directamente en proyectos de trading algorítmico:**

1. **Implementar bar-level returns como estándar:** En lugar de calcular métricas por trade, calcular retornos multiplicando el vector de posición por los retornos del siguiente bar. Esto estabiliza cualquier objective function.

2. **Implementar el pipeline de 4 pasos como checklist obligatorio** antes de considerar live trading cualquier estrategia: no avanzar al siguiente paso si el anterior falla.

3. **Codificar el bar permutation algorithm** como utilidad reutilizable: shuffle separado de intrabar quantities y gaps, preservando el open del primer bar y el close del último (tendencia general intacta).

4. **Usar P-value < 1% como filtro de entrada** para el in-sample permutation test, pero no como target a optimizar; si se manipula la estrategia para pasar el test, el test pierde validez.

5. **Separar el dataset de validación final y no tocarlo** hasta tener estrategias que pasaron ambos permutation tests; cada comparación sobre ese dataset acumula selection bias.

6. **En walk forward:** reoptimizar con la frecuencia máxima que permita el tiempo de cómputo; el autor usa 30 días con una ventana de entrenamiento de 4 años.

7. **Para estrategias con lookbacks:** en lugar de optimizar el lookback, buscar la zona de estabilidad del parámetro (donde un rango amplio funciona) y fijar un valor razonable dentro de esa zona.

8. **El permutation test es genérico:** puede aplicarse no solo a profit factor sino a cualquier hipótesis sobre el mercado (e.g., porcentaje de veces que el precio rebota en una media móvil).

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code