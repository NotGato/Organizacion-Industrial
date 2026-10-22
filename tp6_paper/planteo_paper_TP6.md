# Planteo del paper — Trabajo Práctico N.º 6 (Grupo 6)

**Organización Industrial (1.4.068) — UADE, FCE — 2.º cuatrimestre 2026 — Docente: Fernando Sotero**

> Este documento es la **hoja de ruta** del paper: propone título, pregunta, hipótesis y objetivos; resuelve el modelo cuantitativo de la consigna; ubica cada resultado en las unidades vistas en clase y arma la estructura que piden los *Lineamientos para escribir un paper* y la *Rúbrica*. Es un borrador para que el grupo lo discuta, lo reescriba con sus palabras y lo complete; no es el texto final (la cátedra controla el plagio y la autoría del grupo).

---

## 0. Ficha del trabajo

| Ítem | Propuesta |
|---|---|
| **Título tentativo** | *“¿Por qué gana quien llega primero? Efectos de red, masa crítica y trampas de coordinación en las billeteras virtuales argentinas”* |
| **Tema (consigna)** | Efectos de red, masa crítica y trampas de coordinación en billeteras virtuales y FinTech (Mercado Pago vs. MODO) |
| **Unidad núcleo** | U9 — Economías de red (Pepall, Richards & Norman, 2006, cap. 22; Katz & Shapiro, 1985; Economides, 1996; Rochet & Tirole, 2003, 2006) |
| **Tipo de paper** | Nivel básico (*Lineamientos*): sistematización elaborada de la literatura más un modelo teórico calibrado, aplicados al caso argentino |
| **Formato** | Times New Roman 12, interlineado 1,5; márgenes de 3 cm a izquierda y derecha y de 2,5 cm arriba y abajo; citas y bibliografía en APA (mínimo 10 referencias) |

---

## 1. Problema, pregunta, hipótesis y objetivos

### 1.1 Situación problemática
Las billeteras virtuales son **plataformas de dos lados** (usuarios ↔ comercios). Para cada usuario, el valor de la billetera crece con la cantidad de comercios que la aceptan (y con la cantidad de contactos a los que puede transferir), y para cada comercio crece con la cantidad de usuarios. Por eso la adopción **no es lineal**: hay umbrales, equilibrios múltiples y un fuerte componente de **expectativas**. En la Argentina conviven un incumbente que llegó primero y está integrado a un *marketplace* (Mercado Pago, dentro del ecosistema de Mercado Libre) y una respuesta coordinada de los bancos (MODO, lanzada en 2020 por un consorcio de entidades bancarias). En el medio, el BCRA impulsó la interoperabilidad (Transferencias 3.0 y el QR interoperable)[^verif].

[^verif]: Verificar fechas y número de Comunicación “A” del BCRA en la fuente oficial antes de citarlas (Transferencias 3.0 se lanzó entre fines de 2020 y 2021, y la obligatoriedad del QR interoperable rige desde fines de 2021).

### 1.2 Pregunta de investigación
> **¿Por qué, en un mercado de pagos digitales con efectos de red, la adopción puede quedar atrapada en un equilibrio bajo (o en el estándar del incumbente) aunque exista un equilibrio de mayor bienestar, y qué políticas (interoperabilidad, subsidios iniciales) permiten desplazar el mercado hacia el equilibrio de alta adopción?**

### 1.3 Hipótesis
- **H1 (coordinación):** con efectos de red y expectativas autocumplidas existen equilibrios múltiples; la no adopción es estable, así que el resultado depende de las expectativas iniciales y no solo de los fundamentales (precio y calidad).
- **H2 (masa crítica):** existe un umbral de adopción (la masa crítica) por encima del cual la red crece sola; ese umbral es **creciente en el costo de adopción P** y **decreciente en la intensidad de red α**.
- **H3 (política):** la interoperabilidad (que eleva la α efectiva y comparte la base instalada) y los subsidios transitorios focalizados (que bajan la P efectiva) reducen la masa crítica y el *lock-in*, con un costo fiscal o privado pequeño frente a la ganancia de bienestar.

### 1.4 Objetivos
**General:** explicar, con el modelo de demanda de red de Katz y Shapiro (1985) y Pepall et al. (2006), la dinámica de adopción de las billeteras virtuales y evaluar las políticas para salir de la trampa de coordinación.

**Específicos** (cada uno se corresponde con una consigna del TP):
1. Derivar el consumidor marginal para un tamaño esperado de red dado (consigna 1).
2. Hallar todos los equilibrios de expectativas autocumplidas (EEA) y clasificarlos por estabilidad (consigna 2).
3. Calcular la masa crítica y simular la dinámica de adopción (consigna 3).
4. Analizar el *lock-in* y la inercia y cuantificar los efectos de la interoperabilidad y los subsidios (consigna 4).
5. Vincular los resultados con el resto del programa (monopolio, discriminación de precios, juegos, oligopolio, relaciones verticales, innovación).

---

## 2. Desarrollo cuantitativo (resolución de la consigna)

**Datos:** U = θ·(α·nᵉ) − P, con θ ~ U[0,1], α = 1 y P = 0,16. Población normalizada en 1.

### Consigna 1 — Consumidor marginal
El consumidor θ adopta si θ·α·nᵉ − P ≥ 0. El indiferente cumple:

$$\bar\theta(n^e)=\frac{P}{\alpha\,n^e}=\frac{0{,}16}{n^e}$$

Adoptan todos los θ ≥ θ̄, así que la **demanda dada la expectativa** es

$$D(n^e)=1-\bar\theta=1-\frac{0{,}16}{n^e}\quad\text{si } n^e\ge 0{,}16;\qquad D(n^e)=0 \text{ si } n^e<0{,}16$$

**Lectura económica:** si se espera menos del 16 % de adopción (nᵉ < P/α), ni siquiera el usuario más intensivo (θ = 1) adopta. Así se ve el **problema del huevo y la gallina**: la demanda es creciente en las expectativas (∂D/∂nᵉ = P/(α nᵉ²) > 0) y decreciente en el precio.

### Consigna 2 — Equilibrios de expectativas autocumplidas y estabilidad
En un EEA las expectativas se verifican, es decir, nᵉ = n:

$$n=1-\frac{0{,}16}{n}\;\Longleftrightarrow\; n^2-n+0{,}16=0\;\Longleftrightarrow\; P=\alpha\,n(1-n)$$

$$n=\frac{1\pm\sqrt{1-4(0{,}16)}}{2}=\frac{1\pm0{,}6}{2}\;\Rightarrow\; n_L=0{,}2,\quad n_H=0{,}8$$

A estos se suma el equilibrio trivial **n = 0**. Verificación con las propiedades de las raíces vistas en la U9: n_L + n_H = 1 y n_L·n_H = 0,16 = P. Como P = 0,16 < P_max = α/4 = 0,25, la red es **viable**: el costo de adopción podría subir hasta un 56 % antes de que desaparezcan los equilibrios interiores.

**Estabilidad.** Hay dos maneras equivalentes de verla, y conviene presentar las dos en el paper:

- **Exceso de adopción:** D(n) − n = −(n − 0,2)(n − 0,8)/n. Es negativo en (0; 0,2), donde el mercado se contrae; positivo en (0,2; 0,8), donde se expande; y negativo en (0,8; 1], donde se contrae.
- **Pendiente de la función de reacción de expectativas:** D′(n) = P/(α n²). En n_L vale D′(0,2) = 4 > 1, que corresponde a un equilibrio **inestable**; en n_H vale D′(0,8) = 0,25 < 1, que corresponde a uno **estable**. Para n = 0, cualquier expectativa menor a 0,16 genera D = 0, así que también es **estable**.

| Equilibrio | n | θ̄ | Estabilidad | Interpretación |
|---|---|---|---|---|
| No adopción | 0 | — | Estable | “Nadie quiere ser el primero” |
| Masa crítica | 0,2 | 0,8 | **Inestable** | Umbral entre el fracaso y el éxito de la red |
| Alta adopción | 0,8 | 0,2 | Estable | Red autosostenida |

*Figuras 1 y 2:* `figuras/fig1_demanda_red.png` (campana p(n) = α n(1−n) contra P) y `figuras/fig2_expectativas.png` (D(nᵉ) contra la recta de 45°).

### Consigna 3 — Masa crítica y dinámica
$$n_L(P,\alpha)=\frac{1-\sqrt{1-4P/\alpha}}{2}=0{,}2$$

Hace falta que **al menos el 20 % de la población** (o la expectativa compartida de ese 20 %) adopte para que la red crezca sola hasta el 80 %. Con expectativas adaptativas, n_{t+1} = D(n_t) (simulación en `figuras/fig3_dinamica.png`):

| n₀ | Trayectoria | Destino |
|---|---|---|
| 0,19 | 0,19 → 0,158 → 0 | Colapso |
| 0,21 | 0,21 → 0,238 → 0,328 → 0,512 → 0,688 → … | 0,8 |
| 0,25 | 0,25 → 0,36 → 0,556 → 0,712 → 0,775 → … | 0,8 |
| 1,00 | 1 → 0,84 → 0,81 → … | 0,8 |

**Estática comparativa** (sirve para H2 y para la Figura 4, `figuras/fig4_masa_critica.png`):
- ∂n_L/∂P = 1/(α√(1−4P/α)) = 1/0,6 ≈ 1,67: cada 0,01 adicional de costo de adopción **sube** la masa crítica en alrededor de 1,7 puntos porcentuales.
- ∂n_L/∂α = −P/(α²√(1−4P/α)) ≈ −0,27: una red más intensa o más interconectada **baja** la masa crítica.

### Consigna 4 — *Lock-in*, inercia y políticas

**(a) Ineficiencia del equilibrio alto (sub-adopción, U9 §7).** El bienestar bruto es W(n) = ∫₁₋ₙ¹ θ α n dθ = α n²(2−n)/2. Si P es un costo real de adopción:

| Escenario | n | W bruto | Costo P·n | W neto |
|---|---|---|---|---|
| Trampa (n = 0) | 0 | 0 | 0 | **0** |
| Mercado (n_H) | 0,8 | 0,384 | 0,128 | **0,256** |
| Óptimo social | 1 | 0,5 | 0,16 | **0,34** |

Aun en el equilibrio “bueno” hay sub-adopción (la pérdida es 0,084), porque el adoptante marginal (θ = 0,2) recibe un beneficio privado de 0,16 pero genera una externalidad de α∫₀,₂¹ θ dθ = 0,48 sobre los demás, que no internaliza. Este es el argumento clásico para un **subsidio pigouviano a la adopción**.

**(b) *Lock-in* entre billeteras incompatibles.** Sea A el incumbente con n_A = 0,8 y B un entrante de mejor calidad (α_B > α_A). Un usuario migra si θ α_B n_Bᵉ − P_B − s > θ α_A n_A − P_A, donde s es el costo de cambio (aprendizaje, saldo, historial, contactos). Si n_Bᵉ ≈ 0, nadie migra, aunque una migración coordinada fuera Pareto superior. Es la **inercia excesiva** de Farrell y Saloner (1985) y el caso QWERTY (David, 1985). La base instalada funciona como **barrera a la entrada endógena** (U1, U6).

**(c) Interoperabilidad.** Si las redes son compatibles en un grado β ∈ [0,1], el valor de la billetera i pasa a ser θ α (n_i + β n_j). Con β = 1 (QR y transferencias interoperables), el efecto de red pasa a ser del **sistema** y no de la marca:
- un entrante hereda la base instalada, de modo que su masa crítica “propia” tiende a 0;
- la competencia pasa de ser **“por el mercado”** a ser **“en el mercado”** (precio, comisiones, cashback, servicios: Bertrand diferenciado y Hotelling, U5 y U7);
- en términos del modelo agregado, aumenta la α efectiva y baja n_L (Figura 4).
- *Trade-off* (U9 §7.4): al incumbente no le conviene la compatibilidad, porque pierde el poder de mercado que le da el *lock-in*. Por eso se trata de una **regulación** (BCRA) y no de un resultado espontáneo del mercado.

**(d) Subsidios iniciales (precio de penetración, U9 §6.3–6.4).**
- Un **subsidio transitorio general** s baja el costo efectivo a P − s. Por ejemplo, con s = 0,07 el costo queda en P = 0,09 y la masa crítica en n_L = (1 − √0,64)/2 = **0,10**, la mitad. Con s ≥ 0,16 (adopción gratis o con reintegro total) desaparece el equilibrio n = 0 y adoptan todos. Al retirar el subsidio, como n > 0,2, el mercado converge a 0,8 (Figura 3, trayectoria n₀ = 1).
- Un **subsidio focalizado** a los usuarios de mayor θ alcanza para “sembrar” el 20 %: costa alrededor de 0,2 × 0,16 = **0,032** per cápita y lleva el mercado de W = 0 a W = 0,256. La relación beneficio/costo ronda 8 a 1. Este es el argumento económico de los reintegros y el cashback, de los programas de tipo Cuenta DNI y del subsidio cruzado a un lado de la plataforma (Rochet y Tirole: se le cobra menos al lado “difícil”).
- **Coordinación de expectativas:** anuncios creíbles, adhesión masiva de bancos el mismo día (la estrategia de lanzamiento de MODO) y compromisos públicos. Son mecanismos que mueven nᵉ sin necesidad de mover P.

**(e) Precio de monopolio como referencia (U2 y U9 §7.2).** Si un solo operador eligiera P, maximizaría π = α n²(1 − n), lo que da n_m = 2/3, P_m = 2/9 ≈ 0,222 y una masa crítica de 1/3. Que el costo observado (0,16) sea menor que 2/9 es consistente con **presión competitiva** (MODO y los bancos) o con una **estrategia de penetración**.

---

## 3. Relación con las unidades de la materia

| Unidad | Concepto de clase | Cómo entra en el paper |
|---|---|---|
| **U1** — Introducción, ECD, barreras, mercado relevante | Paradigma estructura–conducta–desempeño; barreras a la entrada; test SSNIP | Los efectos de red generan una **estructura concentrada** (*winner-takes-most*). ¿Cuál es el mercado relevante: billeteras, pagos digitales o medios de pago en general? |
| **U2** — Monopolio | Lerner, peso muerto, monopolio natural, Ramsey, firma dominante con franja competitiva | Monopolio de red (n = 2/3, P = 2/9) y pérdida de peso muerto; Mercado Pago como **firma dominante** frente a una franja de billeteras bancarias |
| **U3** — Discriminación de precios | Segundo grado (tarifa en dos partes, *versioning*), tercer grado, intertemporal | El cashback por banco, día o segmento es discriminación de tercer grado; el *freemium* y las comisiones a comercios funcionan como tarifa en dos partes; el precio de penetración es discriminación intertemporal |
| **U4a** — Juegos estáticos | Equilibrio de Nash, **Caza del Ciervo** (equilibrio Pareto-dominante frente a equilibrio seguro), Batalla de los Sexos | La trampa de coordinación **es** una Caza del Ciervo: (adoptar, adoptar) es Pareto-dominante, pero (no adoptar, no adoptar) también es un equilibrio de Nash. La elección entre Mercado Pago y MODO es una Batalla de los Sexos (todos quieren coordinar, pero cada uno prefiere un estándar distinto) |
| **U4b** — Juegos dinámicos | ENPS, compromisos creíbles, ventaja del primero | La ventaja del que llega primero (Mercado Pago) se parece al liderazgo de Stackelberg. La base instalada es un compromiso creíble, y el anuncio coordinado de los bancos es un compromiso para mover expectativas |
| **U5** — Oligopolio | Bertrand diferenciado, equilibrios múltiples | Con interoperabilidad, las billeteras compiten en comisiones y beneficios como en un Bertrand diferenciado |
| **U6** — Colusión y barreras | Cooperación entre rivales; precio límite y predación; Dixit | MODO es cooperación entre bancos competidores para alcanzar la masa crítica (¿riesgo antitrust o eficiencia?). Los subsidios agresivos plantean la pregunta de si son penetración o predación. La base instalada funciona como la “capacidad” de Dixit, es decir, como compromiso disuasorio |
| **U7** — Diferenciación | Hotelling, diferenciación vertical | Las billeteras se diferencian horizontalmente (ecosistema de e-commerce frente a banco tradicional) y verticalmente (la “calidad” depende del tamaño de la red); *multihoming* |
| **U8** — Relaciones entre empresas | Integración vertical, **foreclosure**, fusiones de conglomerado | La integración Mercado Libre–Mercado Pago implica ventajas de ecosistema y riesgo de cierre de mercado. El QR interoperable es una política **anti-foreclosure** |
| **U9** — Economías de red | EEA, equilibrios múltiples, masa crítica, sub-adopción, *lock-in*, Rochet-Tirole | **Núcleo del paper**, con las consignas 1 a 4 |
| **U10** — Innovación | Schumpeter, Arrow (efecto reemplazo), estándares | Las fintech como destrucción creativa frente a la banca; el efecto reemplazo de Arrow ayuda a explicar por qué los bancos incumbentes innovaron tarde |
| **U11** — Aplicaciones empíricas | Diferencias en diferencias, panel | Extensión propuesta: un diseño DiD sobre la adopción antes y después del QR interoperable con datos del BCRA (sección de limitaciones y trabajo futuro) |

**Hilo conductor que proponemos para la exposición oral:**
efecto de red → expectativas → equilibrios múltiples (Caza del Ciervo) → masa crítica → *lock-in* del primero en llegar → política: interoperabilidad (cambia α y la competencia) y subsidio (cambia P y las expectativas).

---

## 4. Estructura del paper (según los *Lineamientos*)

| Sección | Contenido | Extensión orientativa |
|---|---|---|
| **Carátula** | UADE, FCE, cátedra; título; integrantes; docente | — |
| **Resumen / Abstract** | 100 a 150 palabras: problema, modelo, resultados (n_L = 0,2; n_H = 0,8) y política | ½ página |
| **1. Introducción** | Tema, pregunta (1.2), enfoque, justificación (relevancia para la inclusión financiera y para la defensa de la competencia en plataformas) y estructura del trabajo | 1 a 1½ páginas |
| **2. Estado de la cuestión** | Organizado en **cuatro ejes**: (i) externalidades de red y expectativas (Rohlfs, 1974; Katz y Shapiro, 1985; Economides, 1996); (ii) estándares, *lock-in* y dependencia de la trayectoria (David, 1985; Farrell y Saloner, 1985; Arthur, 1989); (iii) plataformas de dos lados y el problema del huevo y la gallina (Caillaud y Jullien, 2003; Rochet y Tirole, 2003, 2006; Armstrong, 2006); (iv) evidencia empírica en pagos digitales (Crouzet, Gupta y Mezzanotti, 2023; BCRA) | 2 a 3 páginas |
| **3. Metodología** | Modelo teórico calibrado (supuestos: θ uniforme, expectativas autocumplidas, α = 1, P = 0,16); estática comparativa; simulación de la dinámica; supuestos explícitos y sus límites | 1 página |
| **4. Desarrollo y resultados** | Consignas 1 a 4 (sección 2 de este documento) con las Figuras 1 a 4 y las tablas | 4 a 5 páginas |
| **5. Discusión: el caso argentino** | Mercado Pago frente a MODO a la luz del modelo; interoperabilidad del BCRA; subsidios y reintegros; vínculos con U2–U10 (tabla de la sección 3) | 2 páginas |
| **6. Conclusiones** | Respuesta a la pregunta; H1–H3 aceptadas o matizadas; limitaciones (modelo de un solo lado, θ uniforme, expectativas, ausencia de datos) y trabajo futuro (modelo de dos lados, DiD) | 1 página |
| **Bibliografía** | APA, al menos 10 referencias | — |
| **Anexos** | Derivaciones completas (raíces, estabilidad, bienestar), código de simulación (`figuras.py`) y tabla de trayectorias | — |

---

## 5. Bibliografía sugerida (APA; verificar cada referencia antes de citarla)

- Armstrong, M. (2006). Competition in two-sided markets. *The RAND Journal of Economics, 37*(3), 668–691.
- Arthur, W. B. (1989). Competing technologies, increasing returns, and lock-in by historical events. *The Economic Journal, 99*(394), 116–131.
- Banco Central de la República Argentina. (s. f.). *Informe de Pagos Minoristas* [serie mensual]. BCRA. *(Fuente de datos para la sección 5.)*
- Caillaud, B., & Jullien, B. (2003). Chicken & egg: Competition among intermediation service providers. *The RAND Journal of Economics, 34*(2), 309–328.
- Crouzet, N., Gupta, A., & Mezzanotti, F. (2023). Shocks and technology adoption: Evidence from electronic payment systems. *Journal of Political Economy, 131*(11), 3003–3065.
- David, P. A. (1985). Clio and the economics of QWERTY. *The American Economic Review, 75*(2), 332–337.
- Economides, N. (1996). The economics of networks. *International Journal of Industrial Organization, 14*(6), 673–699.
- Farrell, J., & Saloner, G. (1985). Standardization, compatibility, and innovation. *The RAND Journal of Economics, 16*(1), 70–83.
- Katz, M. L., & Shapiro, C. (1985). Network externalities, competition, and compatibility. *The American Economic Review, 75*(3), 424–440.
- Pepall, L., Richards, D., & Norman, G. (2006). *Organización industrial: Teoría y práctica contemporáneas* (3.ª ed.). Thomson. *(Cap. 22; libro de la cátedra.)*
- Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. *Journal of the European Economic Association, 1*(4), 990–1029.
- Rochet, J.-C., & Tirole, J. (2006). Two-sided markets: A progress report. *The RAND Journal of Economics, 37*(3), 645–667.
- Rohlfs, J. (1974). A theory of interdependent demand for a communications service. *The Bell Journal of Economics and Management Science, 5*(1), 16–37.
- Shapiro, C., & Varian, H. R. (1999). *Information rules: A strategic guide to the network economy*. Harvard Business School Press.

*Nota:* la *Rúbrica* (criterio 1) penaliza usar un único material bibliográfico, el libro de la cátedra. Por eso conviene citar al menos un artículo de cada eje del estado de la cuestión.

---

## 6. Checklist frente a la rúbrica

- [ ] **Criterio 1 (30 %), modelo y herramientas matemáticas:** derivación completa, estabilidad por dos vías, estática comparativa, bienestar y las 4 figuras con número, ejes y fuente (“Elaboración propia”).
- [ ] **Criterio 2 (20 %), estructura e hilo conductor:** cada sección cierra con una oración que abre la siguiente; se usa el hilo propuesto en la sección 3.
- [ ] **Criterio 3 (20 %), participación:** repartir secciones (por ejemplo: A, introducción y estado de la cuestión; B, metodología y consignas 1–2; C, consignas 3–4 y figuras; D, caso argentino y conclusiones) y llevar los avances a las clases de consulta.
- [ ] **Criterio 4 (30 %), defensa:** preparar preguntas para el público, por ejemplo: *“¿por qué n = 0,2 es un equilibrio pero nunca lo observamos?”* o *“¿conviene obligar a la interoperabilidad si eso reduce el incentivo a invertir del pionero?”* (tensión con U10, Schumpeter).
- [ ] Verificar los datos del BCRA y las fechas regulatorias; completar la sección 5 del paper con estadísticas reales de adopción (Informe de Pagos Minoristas del BCRA).
- [ ] Redactar con palabras propias y citar todo (control de plagio).
