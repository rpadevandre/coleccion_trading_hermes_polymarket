# ¡Se LIBERÓ! Crea un TRADING BOT para POLYMARKET con HERMES Agent e IA Gratis 🪽

## Información General
- **Canal:** Appsclavitud w VeraBadías
- **Duración:** 19m 30s
- **Idioma detectado:** Español
- **Transcripción fuente:** `Se_LIBERÓ_Crea_un_TRADING_BOT_para_POLYMARKET_con_HERMES_Age.txt`

## Resumen Ejecutivo
El video muestra cómo integrar **Hermes Agent** (plataforma agéntica de IA de código abierto) con **Polymarket** (mercado de predicciones descentralizado) para construir un bot de trading inteligente sin necesidad de escribir código manualmente. El flujo consiste en usar Hermes como agente de investigación autónomo que escanea mercados públicos de Polymarket, analiza posiciones con un LLM (OpenAI GPT), filtra oportunidades de bajo riesgo y entrega señales al usuario para que sea él quien tome la decisión final de inversión.

El autor enfatiza que la arquitectura es deliberadamente semi-autónoma: el agente **no abre posiciones por sí solo**, sino que actúa como capa de inteligencia y filtrado para reducir incertidumbre. Para desplegar el sistema de forma segura y disponible 24/7, recomienda un VPS de Hostinger con Hermes corriendo en Docker, reforzado con Tailscale para acceso seguro. La entrega de señales se automatiza mediante un **cron job** que envía resultados vía Telegram cada 6 horas, eliminando la necesidad de estar frente al ordenador.

El video también menciona posibles mejoras como añadir un **knowledge graph** para contextualizar mercados históricos, la posibilidad de un segundo agente que ejecute las operaciones automáticamente, y la integración con otros modelos más potentes como GPT-4o, GPT-4 mini o GPT-5.5 según el balance entre coste y calidad de análisis.

## Puntos Clave
- **Hermes Agent** es presentado como el estándar actual en agentes autónomos de IA (171k+ estrellas en GitHub, crecimiento constante de commits).
- **Polymarket** es un mercado de predicciones donde se pueden abrir posiciones sobre deportes, política, geopolítica y otros eventos.
- El bot actúa como **agente de investigación**, no de ejecución: el usuario mantiene control sobre la decisión final de inversión.
- El flujo del agente: datos públicos → escaneo de mercado → análisis LLM → filtrado por riesgo → señal para el usuario.
- Se filtra por: liquidez baja, fuentes poco confiables, mercados ambiguos o con datos incompletos.
- Se recomienda **VPS de Hostinger** (plan KVM2) en lugar de máquina local para evitar riesgos de seguridad con credenciales y cuentas bancarias.
- **Docker** es el entorno de contenedores donde corre Hermes dentro del VPS.
- **Tailscale** añade una capa adicional de seguridad para acceso remoto al VPS.
- Un **cron job** automatiza la ejecución cada 6 horas y envía resultados al usuario por **Telegram**.
- El coste de un análisis completo con GPT-4 mini fue aproximadamente **1 centavo USD**, lo que permite análisis frecuentes a bajo coste.
- El modelo recomendado para balance coste/calidad es **GPT-4o mini**; para máxima calidad, **GPT-5.5**.
- Se menciona la posibilidad de un **segundo agente** que ejecute las operaciones automáticamente (como continuación del proyecto).
- Mejora sugerida: integrar un **knowledge graph** con historial de mercados ganadores.

## Conceptos Técnicos Mencionados
- **Hermes Agent** — Plataforma de agentes autónomos de IA de código abierto, considerada el estándar actual para automatización con LLMs.
- **Polymarket** — Mercado de predicciones descentralizado donde se puede hacer trading sobre eventos reales (deportes, política, etc.).
- **LLM (Large Language Model)** — Modelo de lenguaje grande usado para analizar y razonar sobre posiciones de mercado.
- **OpenAI API / platform.openai.com** — Plataforma de generación y gestión de claves API para integrar modelos GPT con aplicaciones externas.
- **GPT-4o mini / GPT-5.5** — Modelos de OpenAI utilizados como motor de razonamiento del agente de trading.
- **VPS (Virtual Private Server)** — Servidor privado virtual usado para correr Hermes 24/7 de forma segura y aislada.
- **Hostinger KVM2** — Plan de VPS recomendado por el autor por su relación coste/rendimiento.
- **Docker** — Sistema de contenedores donde se despliega y aísla la instancia de Hermes.
- **Tailscale** — Red privada virtual (VPN mesh) usada para acceder de forma segura al VPS sin exponer puertos públicos.
- **SSH** — Protocolo de acceso remoto a la terminal del VPS.
- **Cron Job** — Tarea programada en Linux para ejecutar el bot de análisis automáticamente cada N horas.
- **Telegram Bot** — Canal de entrega de señales y resultados del agente directamente al teléfono del usuario.
- **Knowledge Graph** — Estructura de conocimiento contextual propuesta como mejora para mejorar la selección de mercados.
- **Scaffolding (agente)** — Generación automática de la estructura inicial del proyecto por parte del agente al recibir el prompt de configuración.
- **Prompt Engineering** — Técnica de diseño de instrucciones para guiar el comportamiento del agente LLM.

## Fragmentos Relevantes
> "Básicamente es un agente de inteligencia e investigación para decidir cuál posición abrir en Polymarket. Toda la inteligencia y toda la investigación la va a hacer esta gente, pero tú vas a decidir cuál de las sugerencias... vas a abrir."

> "Lo que esto quiere al final de cuentas resolver es el principio de incertidumbre. Es decir, si obviamente no sabemos nada de Bitcoin, ¿cómo podríamos decidir esto? Bueno, es esta precisamente la capa de conocimiento que tenemos que construir con nuestro agente."

> "Esto es para reducir el riesgo, para dejar pasar lo que es seguro y bloquear lo que es ambiguo con baja liquidez o que tiene datos incompletos o la fuente de publicación no es clave."

> "El precio aproximadamente un centavo. Puede ir muchísimo más abajo. Esto significa que podemos correr tantos análisis como nosotros querramos."

> "Como esto está corriendo en el VPS de Hostinger, no solamente no necesito que mi computadora esté prendida, simplemente tampoco necesito estar en frente de mi computadora."

> "Entre mejor el modelo, mejores resultados por obvias razones. Si el modelo es inteligente, va a bloquear mercados impredecibles, sin fuente clara de baja liquidez y te va a filtrar los que son mucho más seguros."

> "Hermes es un software muy abrasivo que al final de cuentas tiene un rango muy amplio de permisos... esto no es recomendable para principiantes [en máquina local]."

## Conclusiones y Aprendizajes
- **Patrón de agente semi-autónomo**: separar la capa de análisis/investigación (automatizada) de la capa de ejecución (humana) es una arquitectura de bajo riesgo aplicable a cualquier dominio que requiera toma de decisiones con datos externos.
- **Deployment en VPS con Docker**: correr agentes LLM en contenedores aislados en un VPS es la práctica recomendada para proyectos que manejan credenciales sensibles o necesitan disponibilidad 24/7.
- **Cron job + Telegram como pipeline de entrega**: la combinación cron → script de análisis → Telegram bot es un patrón reutilizable para cualquier sistema de alertas o señales automatizadas.
- **Gestión de API keys**: nunca integrar claves directamente en el chat del agente; usar variables de entorno o gestores de secretos. El video menciona esto como punto de atención de seguridad.
- **Selección de modelo por tarea**: para tareas de análisis/filtrado con alto volumen de llamadas, GPT-4o mini ofrece un equilibrio óptimo; reservar modelos más potentes (GPT-5.5) para casos donde la calidad del razonamiento es crítica.
- **Tailscale como capa de seguridad**: alternativa a exponer SSH público, ideal para proyectos con acceso remoto frecuente a servidores personales.
- **Knowledge graph como memoria del agente**: añadir contexto histórico estructurado mejora significativamente la calidad de decisiones en agentes que operan sobre dominios repetitivos (mercados, tendencias, etc.).

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code