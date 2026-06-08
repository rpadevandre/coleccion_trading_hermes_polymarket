# Machine-Learning-for-Algorithmic-Trading-Bots-with-Python

## Información General
- **Repo:** `PacktPublishing/Machine-Learning-for-Algorithmic-Trading-Bots-with-Python`
- **URL:** https://github.com/PacktPublishing/Machine-Learning-for-Algorithmic-Trading-Bots-with-Python
- **Lenguaje principal:** Jupyter Notebook
- **Stars:** 405
- **Última actualización:** 2025-12-15
- **Topics:** (ninguno)

## Propósito del Repo
Este repositorio acompaña el curso de video de Packt Publishing *"Machine Learning for Algorithmic Trading Bots with Python"*. Su objetivo es enseñar a desarrolladores y científicos de datos con conocimientos básicos de Python cómo construir bots de trading algorítmico integrando técnicas de machine learning clásicas y modernas (Random Forests, Gradient Boosting, SVR, modelos bayesianos) sobre datos financieros reales de bolsa, forex y criptomonedas.

El repositorio se diferencia por combinar, de forma didáctica y progresiva, el flujo completo de un proyecto de trading cuantitativo: desde la obtención y análisis de datos hasta el backtesting con Zipline, la gestión de riesgo con VaR/CVaR y el despliegue de estrategias ejecutables. Está diseñado tanto para quienes buscan entrar al sector financiero como para profesionales que quieren automatizar estrategias de inversión con ML.

## Arquitectura y Patrones Clave
El proyecto está organizado por **secciones del curso** (section 0001 a section 0006), cada una con notebooks Jupyter y, en las secciones avanzadas (5 y 6), scripts Python ejecutables desde Eclipse IDE. Las secciones reflejan una progresión pedagógica:

1. **Exploración y evaluación de estrategias base** (buy & hold, autocorrelación)
2. **Modelos supervisados progresivos**: Random Forest → Gradient Boosting → SVR
3. **Backtesting con Zipline**: los `Eclipse Projects` contienen `main.py` + `extension.py` con estrategias ejecutables en el motor de backtesting de Zipline
4. **Gestión de riesgo cuantitativo**: cálculo de VaR bayesiano y CVaR con modelos ML
5. **Persistencia de modelos**: uso de `joblib` para serializar estimadores entrenados (`rf_regressor.joblib`, `estimator.joblib`)

El patrón dominante es **script modular por estrategia**: cada estrategia vive en su propio archivo dentro de `strategies/` (e.g., `scalping.py`, `buy_and_hold.py`, `calendar.py`, `auto_correlation.py`) y se orquesta desde `main.py` mediante `run_zipline.py`.

## Componentes Principales

- **`section 0001/`** — Notebooks de obtención de datos financieros y evaluación de estrategia base (buy & hold)
- **`section 0002/`** — Implementación y evaluación de Random Forest Regressor para predicción de precios; incluye modelo serializado (`rf_regressor.joblib`)
- **`section 0003/`** — Evaluación de estrategia con métricas de performance (`performance.csv`)
- **`section 0004/`** — Implementación de Gradient Boosting con Python
- **`section 0005/`** — Estrategia de scalping y su evaluación (`scalping.csv`)
- **`section 0006/`** — Sección avanzada: VaR bayesiano, CVaR con escalping, implementación de VaR con SVR; incluye modelo entrenado (`estimator.joblib`) y múltiples notebooks de evaluación
- **`section 0006/strategies/`** — Módulo de estrategias Zipline: `scalping.py`, `buy_and_hold.py`, `auto_correlation.py`, `calendar.py`, `run_zipline.py`
- **`Eclipse Projects/`** — Proyectos ejecutables por sección con `main.py` y `extension.py` para correr backtests en Zipline desde Eclipse
- **`buy_and_hold.py`** — Implementación standalone de la estrategia de referencia buy & hold
- **`Lecture Notebooks/`** — Copia alternativa de notebooks organizada como material de clase

## Dependencias Clave

- **Zipline** — Motor de backtesting event-driven; ejecuta las estrategias de trading simulando el mercado histórico tick a tick
- **scikit-learn** — Implementación de Random Forest Regressor, Gradient Boosting y SVR para predicción de precios y gestión de riesgo
- **joblib** — Serialización/deserialización de modelos ML entrenados para reutilización sin re-entrenamiento
- **pandas / numpy** — Manipulación de series temporales financieras y cálculo de métricas
- **PyMC3 / arviz** (inferido por la sección de VaR bayesiano) — Modelado probabilístico para estimación bayesiana del Value at Risk
- **Jupyter Notebook** — Entorno principal de exploración, visualización y narrativa del proceso de análisis

## Fragmentos de Código Relevantes

**1. Estructura de estrategia en Zipline (patrón típico de `main.py`)**
```python
# Eclipse Projects/Section 6B/main.py (estructura inferida)
from strategies.scalping import initialize, handle_data
from strategies.run_zipline import run_strategy

if __name__ == '__main__':
    run_strategy(initialize, handle_data, start='2017-01-01', end='2018-01-01')
```

**2. Módulo de estrategia de scalping (patrón `strategies/scalping.py`)**
```python
# section 0006/strategies/scalping.py
def initialize(context):
    context.asset = symbol('BTCUSDT')
    context.threshold = 0.001

def handle_data(context, data):
    price = data.current(context.asset, 'price')
    # lógica de entrada/salida basada en movimientos de micro-precio
    if condicion_entrada:
        order_target_percent(context.asset, 1.0)
    elif condicion_salida:
        order_target_percent(context.asset, 0.0)
```

**3. Persistencia de modelo ML con joblib**
```python
# Entrenamiento y guardado (sección 2)
from sklearn.ensemble import RandomForestRegressor
from joblib import dump, load

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)
dump(model, 'rf_regressor.joblib')

# Reutilización en backtesting (sección 6)
model = load('estimator.joblib')
predictions = model.predict(X_live)
```

## Conclusiones y Aprendizajes

- **Patrón de separación estrategia/ejecución**: Encapsular cada estrategia en su propio módulo (`scalping.py`, `buy_and_hold.py`) y orquestar desde un `main.py` permite testear estrategias de forma aislada y comparativa — adoptable directamente en proyectos de trading propio.
- **Progresión de complejidad del modelo**: La arquitectura del curso (RF → GBoosting → SVR → Bayesiano) demuestra cómo elevar gradualmente la sofisticación del estimador sin cambiar el pipeline de backtesting — un patrón útil para experimentación sistemática.
- **Gestión de riesgo integrada en el pipeline**: Incluir métricas de CVaR/VaR como parte del ciclo de evaluación (no como post-proceso) es una práctica de ingeniería financiera que puede adoptarse en cualquier sistema de trading automatizado.
- **Serialización de modelos para producción**: Usar `joblib` para separar fase de entrenamiento de fase de inferencia es esencial cuando el modelo alimenta una estrategia en tiempo real — evita re-entrenamiento costoso en cada ejecución.
- **Backtesting estructurado**: El uso de Zipline con `initialize`/`handle_data` como contratos de interfaz obliga a pensar en estrategias como componentes intercambiables, lo que facilita la comparación objetiva de performance.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code