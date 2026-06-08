# Investing Algorithm Framework

## Información General
- **Repo:** `coding-kitties/investing-algorithm-framework`
- **URL:** https://github.com/coding-kitties/investing-algorithm-framework
- **Lenguaje principal:** Python
- **Stars:** 1,247
- **Última actualización:** 2026-06-04
- **Topics:** algorithmic-trading, backtesting, backtesting-trading-strategies, cryptocurrency, python, quantitative, quantitative-analysis, quantitative-finance, quantitative-trading, trade, trading, trading-bot, trading-bots, trading-strategies

## Propósito del Repo
Investing Algorithm Framework es un framework completo para el ciclo de vida cuantitativo de trading: permite diseñar estrategias, hacer backtesting (vectorial y event-driven), comparar resultados en un dashboard unificado y desplegar el algoritmo ganador como bot en producción. Está orientado a quants y desarrolladores Python que quieren evitar reinventar infraestructura (gestión de órdenes, portafolios, datos, scheduling) y centrarse en la lógica de estrategia.

Lo que lo diferencia de alternativas como Backtrader o Zipline es que integra en un único paquete: gestión de portafolio persistente con SQLAlchemy, conectividad live via CCXT (criptomonedas), soporte para múltiples data providers (yfinance, Alpha Vantage, Polygon), storage en cloud (Azure Blob, S3), y un CLI para scaffolding y despliegue.

## Arquitectura y Patrones Clave
El proyecto sigue una **arquitectura en capas** bien definida (Domain → Infrastructure → Services → App) típica de Domain-Driven Design:

- **Domain:** modelos de negocio puros, interfaces de servicios, lógica de backtesting y pipelines — sin dependencias externas.
- **Infrastructure:** implementaciones concretas (SQLAlchemy ORM, repositorios, proveedores de datos externos, ejecutores de órdenes vía CCXT).
- **Services:** orquestación entre domain e infrastructure (order service, trade service, portfolio service, backtest store, métricas).
- **App:** punto de entrada del usuario — algoritmo, reporting, API web Flask, modo stateless.

Se usa **Dependency Injection** (`dependency-injector`) para desacoplar capas y facilitar testing. El **patrón Repository** abstrae el acceso a datos. Los **pipelines** (domain/pipeline) permiten construir estrategias como grafos de pasos. El scheduling se maneja con `schedule`, y la exposición opcional de endpoints usa **Flask + Flask-Migrate**.

El storage de backtests usa **Polars** (DataFrames rápidos), **msgpack + zstandard** para serialización comprimida, y **PyArrow** para interoperabilidad columnar — decisión de rendimiento frente a pandas puro.

## Componentes Principales

- **`investing_algorithm_framework/app/`** — Punto de entrada principal: clase `App`, gestión del algoritmo, reporting y API web
- **`investing_algorithm_framework/app/algorithm/`** — Motor de ejecución del algoritmo: scheduling, ciclo de vida run/stop
- **`investing_algorithm_framework/app/stateless/`** — Modo stateless para backtesting sin base de datos persistente
- **`investing_algorithm_framework/domain/`** — Modelos de negocio puros, interfaces, lógica de backtesting y pipeline
- **`investing_algorithm_framework/domain/models/`** — Entidades: Order, Trade, Position, Portfolio, Symbol, etc.
- **`investing_algorithm_framework/domain/pipeline/`** — Abstracción de pipelines de estrategia (grafos de transformación de datos)
- **`investing_algorithm_framework/domain/backtesting/`** — Motor de backtesting event-driven y vectorial
- **`investing_algorithm_framework/infrastructure/`** — Implementaciones concretas: ORM SQLAlchemy, CCXT, repositorios
- **`investing_algorithm_framework/infrastructure/data_providers/`** — Conectores a yfinance, Alpha Vantage, Polygon
- **`investing_algorithm_framework/infrastructure/order_executors/`** — Ejecución de órdenes real vía CCXT
- **`investing_algorithm_framework/services/`** — Capa de orquestación: order_service, trade_service, portfolio, backtest_store, métricas
- **`investing_algorithm_framework/services/backtest_store/`** — Persistencia y comparación de resultados de backtests
- **`investing_algorithm_framework/services/metrics/`** — Cálculo de métricas cuantitativas (Sharpe, drawdown, etc.)
- **`investing_algorithm_framework/cli/`** — CLI con templates para scaffolding de nuevos proyectos
- **`investing_algorithm_framework/notebook/`** — Integración Jupyter para análisis interactivo
- **`examples/strategies_showcase/`** — 26 estrategias de ejemplo: trend-following, mean-reversion, pairs trading, market making, HFT, opciones, etc.

## Dependencias Clave

| Librería | Uso concreto |
|---|---|
| `ccxt` | Conectividad con exchanges de criptomonedas para órdenes live |
| `SQLAlchemy` | ORM para persistencia de portafolio, órdenes y trades |
| `Flask` + `Flask-Migrate` | API web opcional para inspeccionar el estado del bot |
| `polars` | DataFrames de alta performance para backtesting vectorial |
| `pyarrow` | Serialización columnar e interoperabilidad de datos |
| `msgpack` + `zstandard` | Serialización comprimida rápida para backtest store |
| `dependency-injector` | Inyección de dependencias entre capas |
| `schedule` | Scheduling de estrategias en producción |
| `plotly` | Visualización de resultados de backtests |
| `azure-storage-blob` / `boto3` | Storage remoto de backtests en Azure Blob / AWS S3 |
| `yfinance` / `alpha_vantage` / `polygon-api-client` | Data providers alternativos (opcionales) |
| `tqdm` / `tabulate` | UI de progreso y tablas en CLI |
| `marshmallow` | Serialización/deserialización de modelos para la API |

## Fragmentos de Código Relevantes

**1. Definición mínima de estrategia y app:**
```python
from investing_algorithm_framework import App, Algorithm, Strategy, TradingDataSource

app = App()

class MyStrategy(Strategy):
    time_unit = TimeUnit.DAY
    interval = 1
    
    def apply_strategy(self, algorithm, market_data):
        # Lógica de señal
        if signal_buy:
            algorithm.create_limit_order(
                target_symbol="BTC/USDT",
                order_side=OrderSide.BUY,
                amount=0.01,
                price=market_data["BTC/USDT"]["close"][-1]
            )

app.add_algorithm(Algorithm(strategy=MyStrategy()))
app.run()
```

**2. Backtesting con comparación de múltiples estrategias:**
```python
from investing_algorithm_framework import BacktestService

backtest_service = BacktestService()
results = backtest_service.run([strategy_a, strategy_b, strategy_c])
backtest_service.compare(results)  # Dashboard unificado con métricas
```

**3. Pipeline cross-sectional (selección de activos en corte transversal):**
```python
# Ejemplo del showcase 03_cross_sectional_momentum
class CrossSectionalPipeline(Pipeline):
    def run(self, data):
        # Rankear activos por momentum a 12 meses
        ranked = data.sort("momentum_12m", descending=True)
        return ranked.head(10)  # Top 10 para long
```

## Conclusiones y Aprendizajes

1. **Arquitectura en capas DDD para sistemas de trading:** Separar Domain (modelos puros) → Infrastructure (implementaciones) → Services (orquestación) → App (entrypoint) es directamente adoptable para cualquier sistema financiero o de dominio complejo donde el testing y el reemplazo de dependencias sean críticos.

2. **Dependency Injection como ciudadano de primera clase:** Usar `dependency-injector` explícitamente (en lugar de singletons globales) facilita el modo stateless para backtesting — el mismo código de estrategia corre en live y en backtest cambiando sólo el contenedor de DI.

3. **Stack de datos: Polars + msgpack + zstandard + PyArrow:** Para backtesting a escala, reemplazar pandas por Polars y usar serialización comprimida en lugar de CSV/JSON es un patrón de rendimiento concreto y adoptable.

4. **Backtest Store desacoplado del motor:** Separar el almacenamiento y comparación de resultados de backtest en un servicio propio (con soporte cloud S3/Azure) permite construir pipelines CI/CD de estrategias donde cada commit ejecuta backtests y compara contra la baseline.

5. **CLI con scaffolding de templates:** Incluir un CLI (`investing-algorithm-framework`) con templates para nuevos proyectos es un patrón de DX adoptable en frameworks propios — reduce la fricción de onboarding.

6. **26 estrategias de ejemplo como documentación ejecutable:** Tener una carpeta `examples/strategies_showcase/` con implementaciones reales (desde DCA hasta HFT y opciones) es más valioso que documentación textual para un framework técnico.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code