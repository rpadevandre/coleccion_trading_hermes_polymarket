# Fincept Terminal

## Información General
- **Repo:** `Fincept-Corporation/FinceptTerminal`
- **URL:** https://github.com/Fincept-Corporation/FinceptTerminal
- **Lenguaje principal:** C++
- **Stars:** 25,895
- **Última actualización:** 2026-06-05
- **Topics:** ai-agents, algorithmic-trading, bloomberg-terminal, cpp, finance, financial-markets, fintech, good-first-issue, investment, investment-research, machine-learning, opensource, python, qt, quantitative-finance, stock-market, trading

## Propósito del Repo
Fincept Terminal es una aplicación de escritorio moderna orientada a finanzas, diseñada como alternativa open-source al Bloomberg Terminal. Ofrece herramientas de análisis de mercados, investigación de inversiones, datos económicos, trading algorítmico y agentes de IA, todo dentro de una interfaz gráfica interactiva construida con Qt6 y C++20, con Python como motor de scripting y análisis.

Está diseñado para traders, quants, analistas financieros e inversores individuales que necesitan acceso a capacidades de nivel institucional sin los costes prohibitivos de terminales comerciales. Su diferenciador clave es la combinación de un frontend nativo de alto rendimiento (C++/Qt6), un backend de scripting extensible (Python) y soporte nativo para agentes de IA, trading algorítmico y conexión a wallets cripto.

## Arquitectura y Patrones Clave
La arquitectura es **híbrida C++/Python en capas**, con separación clara entre el core de la aplicación (C++20 + Qt6) y los scripts de análisis/agentes (Python). El frontend gráfico reside completamente en C++/Qt6, mientras que la lógica de dominio financiero compleja (AI agents, quantitative analysis, trading algorithms) se delega a scripts Python embebidos.

Patrones arquitectónicos notables:
- **Multi-stage Docker build**: construcción determinista y reproducible con soporte multi-arquitectura (amd64/arm64) usando BuildKit.
- **Separación por dominio**: cada funcionalidad financiera tiene su propio módulo (`algo_engine`, `datahub`, `trading`, `auth`, `mcp`), siguiendo principios de bajo acoplamiento.
- **Bridge C++/Python**: el directorio `src/python/` actúa como capa de integración entre el runtime C++ y los scripts Python.
- **ADR (Architecture Decision Records)**: el proyecto documenta decisiones arquitectónicas formalmente en `docs/adr/`.
- **CMake Presets**: configuración de build estandarizada con `CMakePresets.json` para diferentes entornos.
- **Packaging multiplataforma**: scripts dedicados para Flatpak (Linux), instaladores Windows/macOS, todos automatizados vía GitHub Actions.

## Componentes Principales

- **`fincept-qt/src/app/`** — Punto de entrada de la aplicación Qt, inicialización del main window y ciclo de eventos
- **`fincept-qt/src/core/`** — Núcleo de la aplicación: gestión de estado, configuración y servicios fundamentales
- **`fincept-qt/src/screens/`** — Pantallas/vistas de la UI (dashboard, mercados, portfolio, etc.)
- **`fincept-qt/src/ui/`** — Componentes reutilizables de interfaz gráfica (widgets custom, layouts)
- **`fincept-qt/src/algo_engine/`** — Motor de trading algorítmico y backtesting
- **`fincept-qt/src/datahub/`** — Capa de ingesta y normalización de datos financieros de múltiples fuentes
- **`fincept-qt/src/trading/`** — Módulo de órdenes, ejecución y conexión a brokers (ej. AngelOne)
- **`fincept-qt/src/auth/`** — Autenticación y gestión de sesiones de usuario
- **`fincept-qt/src/mcp/`** — Implementación del protocolo MCP (Model Context Protocol) para agentes de IA
- **`fincept-qt/src/network/`** — Capa HTTP/WebSocket para llamadas a APIs externas
- **`fincept-qt/src/python/`** — Bridge de integración Python embebido en el runtime C++
- **`fincept-qt/src/services/`** — Servicios de aplicación (notificaciones, caché, persistencia)
- **`fincept-qt/src/storage/`** — Capa de almacenamiento local (SQLite u similar)
- **`fincept-qt/scripts/agents/`** — Agentes de IA para investigación y análisis autónomo
- **`fincept-qt/scripts/agno_trading/`** — Scripts de trading con el framework Agno
- **`fincept-qt/scripts/ai_quant_lab/`** — Laboratorio cuantitativo con ML/AI
- **`fincept-qt/scripts/alpha_arena/`** — Plataforma de competición de estrategias alpha
- **`fincept-qt/scripts/vision_quant/`** — Análisis cuantitativo basado en visión/charts
- **`fincept-qt/scripts/voice/`** — Interfaz de voz para control del terminal
- **`fincept-qt/scripts/mcp/`** — Herramientas MCP para integración con LLMs externos
- **`fincept-qt/scripts/technicals/`** — Indicadores técnicos y análisis chartista
- **`fincept-qt/resources/`** — Assets: íconos, charts, notebooks Jupyter, demo portfolio

## Dependencias Clave

- **Qt 6.8.3** — Framework UI: rendering gráfico, event loop, WebSockets (`qtwebsockets`), multimedia (`qtmultimedia`), charts (`qtcharts`)
- **C++20** — Lenguaje base para performance y features modernas (concepts, ranges, coroutines)
- **Python 3.11+** — Runtime embebido para scripts de análisis, agentes de IA y extensiones
- **CMake 3.27+** — Sistema de build con soporte para presets y multi-plataforma
- **aqtinstall** — Instalación automatizada de Qt en pipelines CI/CD
- **GCC 13 / Clang** — Compiladores soportados (clang-format y clang-tidy para calidad de código)
- **Agno Framework** — Framework para agentes de trading autónomos (scripts/agno_trading)
- **Docker BuildKit** — Containerización multi-arch para distribución y desarrollo reproducible

## Fragmentos de Código Relevantes

**1. Estrategia de build multi-arquitectura en Docker:**
```dockerfile
# Resolución de arquitectura en tiempo de build
RUN set -eux; \
    case "${TARGETARCH}" in \
      amd64) \
        QT_ARCH_AQT=linux_gcc_64; \
        QT_ARCH_PATH=gcc_64; \
        CMAKE_ASSET="cmake-${CMAKE_VERSION}-linux-x86_64.sh"; \
        ;; \
      arm64) \
        QT_ARCH_AQT=linux_gcc_arm64; \
        QT_ARCH_PATH=gcc_arm64; \
        CMAKE_ASSET="cmake-${CMAKE_VERSION}-linux-aarch64.sh"; \
        ;; \
    esac
```
*Patrón: resolución de arquitectura en imagen en lugar de como ARGs externos, simplificando la CLI de build.*

**2. Ejecución con X11 forwarding (Linux):**
```bash
docker run --rm -it --net=host \
  -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
  fincept/terminal:4.0.2
```
*Patrón: aplicación GUI nativa containerizada con display forwarding, útil para distribución reproducible de apps Qt.*

**3. Estructura de módulos C++ por dominio:**
```
fincept-qt/src/
├── algo_engine/    # Motor algorítmico
├── datahub/        # Ingesta de datos
├── trading/        # Ejecución de órdenes
├── mcp/            # Protocolo de agentes IA
├── auth/           # Autenticación
├── network/        # HTTP/WebSocket
└── python/         # Bridge C++/Python
```
*Patrón: separación por capacidad de negocio, no por capa técnica, dentro de un monorepo C++.*

## Conclusiones y Aprendizajes

1. **Arquitectura híbrida C++/Python**: el patrón de tener un frontend nativo de alto rendimiento (Qt/C++) con scripts Python embebidos para lógica de dominio compleja es directamente adoptable en aplicaciones que necesitan rendimiento UI + flexibilidad de análisis.

2. **Multi-stage Docker para apps GUI**: el Dockerfile demuestra cómo containerizar aplicaciones Qt con X11 forwarding manteniendo builds reproducibles y multi-arco, un patrón valioso para distribución de herramientas de escritorio.

3. **Modularización por dominio**: cada capacidad financiera (trading, datahub, auth, algo_engine) es un módulo independiente con su propio directorio, facilitando contribuciones independientes y testeo aislado.

4. **ADR como práctica de documentación**: el uso de Architecture Decision Records (`docs/adr/`) para documentar el "por qué" de decisiones técnicas es una práctica de madurez de ingeniería directamente adoptable.

5. **CMake Presets para developer experience**: `CMakePresets.json` estandariza configuraciones de build entre desarrolladores, eliminando inconsistencias de entorno, especialmente valioso en proyectos C++ cross-platform.

6. **MCP Protocol para agentes de IA**: la integración nativa del Model Context Protocol (`src/mcp/`) como capa de comunicación con LLMs es un patrón emergente para aplicaciones AI-native que vale la pena estudiar.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code