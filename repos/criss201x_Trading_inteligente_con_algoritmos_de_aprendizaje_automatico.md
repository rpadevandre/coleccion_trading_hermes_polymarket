# Trading inteligente con algoritmos de aprendizaje automático

## Información General
- **Repo:** `criss201x/Trading_inteligente_con_algoritmos_de_aprendizaje_automatico`
- **URL:** https://github.com/criss201x/Trading_inteligente_con_algoritmos_de_aprendizaje_automatico
- **Lenguaje principal:** Python
- **Stars:** 1
- **Última actualización:** 2021-07-21
- **Topics:** ninguno

## Propósito del Repo
Este repositorio implementa un pipeline completo de trading algorítmico inteligente que combina extracción de datos financieros, análisis estadístico y modelos de aprendizaje automático para apoyar la toma de decisiones de inversión. El proyecto cubre todo el flujo desde el web scraping de datos bursátiles hasta la aplicación de algoritmos como Montecarlo, K-Means, GMM, Filtro de Kalman y redes neuronales sobre series temporales de precios.

Está diseñado como un proyecto académico/educativo orientado a analistas financieros, estudiantes de ciencia de datos y desarrolladores interesados en la intersección entre ML y finanzas cuantitativas. Su diferenciación radica en cubrir múltiples etapas del pipeline de forma modular: extracción, procesamiento, análisis de correlación, análisis de sentimiento y modelado predictivo, todo en Python.

## Arquitectura y Patrones Clave
El repositorio sigue una arquitectura de **pipeline ETL financiero por etapas**, donde cada carpeta representa una fase independiente del flujo de datos:

1. **Extracción** → scraping y descarga de datos históricos
2. **Preprocesamiento** → filtrado (Kalman), normalización
3. **Análisis** → correlación entre activos, análisis estadístico
4. **Modelado** → clustering (K-Means, GMM), simulación (Montecarlo), clasificación (redes neuronales)
5. **Señales** → análisis de sentimiento correlacionado con precios

El patrón dominante es el de **scripts independientes por técnica**, sin acoplamiento entre módulos, lo que facilita el estudio individual de cada algoritmo. No hay framework de orquestación; cada `.py` es autocontenido con sus propias cargas de datos.

## Componentes Principales

- **`Extraccion de datos/Extraccion de datos.py`** — Descarga de datos históricos de acciones (probablemente via Yahoo Finance o similar)
- **`Extraccion de datos/filtro de kalman.py`** — Implementación del Filtro de Kalman para suavizado de series de precios y reducción de ruido
- **`Extraccion de datos/procesado de datos.py`** — Limpieza y transformación de datos crudos para consumo por modelos
- **`Analisis de correlacion/Finanzas_en_Wilkipedia.py`** — Web scraping de Wikipedia para obtener lista de empresas del S&P 500 y análisis de correlación entre activos
- **`Analisis de datos financieros/analisis de montecarlo.py`** — Simulación de Montecarlo para estimación de distribuciones de retornos futuros
- **`Analisis de datos financieros/Ejercicio de bolsa por clusterizacion.py`** — Agrupación de acciones por comportamiento usando clustering
- **`Modelos de machine learning aplicados al trading/k-means_aplicado_al_trading.py`** — K-Means para identificar regímenes de mercado o grupos de activos similares
- **`Modelos de machine learning aplicados al trading/gaussian_mixture_model_aplicado_al_trading.py`** — GMM para modelado probabilístico de estados de mercado
- **`Analisis de sentimiento/Analisis_de_sentimiento_basico.py`** — Análisis de sentimiento sobre tweets financieros
- **`Analisis de sentimiento/Analisis_de_sentimiento_y_correlacion.py`** — Correlación entre sentimiento de redes sociales y movimientos de precio
- **`Redes Neuronales/Clasificacion por redes neuronales.py`** — Clasificador neuronal para señales de compra/venta
- **`Redes Neuronales/Preprocesamiento de datos.py`** — Pipeline de features para alimentar la red neuronal
- **`Series temporales/entrenamiento_dataset.py`** — Preparación de datasets temporales con ventanas deslizantes

## Dependencias Clave
Inferidas por el contexto del proyecto (no hay requirements.txt explícito):

- **`pandas` / `numpy`** — Manipulación de series temporales y datos financieros
- **`scikit-learn`** — Implementación de K-Means, GMM y métricas de evaluación
- **`matplotlib`** — Visualización de resultados (assets con 15 figuras generadas)
- **`yfinance` o `pandas-datareader`** — Extracción de datos históricos de mercado
- **`pykalman` o implementación propia** — Filtro de Kalman para suavizado de señales
- **`TextBlob` o `VADER`** — Análisis de sentimiento sobre tweets (archivos `tweets4.csv`, `tweets_en.csv`)
- **`tensorflow`/`keras` o `scikit-learn MLPClassifier`** — Clasificación mediante redes neuronales
- **`beautifulsoup4` / `requests`** — Web scraping de Wikipedia para el S&P 500

## Fragmentos de Código Relevantes

**Flujo conceptual del pipeline (descrito en README):**
```
Extracción de datos (Web Scraping / APIs)
    ↓
Procesado y filtrado (Filtro de Kalman)
    ↓
Análisis estadístico (Correlación, Montecarlo)
    ↓
Modelos ML (K-Means, GMM, Redes Neuronales)
    ↓
Análisis de sentimiento (Twitter)
    ↓
Apoyo a decisión de compra/venta
```

**Estructura típica de script de clustering (patrón inferido de `k-means_aplicado_al_trading.py`):**
```python
# Patrón común en los módulos de ML del repo
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Cargar datos preprocesados
data = pd.read_pickle('StockValues.p')

# Feature engineering: retornos diarios
returns = data.pct_change().dropna()

# Aplicar K-Means para identificar regímenes
kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(returns)

# Visualizar clusters
plt.scatter(returns.iloc[:,0], returns.iloc[:,1], c=labels)
plt.show()
```

**Análisis de correlación del S&P 500 (patrón de `Finanzas_en_Wilkipedia.py`):**
```python
# Web scraping de lista S&P500 desde Wikipedia
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})
tickers = [row.findAll('td')[0].text.strip() 
           for row in table.findAll('tr')[1:]]

# Guardar para reutilización
import pickle
with open("sp500.pickle", "wb") as f:
    pickle.dump(tickers, f)
```

## Conclusiones y Aprendizajes

- **Pipeline por etapas independientes**: la organización por carpetas temáticas (extracción → análisis → modelado) es un patrón limpio y replicable para proyectos de ML financiero educativo.
- **Filtro de Kalman como preprocesador**: usar Kalman antes de aplicar ML reduce el ruido de series financieras, mejorando la calidad de las señales — patrón directamente adoptable.
- **Persistencia con pickle**: usar `.pickle` y `.p` para cachear datos descargados evita llamadas repetidas a APIs externas, patrón útil en desarrollo iterativo.
- **Análisis de sentimiento + precio**: la correlación tweet-precio es una señal complementaria valiosa; el patrón de cruzar datos de redes sociales con series temporales es extensible a otras fuentes (noticias, Reddit).
- **GMM sobre K-Means para regímenes de mercado**: GMM permite identificar estados de mercado con probabilidades suaves (bull/bear/lateral), más robusto que K-Means para datos financieros no esféricos.
- **Montecarlo para gestión de riesgo**: las simulaciones de Montecarlo sobre retornos son un método estándar para calcular VaR (Value at Risk) — patrón directo para cualquier sistema de risk management.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code