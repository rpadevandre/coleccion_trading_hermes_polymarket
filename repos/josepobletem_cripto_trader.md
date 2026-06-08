# Crypto Trader Bot

## Información General
- **Repo:** `josepobletem/cripto_trader`
- **URL:** https://github.com/josepobletem/cripto_trader
- **Lenguaje principal:** Python
- **Stars:** 1
- **Última actualización:** 2025-08-19
- **Topics:** ninguno

## Propósito del Repo
`cripto_trader` es un bot de trading automático de criptomonedas diseñado como plataforma educativa y de producción ligera. Combina la API de Binance para operar en mercados crypto, OpenAI (GPT-4) para explicar en lenguaje natural las decisiones de compra/venta, y FastAPI para exponer los endpoints de control. Su principal diferenciador es la integración de IA explicativa junto con una estrategia algorítmica clásica (cruce de EMAs), presentando todo en un stack completo con persistencia, observabilidad (Prometheus) y despliegue en nube mediante Terraform.

Está diseñado para desarrolladores que quieren iniciarse en trading algorítmico, aprender integración de APIs financieras y de IA, y tener una base sólida y auditable que puedan extender hacia un producto real o usarlo como portafolio técnico.

## Arquitectura y Patrones Clave
El proyecto sigue una arquitectura de capas con separación clara de responsabilidades dentro del paquete `trading/`. El flujo principal es: el scheduler dispara la estrategia periódicamente → la estrategia consulta precios a Binance → decide BUY/SELL/HOLD → GPT genera una explicación → la operación se persiste en SQLite. FastAPI actúa como capa de control/observabilidad, exponiendo un webhook para ejecución manual.

Patrones técnicos destacados:
- **Scheduler-driven architecture**: APScheduler ejecuta la lógica de trading en intervalos configurables sin intervención manual.
- **Strategy Pattern**: La lógica de decisión está aislada en `strategy.py`, separada del cliente HTTP y la persistencia.
- **Repository Pattern ligero**: `db.py` encapsula todas las operaciones SQLAlchemy.
- **Decorator/Middleware de observabilidad**: Prometheus-client expone métricas en tiempo real.
- **IaC con Terraform**: Infraestructura reproducible para GCP (Cloud Run) y AWS (ECS/EC2).
- **CI/CD**: GitHub Actions en `.github/workflows/ci.yml` para lint, tests y validación automática.

## Componentes Principales

- **`main.py`** — Punto de entrada FastAPI; define rutas (incluyendo `/webhook` para ejecución manual) y arranca el scheduler al iniciar.
- **`trading/binance_client.py`** — Wrapper sobre `python-binance`; obtiene precios OHLCV y ejecuta órdenes en el exchange.
- **`trading/strategy.py`** — Implementa la estrategia de cruce de EMAs (EMA corta vs EMA larga) para generar señales BUY/SELL/HOLD.
- **`trading/gpt_helper.py`** — Llama a la API de OpenAI para generar una explicación en lenguaje natural de cada decisión de trading.
- **`trading/scheduler.py`** — Configura y lanza APScheduler para ejecutar el ciclo de trading automáticamente.
- **`trading/db.py`** — Capa de persistencia con SQLAlchemy; guarda cada operación en SQLite (`trades.db`).
- **`trading/schemas.py`** — Modelos Pydantic para validación de datos de entrada/salida en FastAPI.
- **`trading/logger.py`** — Configuración centralizada de logging hacia `trading.log`.
- **`infra/gcp/` y `infra/aws/`** — Archivos Terraform para despliegue en GCP Cloud Run y AWS respectivamente.
- **`tests/`** — Suite de tests unitarios con pytest para cada módulo + tests de infraestructura simulada.

## Dependencias Clave

| Librería | Uso concreto |
|---|---|
| `fastapi` + `uvicorn` | Framework web para exponer API REST y webhook de control |
| `python-binance` | Cliente oficial Binance para obtener datos de mercado y ejecutar órdenes |
| `openai` | Llamadas a GPT-4 para explicar decisiones de trading en lenguaje natural |
| `apscheduler` | Ejecución periódica automática del ciclo de trading |
| `sqlalchemy` | ORM para persistir operaciones en SQLite |
| `prometheus-client` | Exposición de métricas de rendimiento en tiempo real |
| `python-dotenv` | Gestión de variables de entorno (API keys) desde `.env` |
| `pytest` | Testing unitario e integración de todos los módulos |
| `black` + `isort` + `flake8` | Calidad y estilo de código |

## Fragmentos de Código Relevantes

**1. Webhook para ejecución manual del ciclo de trading:**
```bash
curl -X POST http://localhost:8000/webhook
```
Permite disparar manualmente el ciclo sin esperar al scheduler, útil para debugging o pruebas en producción.

**2. Comandos del Makefile — flujo completo de desarrollo:**
```bash
make install        # Instala dependencias en venv
make run            # Inicia FastAPI en localhost:8000
make test           # Corre tests unitarios con pytest -v
make docker-up      # Levanta todo con Docker Compose
make deploy-gcp     # terraform init + apply en infra/gcp/
make lint           # flake8 sobre trading/ y tests/
```

**3. Docker Compose con volúmenes para persistencia:**
```yaml
services:
  trader:
    build: .
    env_file: .env
    volumes:
      - ./trading.log:/app/trading.log
      - ./trades.db:/app/trades.db
    ports:
      - "8000:8000"
    restart: unless-stopped
```
Los volúmenes garantizan que los logs y la base de datos SQLite sobrevivan reinicios del contenedor.

## Conclusiones y Aprendizajes

- **Separación de estrategia y ejecución**: Aislar `strategy.py` del cliente Binance permite testear la lógica de decisión con datos mock sin necesidad de llamadas reales al exchange — patrón directamente adoptable en cualquier sistema de reglas de negocio.
- **IA como capa explicativa, no decisora**: Usar GPT-4 para explicar (no para decidir) mantiene el sistema determinista y auditable, mientras agrega valor UX. Este patrón es reutilizable en cualquier sistema donde se requiera transparencia algorítmica.
- **Scheduler + FastAPI**: La combinación de APScheduler iniciado al arrancar FastAPI es un patrón limpio para sistemas que necesitan tanto automatización periódica como control por API.
- **Volúmenes Docker para estado local**: Montar `trades.db` y `trading.log` como volúmenes es la forma correcta de manejar estado persistente en contenedores sin infraestructura de BD externa.
- **IaC desde el inicio**: Incluir Terraform en el repo desde el primer commit normaliza el despliegue reproducible y elimina la dependencia de configuración manual en cloud.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code