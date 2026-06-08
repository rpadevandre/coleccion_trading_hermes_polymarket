# MiroFish

## Información General
- **Repo:** `666ghj/MiroFish`
- **URL:** https://github.com/666ghj/MiroFish
- **Lenguaje principal:** Python
- **Stars:** 65,211
- **Última actualización:** 2026-05-24
- **Topics:** agent-memory, financial-forecasting, future-prediction, knowledge-graph, llms, multi-agent-simulation, public-opinion-analysis, python3, social-prediction, swarm-intelligence

## Propósito del Repo
MiroFish es un motor de inteligencia de enjambre (swarm intelligence) de próxima generación que utiliza tecnología multi-agente para construir mundos digitales paralelos de alta fidelidad a partir de información semilla del mundo real (noticias, señales financieras, borradores de políticas). Miles de agentes con personalidades independientes, memoria a largo plazo y lógica conductual interactúan libremente para modelar evolución social y predecir trayectorias futuras. La propuesta de valor es permitir "ensayar el futuro en un sandbox digital".

Lo diferencia de otros sistemas de predicción su arquitectura de emergencia colectiva: en lugar de modelos estadísticos clásicos, captura el comportamiento emergente que surge de interacciones individuales a escala. Está diseñado tanto para analistas de decisiones (gobiernos, empresas) como para investigadores que quieran simular dinámica social, opinión pública, mercados financieros o incluso narrativas literarias.

## Arquitectura y Patrones Clave
El sistema sigue una arquitectura **full-stack desacoplada**: backend Python (Flask/FastAPI) expuesto en el puerto 5001 y frontend Vue.js en el puerto 3000, orquestados mediante `concurrently` en modo desarrollo o Docker Compose en producción.

La capa de agentes combina tres patrones fundamentales:
- **Agent Memory con grafo de conocimiento**: integración con **Zep** para memoria persistente a largo plazo de cada agente, permitiendo que recuerden interacciones previas y mantengan coherencia temporal.
- **Simulación paralela**: el script `run_parallel_simulation.py` indica que múltiples agentes se ejecutan concurrentemente, probablemente con asyncio o threading.
- **LLM como motor de razonamiento**: cada agente usa un LLM (compatible con OpenAI SDK) para generar sus respuestas, con soporte para un LLM "boost" secundario para tareas de alta frecuencia.
- **Scripts de simulación especializados**: simulaciones dedicadas para Twitter, Reddit y casos generales, sugiriendo un patrón de estrategia para distintos dominios sociales.

## Componentes Principales
- **`backend/app/api/`** — Endpoints REST que exponen las capacidades de simulación y predicción al frontend
- **`backend/app/models/`** — Modelos de datos para agentes, simulaciones y resultados
- **`backend/app/services/`** — Lógica de negocio: orquestación de agentes, integración LLM, gestión de memoria
- **`backend/app/utils/`** — Utilidades auxiliares (logging, helpers de API, procesamiento de datos)
- **`backend/scripts/run_parallel_simulation.py`** — Motor de simulación paralela principal
- **`backend/scripts/run_twitter_simulation.py`** — Simulación especializada para dinámicas de Twitter/X
- **`backend/scripts/run_reddit_simulation.py`** — Simulación especializada para dinámicas de Reddit
- **`backend/scripts/action_logger.py`** — Registro y trazabilidad de acciones de agentes
- **`frontend/src/views/`** — Vistas Vue.js para interfaz de usuario (configuración de simulación, dashboards)
- **`frontend/src/store/`** — Estado global Vuex/Pinia de la aplicación
- **`frontend/src/i18n/`** — Internacionalización (inglés y chino manifiesto en `locales/`)
- **`backend/app/config.py`** — Configuración centralizada que lee variables de entorno

## Dependencias Clave
- **LLM API (OpenAI SDK compatible)** — Motor de razonamiento de cada agente; compatible con cualquier proveedor (Alibaba Qwen, OpenAI, etc.)
- **Zep** — Grafo de memoria persistente para agentes; almacena y recupera contexto a largo plazo de cada entidad
- **uv** — Gestor de paquetes y entornos Python ultrarrápido (reemplaza pip/poetry)
- **Vue.js + Vite** — Frontend reactivo con hot-reload para visualización de simulaciones
- **Docker / Docker Compose** — Contenedorización para despliegue reproducible en un solo comando
- **concurrently** — Ejecución simultánea de procesos backend y frontend en desarrollo

## Fragmentos de Código Relevantes

**1. Configuración de entorno — Dual LLM setup con memoria Zep:**
```env
# Motor principal de razonamiento de agentes
LLM_API_KEY=your_api_key_here
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

# Grafo de memoria persistente para agentes
ZEP_API_KEY=your_zep_api_key_here

# LLM secundario de alta velocidad (opcional, para paralelismo)
LLM_BOOST_API_KEY=your_api_key_here
LLM_BOOST_BASE_URL=your_base_url_here
LLM_BOOST_MODEL_NAME=your_model_name_here
```

**2. Orquestación de servicios — Arquitectura desacoplada en Docker:**
```yaml
services:
  mirofish:
    image: ghcr.io/666ghj/mirofish:latest
    ports:
      - "3000:3000"   # Frontend Vue.js
      - "5001:5001"   # Backend Python API
    volumes:
      - ./backend/uploads:/app/backend/uploads
```

**3. Build multi-stage — Python + Node en un solo contenedor:**
```dockerfile
FROM python:3.11
# Instala Node.js para el frontend
RUN apt-get install -y nodejs npm

# Usa uv para gestión de dependencias Python
COPY --from=ghcr.io/astral-sh/uv:0.9.26 /uv /uvx /bin/

# Instala dependencias Node y Python en capas cacheadas
RUN npm ci && npm ci --prefix frontend \
  && cd backend && uv sync --frozen

CMD ["npm", "run", "dev"]  # concurrently lanza ambos servicios
```

## Conclusiones y Aprendizajes

1. **Patrón Dual-LLM**: separar un LLM principal (alta calidad, menor velocidad) de un LLM "boost" (alta velocidad) permite optimizar costo/latencia según la criticidad de cada llamada — patrón directamente adoptable en sistemas multi-agente propios.

2. **Zep como capa de memoria de agentes**: en lugar de reinventar almacenamiento de contexto, delegar la memoria persistente con grafo de conocimiento a Zep simplifica enormemente la arquitectura y permite queries semánticas sobre el historial de cada agente.

3. **Scripts de simulación por dominio**: el patrón de tener scripts especializados (`run_twitter_simulation.py`, `run_reddit_simulation.py`) con una base común (`run_parallel_simulation.py`) implementa el patrón **Strategy** limpiamente para distintos contextos sociales.

4. **uv para gestión de dependencias Python en CI/CD**: el uso de `uv sync --frozen` en Docker garantiza reproducibilidad y velocidad de instalación, siendo un reemplazo moderno y superior a pip-tools o poetry para proyectos en producción.

5. **Contenedor multi-runtime**: alojar Python y Node.js en el mismo contenedor con puertos separados es una estrategia pragmática para proyectos full-stack pequeños-medianos que evita la complejidad de orquestar múltiples servicios.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code