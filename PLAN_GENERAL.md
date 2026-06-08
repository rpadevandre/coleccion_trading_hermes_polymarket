# Plan general: Agente de investigación de Polymarket con Hermes

> **Nota para el agente que ejecute este plan (Hermes Agent / Claude Code):**
> Este documento es una especificación accionable. Está escrito para que la
> sigas paso a paso, fase por fase, marcando cada criterio de éxito antes de
> avanzar a la siguiente fase. Todas las rutas de archivo son relativas a la
> raíz del proyecto `subtitulos_youtube`. Cuando el plan dice "lee `repos/X.md`"
> o "lee `videos/Y.md`", esos archivos están dentro de esta misma carpeta
> (`outputs/coleccion_trading_hermes_polymarket/`) — ábrelos para extraer
> patrones concretos antes de escribir código. No inventes detalles de API o
> arquitectura: si no está en estas fuentes ni en `sintesis/`, dilo
> explícitamente y decide con criterio conservador (ver "Principios no
> negociables" más abajo).

---

## 0. Objetivo del proyecto

**El objetivo final de este proyecto es generar ingresos reales operando en
mercados de predicción de Polymarket.** No es un ejercicio académico ni un
sistema que se queda para siempre en modo "solo investigación" — la
investigación y el modo de pruebas son **etapas necesarias del camino hacia
dinero real**, no el destino.

El plan avanza en tres etapas secuenciales, cada una con su propia validación
antes de pasar a la siguiente:

1. **Etapa A — Investigación y señales** (Fases 1-5 de este plan): el sistema
   escanea mercados, rastrea wallets "smart money", analiza oportunidades con
   IA y genera señales puntuadas con una rúbrica explícita. Aún no hay dinero
   en juego — el objetivo de esta etapa es demostrar que el sistema puede
   *encontrar* oportunidades razonables de forma consistente.
2. **Etapa B — Test con dinero ficticio (paper trading)** (Fase 6): las
   señales generadas en la Etapa A se registran como si se hubiera operado
   con ellas (capital simulado, P&L simulado), para medir el rendimiento real
   del sistema *antes* de arriesgar dinero. Esta etapa es la que decide si
   el sistema está listo para pasar a la siguiente.
3. **Etapa C — Operación con dinero real** (Fase 7): solo se llega aquí si
   la Etapa B demuestra resultados positivos sostenidos. Aquí es donde el
   sistema empieza a generar ingresos de verdad — con capital real, límites
   de riesgo explícitos, y siempre con un gate de aprobación humana en cada
   operación (al menos hasta que el historial de la Etapa B + C temprana
   justifique relajar ese gate, y eso lo decide el usuario, no el agente).

Este orden no es burocracia: es la única secuencia que protege el capital del
usuario mientras se construye evidencia real de que el sistema funciona. Saltarse
la Etapa B para ir directo a operar con dinero real es exactamente el
anti-patrón que las fuentes de esta colección señalan como la causa más común
de pérdidas (ver `sintesis/...md`, riesgo #1, y el comentario explícito en
`videos/Se_LIBERÓ_Crea_un_TRADING_BOT_para_POLYMARKET_con_HERMES_Age.md`:
*"el agente no abre posiciones por sí solo"* — esa frase describe el punto de
partida de la Etapa C, no una limitación permanente del proyecto).

---

## 1. Principios no negociables

Estos principios vienen directamente de los riesgos identificados en
`sintesis/20260608_agente_de_tradingpredicción_con_Hermes_y_Polymarke.md`
(sección "Riesgos y anti-patrones") y de patrones repetidos en 3+ fuentes de
la colección. Existen precisamente para que el proyecto **pueda llegar** a
generar ingresos reales sin que un error de diseño temprano queme el capital
o la cuenta antes de tiempo. **No se pueden saltar para "ir más rápido"**:

1. **Ninguna transacción con dinero real sin aprobación humana explícita por
   operación**, al menos durante las Etapas A, B y el arranque de la Etapa C.
   El sistema genera y razona señales; una persona aprueba o rechaza cada
   operación real por Telegram. Esto no es una restricción "para siempre" —
   es el punto de partida seguro desde el que se construye el historial que,
   eventualmente, podría justificar más autonomía (decisión que toma el
   usuario explícitamente, nunca el agente por su cuenta). (Fuente:
   `videos/Se_LIBERÓ_Crea_un_TRADING_BOT_para_POLYMARKET_con_HERMES_Age.md`,
   `sintesis/...md` riesgo #1)
2. **Modelos de razonamiento serios para análisis, modelos baratos solo para
   tareas mecánicas** (scraping, formateo). Un agente orquestador con un
   modelo débil degrada la calidad de las decisiones. (Fuente: `sintesis` riesgo #2)
3. **Toda persistencia en SQLite con WAL mode**, en un directorio persistente
   del VPS — nunca en un workspace temporal que pueda borrarse. (Fuente:
   `sintesis` riesgos #5 y #8)
4. **Rate limiting respetuoso con la API de Polymarket**: backoff exponencial,
   cooldowns ante 429/402. Un baneo de IP mata el proyecto completo. (Fuente:
   `sintesis` riesgo #5)
5. **Credenciales solo en `.env` del VPS**, nunca en el repo de GitHub —
   doblemente importante porque ya hubo un incidente de visibilidad de repo
   en este proyecto (corregido, pero sirve de recordatorio).
6. **No usar OAuth de suscripción para nada que toque dinero real.** OAuth
   está bien para análisis; cualquier futura ejecución de trades necesitaría
   API keys pagadas y dedicadas. (Fuente: `sintesis` riesgo #7)

Si en algún punto de la ejecución de este plan una decisión entra en conflicto
con uno de estos principios, **detente y repórtalo al usuario** en lugar de
improvisar una excepción.

---

## 2. Arquitectura objetivo (versión mínima viable)

A diferencia de la arquitectura "completa" descrita en `sintesis/...md`
(que incluye un segundo agente de ejecución, Kanban multi-agente, FastAPI REST
con `/approve`, etc.), **este plan apunta a un MVP más pequeño y entregable
en días, no semanas**, que puede crecer hacia esa arquitectura completa si
demuestra valor:

```
┌──────────────────────────────────────────────────────────┐
│                 HERMES AGENT (VPS, ya activo)              │
│                                                            │
│   CRON (cada 6h)                                          │
│        │                                                  │
│        ▼                                                  │
│   skill: polymarket-research  ──▶  polymarket_client.py   │
│        │                              (CLOB + Gamma API)  │
│        ▼                                                  │
│   scoring (bettor_scorer.py, umbral 65/100)               │
│        │                                                  │
│        ▼                                                  │
│   hermes_polymarket.db (SQLite, WAL)                      │
│   tablas: markets · signals · wallet_profiles             │
│        │                                                  │
│        ▼                                                  │
│   Telegram: resumen de señales pendientes de revisión     │
│   (el usuario decide — el sistema NO ejecuta nada)        │
└──────────────────────────────────────────────────────────┘
```

**Por qué este MVP y no el completo de una vez:**
- Permite validar si las señales generadas son útiles *antes* de invertir
  tiempo en un segundo agente de ejecución, Kanban, FastAPI, dashboards, etc.
- Reduce la superficie de fallo: una sola skill, una sola DB, un solo cron.
- Es coherente con el patrón "investigar → validar → escalar" que se repite
  en las fuentes (p. ej. `videos/Using_the_New_Hermes_Agent_to_Track_Polymarket_Smart_Money.md`
  empieza con tracking simple antes de construir nada más complejo).

Si el MVP demuestra valor durante 2-3 semanas de uso real, entonces sí migrar
hacia la arquitectura dual (análisis + ejecución) descrita en `sintesis/...md`
sección "Arquitectura recomendada".

---

## 3. Mapa de la colección — qué leer para cada parte

Antes de escribir cualquier código, lee estas fuentes **en este orden**. Cada
una aporta un patrón concreto y reusable:

| Para construir... | Lee primero | Qué extraer |
|---|---|---|
| El cliente de la API de Polymarket | [`repos/DevvGwardo_polymarket-dashboard-skill.md`](repos/DevvGwardo_polymarket-dashboard-skill.md) | Estructura exacta de `polymarket.py` + `polymarket_client.py`, lista de endpoints CLOB/Gamma documentados en su `references/api-endpoints.md` |
| El formato de skill para Hermes | [`repos/DevvGwardo_polymarket-dashboard-skill.md`](repos/DevvGwardo_polymarket-dashboard-skill.md) | Cómo registró su `SKILL.md`; combínalo con el formato real ya verificado en `~/.hermes/skills/youtube-research-bot/` (categoría + `SKILL.md` con frontmatter YAML) |
| El scoring multi-criterio | [`repos/DevvGwardo_polymarket-dashboard-skill.md`](repos/DevvGwardo_polymarket-dashboard-skill.md), [`videos/I_Built_an_AI_Agent_to_Find_Hidden_Polymarket_Alpha_Claude_C.md`](videos/I_Built_an_AI_Agent_to_Find_Hidden_Polymarket_Alpha_Claude_C.md) | Dimensiones del Opportunity Score (Risk/Reward, Conviction, Volume, EV, Source reliability) y el umbral de 65/100 |
| El tracking de smart money | [`videos/Using_the_New_Hermes_Agent_to_Track_Polymarket_Smart_Money.md`](videos/Using_the_New_Hermes_Agent_to_Track_Polymarket_Smart_Money.md) | Frecuencia del cron (cada 7 min para leaderboard), cómo extraer estrategia de una wallet con LLM, manejo del error 529 por rate limiting |
| El blueprint completo del bot semi-autónomo | [`videos/Se_LIBERÓ_Crea_un_TRADING_BOT_para_POLYMARKET_con_HERMES_Age.md`](videos/Se_LIBERÓ_Crea_un_TRADING_BOT_para_POLYMARKET_con_HERMES_Age.md) | Flujo completo señal → filtro de riesgo → cron + Telegram, costos reales reportados, y la frase clave: "el agente no abre posiciones por sí solo" |
| Patrones de orquestación si el MVP escala | [`repos/DFZinc_JANUS.md`](repos/DFZinc_JANUS.md), [`videos/I_Built_the_Ultimate_Multi-Agent_Workflow_w_Hermes_Agent_Kan.md`](videos/I_Built_the_Ultimate_Multi-Agent_Workflow_w_Hermes_Agent_Kan.md) | Separación Hermes/Tyche con DBs independientes, patrón Kanban-SQLite como capa de coordinación — **solo si decides crecer más allá del MVP** |
| Frameworks de trading de referencia (para vocabulario y patrones, no para copiar código) | [`repos/coding-kitties_investing-algorithm-framework.md`](repos/coding-kitties_investing-algorithm-framework.md), [`repos/666ghj_MiroFish.md`](repos/666ghj_MiroFish.md), [`repos/Fincept-Corporation_FinceptTerminal.md`](repos/Fincept-Corporation_FinceptTerminal.md) | Cómo proyectos maduros estructuran backtesting, multi-agente para forecasting, y dashboards tipo terminal — útil para ideas de evolución futura del MVP, no para la primera versión |

La especificación técnica detallada (schema SQL completo, prompts del agente,
estructura exacta de carpetas del skill, código de referencia de
`PolymarketClient` y `bettor_scorer`) ya existe en
[`sintesis/20260608_agente_de_tradingpredicción_con_Hermes_y_Polymarke.md`](sintesis/20260608_agente_de_tradingpredicción_con_Hermes_y_Polymarke.md)
secciones "Spec de implementación" Fase 0 a Fase 5. **Este plan no la repite —
la reordena en una secuencia ejecutable de MVP y le añade los criterios de
éxito que esa síntesis no tenía.**

---

## 4. Fases de ejecución (con criterios de éxito verificables)

> Convención: cada fase termina con un bloque "✅ Criterio de éxito" — no
> avances a la siguiente fase hasta poder marcarlo como cumplido. Si algo no
> se puede verificar (p. ej. necesita una cuenta o credencial que no existe
> todavía), repórtalo al usuario explícitamente en lugar de asumir que está bien.

### Fase 1 — Cliente de Polymarket como módulo independiente

**Qué hacer:**
- Crear `polymarket_client.py` (async, con `aiohttp`) que cubra como mínimo:
  `get_trending`, `get_market(condition_id)`, `get_orderbook(condition_id)`,
  `get_leaderboard`, `get_wallet_history(address)`.
- Usar los endpoints documentados en `repos/DevvGwardo_polymarket-dashboard-skill.md`
  (CLOB `https://clob.polymarket.com`, Gamma `https://gamma-api.polymarket.com`).
- Implementar backoff exponencial y manejo explícito de 429/402/529 desde el
  primer commit (no como mejora posterior — es uno de los riesgos #5 marcados
  en la síntesis).
- Probarlo de forma aislada con un script CLI simple (`polymarket.py search "..."`,
  `polymarket.py trending`) **antes** de integrarlo con Hermes.

**✅ Criterio de éxito:** ejecutar `polymarket.py trending --limit 5` desde
la terminal del VPS devuelve datos reales de mercados sin errores de rate
limit, y el código maneja una respuesta 429 simulada sin crashear.

---

### Fase 2 — Persistencia (SQLite + WAL)

**Qué hacer:**
- Crear `hermes_polymarket.db` en un directorio persistente del proyecto
  (NO en `/tmp` ni en un workspace de agente que pueda limpiarse).
- Implementar el schema de las tablas `markets`, `signals`, `wallet_profiles`
  tal como está especificado en `sintesis/...md` Fase 2.1 (puedes omitir la
  tabla `executions` y `tasks`/Kanban en el MVP — no hay ejecución todavía).
- Activar `PRAGMA journal_mode=WAL`.

**✅ Criterio de éxito:** se puede insertar y leer un registro de prueba en
cada una de las tres tablas desde un script Python independiente, y el
archivo `.db-wal` aparece junto a la base de datos tras la primera escritura.

---

### Fase 3 — Scoring multi-criterio

**Qué hacer:**
- Implementar `bettor_scorer.py` con las 5 dimensiones descritas en
  `sintesis/...md` Fase 1.3 (Risk/Reward, Volume, Conviction, Expected Value,
  Source reliability) sumando 100 puntos, con **umbral explícito en 65/100**
  para generar una señal `BUY`/`WATCH` vs `SKIP`.
- Documentar en el propio código *de dónde* sale cada fórmula de scoring —
  si la inventas porque la fuente no da el detalle exacto, dilo explícitamente
  en un comentario (ej. `# fórmula propia — DevvGwardo.md no detalla los pesos exactos`).

**✅ Criterio de éxito:** dado un `market_data` de ejemplo (puedes usar uno
real obtenido en la Fase 1), el scorer devuelve un diccionario con el desglose
por dimensión, el total, y la recomendación, de forma determinista (mismo
input → mismo output).

---

### Fase 4 — Skill de Hermes: `polymarket-research`

**Qué hacer:**
- Seguir el formato real ya verificado en
  `~/.hermes/skills/youtube-research-bot/` (carpeta categoría +
  subcarpetas con `SKILL.md` y frontmatter YAML), **no** el formato `.py`
  obsoleto de `hermes_skills/*.py` (ver nota de versión en `CLAUDE.md`,
  sección "Integración con Hermes Agent").
- El `SKILL.md` debe declarar claramente en su descripción: *"Esta skill
  genera señales de investigación. NO ejecuta operaciones ni mueve fondos."*
- Comandos a exponer como mínimo: `scan` (trending + scoring), `analyze <id>`
  (análisis profundo de un mercado), `wallet <address>` (extracción de
  estrategia desde historial).

**✅ Criterio de éxito:** `hermes skills list` muestra la skill como
`local | local | enabled`, y pedirle a Hermes en lenguaje natural "escanea
los mercados de Polymarket en tendencia" invoca la skill correctamente.

---

### Fase 5 — Cron de escaneo + entrega por Telegram

**Qué hacer:**
- Crear un script de cron (siguiendo el patrón ya usado en
  `~/.hermes/scripts/monitor_investigacion.sh`) que: escanee mercados
  trending, los puntúe, guarde resultados en `signals`, y envíe un resumen
  por Telegram de las señales que superan el umbral de 65/100.
- Frecuencia recomendada por las fuentes: cada 6 horas para el escaneo
  general (`videos/Se_LIBERÓ_...md`), cada 7 minutos solo si decides añadir
  tracking de leaderboard en tiempo casi real (`videos/Using_the_New_Hermes_Agent_to_Track_Polymarket_Smart_Money.md`)
  — **empieza con cada 6 horas**; ajusta solo si el volumen de señales útiles
  lo justifica.
- El mensaje de Telegram debe incluir el razonamiento de la señal (no solo
  el score), para que el usuario pueda decidir con contexto.

**✅ Criterio de éxito:** el cron corre al menos una vez de forma manual
(`hermes cron run <id>` o equivalente) sin errores, y llega un mensaje a
Telegram con al menos una señal o un "sin oportunidades por encima del umbral
en este ciclo" — nunca un mensaje vacío o un error silencioso.

---

### Fase 6 — Etapa B: paper trading con dinero ficticio (mínimo 2-3 semanas)

**Esta fase es el verdadero examen del sistema — no un "extra" opcional.**
El objetivo aquí ya no es solo "¿genera el sistema señales razonables?" sino
**"¿generaría dinero real si operáramos según estas señales?"**

**Qué hacer:**
- Crear una tabla `paper_positions` (o ampliar `signals`) que registre, por
  cada señal que supere el umbral: el "capital ficticio" que se habría
  arriesgado, el precio de entrada simulado, el resultado del mercado al
  cerrar, y el P&L simulado resultante. Define un capital ficticio total fijo
  desde el inicio (p. ej. "$1000 ficticios") para que las métricas de
  rendimiento sean comparables entre señales.
- Generar un resumen periódico (semanal) por Telegram con métricas agregadas:
  win rate, P&L acumulado simulado, drawdown máximo simulado, número de
  señales operadas vs. descartadas. Esto convierte el "feedback manual" en
  **datos cuantitativos de rendimiento**, que es lo que realmente se necesita
  para decidir si pasar a dinero real.
- Sigue siendo **cero dinero real en juego** — el riesgo de esta etapa es
  solo de tiempo, no de capital. Esto es exactamente lo que recomienda
  `videos/Using_the_New_Hermes_Agent_to_Track_Polymarket_Smart_Money.md`
  ("paper trading antes de producción") y el riesgo #1 de `sintesis/...md`.

**✅ Criterio de éxito (el "go/no-go" hacia dinero real):**
- Al menos 20-30 señales simuladas cerradas con resultado conocido (no solo
  registradas — *resueltas*, es decir, el mercado de predicción ya cerró).
- P&L simulado acumulado positivo de forma sostenida (no solo una racha
  puntual — revisa la curva, no solo el número final).
- Win rate y drawdown simulado dentro de límites que el usuario considere
  aceptables para arriesgar capital real (estos límites los define el
  usuario explícitamente antes de pasar a la Fase 7 — el agente no los
  inventa ni los relaja).

Si los resultados son negativos o mediocres: **no se avanza a la Fase 7.**
Se vuelve a la Fase 3 (scoring) o Fase 1 (fuentes de datos) a ajustar el
sistema, y se repite la Fase 6 con los cambios. Iterar aquí es barato;
iterar con dinero real no lo es.

---

### Fase 7 — Etapa C: arranque de operación con dinero real

**Esta fase es el destino del proyecto — pero solo se entra a ella cuando la
Fase 6 ha demostrado, con datos, que el sistema es rentable de forma
sostenida Y el usuario da luz verde explícita para arriesgar capital real.**
No se inicia por inferencia ni por "ya pasó suficiente tiempo" — requiere
confirmación humana directa, exactamente igual que cada operación individual
la requerirá dentro de esta etapa.

**Qué hacer (siguiendo la arquitectura "completa" ya especificada en
`sintesis/...md`, secciones "Arquitectura recomendada" y Fases 3-5 de su
spec de implementación):**
1. Definir con el usuario un **capital real inicial limitado** (no todo el
   capital disponible — empezar con una fracción pequeña que el usuario
   pueda permitirse perder por completo sin consecuencias graves).
2. Construir el agente de ejecución separado (patrón Hermes/Tyche de
   `repos/DFZinc_JANUS.md`) con su propia base de datos (`tyche.db`) — la
   separación entre análisis y ejecución existe precisamente para que esta
   etapa no contamine ni arriesgue la lógica ya validada de la Etapa A/B.
3. Implementar el `human gate` real: cada señal que supere el umbral genera
   un mensaje de Telegram con botones de aprobar/rechazar, y **ninguna
   transacción se firma sin esa aprobación explícita** (Fuente:
   `videos/I_Built_the_Ultimate_Multi-Agent_Workflow_w_Hermes_Agent_Kan.md`,
   patrón de "único gate vía Telegram antes del Builder").
4. Usar API keys pagadas y dedicadas para el agente de ejecución — nunca
   OAuth de suscripción para nada que mueva fondos reales (riesgo #7 de
   `sintesis/...md`).
5. Si el flujo crece a más de 2 agentes trabajando en paralelo, añadir
   Kanban-SQLite como capa de coordinación
   (`videos/I_Built_the_Ultimate_Multi-Agent_Workflow_w_Hermes_Agent_Kan.md`,
   `videos/Hermes_Kanban_Swarm_es_BRUTAL_Tutorial_Completo.md`).
6. Si el flujo de aprobación por Telegram se vuelve insuficiente para el
   volumen de señales, añadir FastAPI REST (`server.py`) con endpoint
   `/approve` (`repos/DFZinc_JANUS.md`).

**✅ Criterio de éxito inicial de la Etapa C:** la primera operación con
dinero real se ejecuta solo después de aprobación explícita del usuario por
Telegram, queda registrada en `executions` con su resultado real, y el
capital arriesgado nunca excede el límite que el usuario definió en el
punto 1. A partir de ahí, el ciclo de "medir → ajustar → repetir" continúa
indefinidamente — este es el modo de operación permanente del proyecto, no
un punto final.

**Sobre relajar el human gate más adelante:** una vez que exista un
historial real de operaciones aprobadas y su rendimiento, el usuario *podría*
decidir automatizar partes del flujo (p. ej. aprobar automáticamente señales
por debajo de cierto monto). Esa decisión, cuándo y cómo tomarla, es
exclusivamente del usuario — el agente puede sugerirlo basándose en datos,
pero nunca implementarlo por iniciativa propia.

---

## 5. Estructura de archivos sugerida (en el VPS)

```
/home/hermes/subtitulos_youtube/
├── polymarket/
│   ├── polymarket_client.py      # Fase 1
│   ├── polymarket.py             # CLI — Fase 1
│   ├── bettor_scorer.py          # Fase 3
│   ├── db.py                     # Fase 2 (acceso a SQLite/WAL)
│   └── hermes_polymarket.db      # Fase 2 (persistente — NO en workspace temporal)
└── (skill registrada por separado en ~/.hermes/skills/polymarket-research/)
```

Esto mantiene el código del proyecto de investigación de Polymarket separado
del pipeline existente de `subtitulos_youtube` (que sigue dedicado a YouTube
+ GitHub research), evitando mezclar responsabilidades.

---

## 6. Cómo lanzar este plan desde Hermes

Una vez que el usuario decida empezar, el comando natural sería:

```
/goal Construye el sistema descrito en
outputs/coleccion_trading_hermes_polymarket/PLAN_GENERAL.md, cuyo objetivo
final es generar ingresos reales operando en Polymarket — pasando primero
por investigación/señales (Fase 1-5), luego por validación con dinero
ficticio (Fase 6) y finalmente por operación con dinero real (Fase 7).
Empieza por la Fase 1. No avances de fase sin marcar el criterio de éxito
de la fase anterior como cumplido — en particular, NO inicies la Fase 6
sin que el cron de la Fase 5 lleve corriendo de forma estable, y NO inicies
la Fase 7 sin mostrarme los resultados cuantitativos de la Fase 6 y recibir
mi confirmación explícita de que quiero arriesgar capital real.
```

El agente que ejecute esto debe tratar las "✅ Criterio de éxito" de cada
fase como gates obligatorios — exactamente el mismo principio de
human-in-the-loop / verificación-antes-de-avanzar que este plan exige para
el sistema que está construyendo. La diferencia entre "investigación" y
"negocio rentable" no es la ambición del proyecto — es la cantidad de
evidencia acumulada antes de arriesgar capital. Ese es el propósito de las
Fases 6 y 7: convertir ambición en evidencia, y evidencia en ingresos.
