# Using the New Hermes Agent to Track Polymarket "Smart Money"

## Información General
- **Canal:** The Prediction Engineer
- **Duración:** 6m 34s
- **Idioma detectado:** English
- **Transcripción fuente:** `Using_the_New_Hermes_Agent_to_Track_Polymarket_Smart_Money.txt`

## Resumen Ejecutivo
El video presenta Hermes Agent, un agente de IA con ~21,000 estrellas en GitHub, utilizado para automatizar el seguimiento de traders rentables en Polymarket. El autor lo configura para analizar el leaderboard de Polymarket, extraer las estrategias de los wallets más rentables y enviar actualizaciones periódicas (cada 7 minutos) vía terminal, sin necesidad de revisar manualmente los trades.

Se compara Hermes Agent con su competidor principal Open Claw (presumiblemente Claude/Anthropic's Computer Use), destacando tres ventajas clave: mayor transparencia en la ejecución de pasos, mejor memoria persistente y mejora autónoma de habilidades, y mayor facilidad de instalación (5-10 minutos desde cero). El autor usa el modelo Sonnet de Anthropic como backend tras encontrar rate limiting con Opus (error 529).

El caso de uso concreto mostrado es un sistema de análisis de wallets de Polymarket que extrae la estrategia de trading de cada trader rentable, como el ejemplo de un trader que usa el precio overnight del SPX para decidir entradas y salidas, con ganancias de ~$25K totales y ~$15K en el último mes.

## Puntos Clave
- **Hermes Agent** es un agente de IA open source con 21K+ GitHub stars, de rápida adopción
- Se instala con un único script (one-click command) desde el sitio de News Research en 5-10 minutos
- Funciona en terminal, aceptando instrucciones en lenguaje natural
- Muestra cada paso que ejecuta en tiempo real (browser snapshot, navegación, etc.), a diferencia de Open Claw
- Tiene **memoria auto-mejorante**: aprende tareas nuevas y las convierte en "skills" reutilizables sin necesidad de re-enseñarlas
- Se configuró un **cron job** que corre cada 7 minutos para extraer wallets y estrategias del leaderboard de Polymarket
- El modelo recomendado es **Claude Sonnet** (no Opus) para evitar errores 529 por rate limiting
- El autor identifica una estrategia de trader rentable basada en el precio overnight del SPX para timing de entradas/salidas
- Plan de uso: backtesting y paper trading de las estrategias identificadas antes de producción

## Conceptos Técnicos Mencionados
- **Hermes Agent** — Agente de IA open source (GitHub, ~21K stars) para automatización de tareas mediante lenguaje natural
- **Open Claw** — Competidor de Hermes Agent (posiblemente referencia a Claude Computer Use de Anthropic); usado como baseline de comparación
- **Polymarket** — Plataforma de prediction markets con leaderboard público de traders y transparencia de wallets
- **Claude Sonnet / Opus** — Modelos de lenguaje de Anthropic usados como backend del agente; Sonnet recomendado por menor rate limiting
- **Cron Job** — Tarea programada configurada dentro del agente para ejecutarse cada 7 minutos automáticamente
- **Browser Snapshot / Browser Navigate** — Herramientas internas del agente para interactuar con sitios web (web scraping / browser automation)
- **Memory / Skills System** — Mecanismo de Hermes Agent para persistir y mejorar habilidades aprendidas entre sesiones
- **Wallet Analysis** — Técnica de extracción de estrategias de trading a partir de direcciones de wallet en blockchain
- **SPX Overnight Pricing** — Estrategia de trading basada en el precio del S&P 500 fuera de horario de mercado como señal de entrada/salida
- **Copy Trading / Whale Tracking** — Caso de uso mencionado: replicar automáticamente las operaciones de wallets rentables
- **Hyperliquid / Kelshi** — Otras plataformas de trading mencionadas como contexto del autor

## Fragmentos Relevantes

> *"The absolute best part about Polymarket is the transparency. You can see what every trader is doing, including every profitable trader's strategies."*

> *"Hermes agent actually tells you exactly what it's doing. So you can see here browser snapshot, browser navigate to this thing. It's very nice because Open Claw, if it gets stuck somewhere, you don't really know where it gets stuck."*

> *"Hermes agent is much better at that. So it will actually, if you tell it to give it a prompt and a skill, it will actually build it into another skill and update skills over time on its own."*

> *"All I did was I copied it in... I got started in literally like 5 minutes. Super fast. And all you do is you run this install script and then you choose your model and then you just start talking to it."*

> *"I had to use Sonnet within Anthropic because I tried using Opus and it kept running into 529 errors... if you're running into problems with using Opus directly on it, try Sonnet."*

> *"Send me the update every 15 minutes... I set up a task which it runs every now 7 minutes and it sends me those new addresses every 7 minutes with that write-up."*

> *"They already know how to do these tasks. You don't have to teach them again."*

## Conclusiones y Aprendizajes
- **Agentes con transparencia de ejecución son más debuggeables**: Al construir pipelines de agentes, exponer los pasos intermedios (logs de acciones) facilita identificar fallos y comportamientos no deseados.
- **Memoria persistente como feature de producción**: Para tareas repetitivas o pipelines de trading, un agente que convierte instrucciones en skills reutilizables reduce la necesidad de re-prompting y mejora la fiabilidad.
- **Instalación y onboarding importan**: Hermes Agent demuestra que un buen script de instalación one-click puede ser un diferenciador real frente a alternativas más complejas.
- **Patrón de uso concreto aplicable**: Configurar un cron job dentro del agente para scraping periódico de datos públicos (leaderboards, wallets) + análisis + notificación es un pipeline replicable para cualquier fuente de datos pública con transparencia on-chain.
- **Gestión de rate limits**: Seleccionar el tier correcto del modelo (Sonnet vs Opus) según la carga de trabajo es crítico para evitar interrupciones en producción.
- **Flujo de investigación de estrategias**: Usar agentes para identificar → analizar → backtest → paper trade → producción es un framework aplicable a cualquier sistema de trading algorítmico.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code