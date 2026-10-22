# Guía didáctica — Todo lo que hay que entender para resolver el TP 6

**Organización Industrial — UADE — Grupo 6**
Tema: *Efectos de red, masa crítica y trampas de coordinación en billeteras virtuales (Mercado Pago, MODO)*

> **Cómo usar esta guía:** está ordenada de lo más básico a lo más complejo.
> - **Parte A:** las herramientas matemáticas mínimas.
> - **Parte B:** la Unidad 9, paso a paso. Es el corazón del TP.
> - **Parte C:** el resto de las unidades, explicando *para qué* sirve cada una en este problema.
> - **Parte D:** un glosario rápido de parámetros y conceptos.
>
> Cada concepto se presenta en tres capas: **qué es → por qué importa → ejemplo con billeteras**.

---

## PARTE A — Herramientas matemáticas que se usan

### A.1 La distribución uniforme: θ ~ U[0,1]
**Qué es.** Decir que θ (theta) sigue una distribución uniforme entre 0 y 1 significa que los consumidores están **repartidos de forma pareja** en ese intervalo. Imaginen 100 personas formadas en una fila ordenada de menor a mayor θ: la primera tiene θ = 0, la del medio θ = 0,5 y la última θ = 1, con la misma cantidad de gente en cada tramo.

**La propiedad clave que usamos:** la fracción de personas con θ mayor o igual a un valor x es simplemente **1 − x**.
- ¿Qué fracción tiene θ ≥ 0,8? → 1 − 0,8 = **0,2** (el 20 %).
- ¿Qué fracción tiene θ ≥ 0,2? → 1 − 0,2 = **0,8** (el 80 %).

Por eso, cuando encontramos al “consumidor indiferente” θ̄, la cantidad de adoptantes es directamente **1 − θ̄**.

### A.2 La ecuación cuadrática
Una ecuación del tipo a·n² + b·n + c = 0 se resuelve con la fórmula resolvente:

$$n=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

En el TP aparece n² − n + 0,16 = 0, es decir, a = 1, b = −1 y c = 0,16:

$$n=\frac{1\pm\sqrt{1-0{,}64}}{2}=\frac{1\pm0{,}6}{2}\Rightarrow n=0{,}2\ \text{ o }\ n=0{,}8$$

**Truco de verificación (propiedades de las raíces):** para n² − n + P = 0, la suma de las raíces es 1 y el producto es P. Comprobación: 0,2 + 0,8 = 1 y 0,2 × 0,8 = 0,16. ✓

**El discriminante** (lo que está dentro de la raíz, 1 − 4P) dice cuántas soluciones hay:
- si es mayor que 0 (P < 0,25), hay **dos** equilibrios interiores;
- si es igual a 0 (P = 0,25), hay **uno** (n = 0,5);
- si es menor que 0 (P > 0,25), **no hay ninguno**: la red no puede sostenerse.

### A.3 Derivadas: para qué las usamos
La derivada mide **cuánto cambia una cosa cuando cambia otra un poquito**. En el TP la usamos para tres cosas:
1. **Encontrar máximos**, por ejemplo el precio que maximiza el beneficio de un monopolista: se iguala la derivada a cero (condición de primer orden, **CPO**).
2. **Estática comparativa:** si sube el precio P, ¿cuánto sube la masa crítica? Eso es ∂n_L/∂P.
3. **Estabilidad:** comparar la pendiente de una curva con la recta de 45° (lo vemos en B.6).

### A.4 Integrales: para medir bienestar
Para sumar la utilidad de *todos* los consumidores que adoptan se usa la integral, que en este contexto es una suma continua. Si adoptan los tipos θ entre 1 − n y 1, y cada uno obtiene θ·n, el bienestar total es:

$$W(n)=\int_{1-n}^{1}\theta\, n\, d\theta=\frac{n^2(2-n)}{2}$$

### A.5 Sistemas dinámicos simples: n_{t+1} = D(n_t)
Es una regla que dice: “la adopción de mañana depende de lo que la gente ve hoy”. Arrancando de un valor inicial n₀, se aplica la regla una y otra vez y se observa **hacia dónde converge**. Con eso se simula si la red crece o colapsa.

---

## PARTE B — Unidad 9: Economías de red (el corazón del TP)

### B.1 ¿Qué es un efecto de red?
**Qué es.** Hay **efecto de red** (o externalidad de red) cuando el valor que una persona obtiene de un bien **aumenta con la cantidad de otras personas que lo usan**. Formalmente, ∂v/∂n > 0: la utilidad sube cuando sube n.

**Por qué importa.** En un mercado “normal” (comprar un alfajor) me da igual cuántos otros compran ese alfajor. En un mercado de red, lo que hacen los demás **cambia mi decisión**. Eso rompe la lógica habitual de oferta y demanda.

**Ejemplo con billeteras.** Una billetera virtual que no acepta ningún comercio y a la que ninguno de mis amigos puede transferirle plata **no me sirve para nada**, por más linda que sea la app. Si todos los kioscos aceptan su QR, en cambio, me resulta muy útil.

**Dos tipos de efecto de red:**

| Tipo | Qué es | En billeteras |
|---|---|---|
| **Directo** (*same-side*) | Me beneficia que haya más usuarios **del mismo tipo** que yo | Más amigos con Mercado Pago → más fácil dividir gastos y transferir |
| **Indirecto** (*cross-side*) | Me beneficia que haya más usuarios **del otro lado** de la plataforma | Más **comercios** que aceptan el QR → más útil para el **usuario**, y viceversa |

Las billeteras tienen **ambos**, pero el más fuerte es el **indirecto**: por eso son un **mercado de dos lados** (ver B.11).

**Ley de Metcalfe (intuición):** con n usuarios hay n(n−1)/2 conexiones posibles, así que el valor crece *más rápido* que la cantidad de usuarios.

### B.2 La función de utilidad del TP, término por término

$$U=\theta\cdot(\alpha\cdot n^e)-P$$

| Símbolo | Nombre | Qué significa | Ejemplo / interpretación |
|---|---|---|---|
| **U** | Utilidad neta | Beneficio neto de adoptar la billetera. Si U ≥ 0 la persona adopta; si U < 0, no | Es la “cuenta mental” de cada persona |
| **θ** (theta) | Tipo del consumidor / **intensidad de uso** | Cuánto aprovecharía esa persona la billetera. Va de 0 (no la usaría casi nunca) a 1 (la usaría todo el tiempo) | θ alto: un joven que paga todo con el celular o un comerciante. θ bajo: un jubilado que paga en efectivo |
| **θ ~ U[0,1]** | Distribución de los tipos | Hay consumidores de todas las intensidades, repartidos parejo | Permite contar adoptantes con “1 − θ̄” |
| **nᵉ** | **Tamaño esperado de la red** | La fracción de la población que la persona *cree* que va a usar la billetera (entre 0 y 1) | “¿Cuántos de mis contactos y comercios van a estar en MODO?” |
| **α** (alfa) | **Intensidad del efecto de red** | Cuánto valor agrega cada unidad de red. Con α = 1, el valor proviene esencialmente de cuántos la usan | α alto: la red vale mucho (por ejemplo, con QR interoperable). α bajo: la red importa poco |
| **α·nᵉ** | Valor de la red | Lo que vale “estar conectado” a una red de tamaño nᵉ | — |
| **θ·α·nᵉ** | Beneficio bruto | Valor de la red multiplicado por cuánto la usa esa persona | La red le vale más a quien más la usa |
| **P** | **Precio o costo efectivo de adopción** | Todo lo que cuesta adoptar, no solo el precio monetario | Las apps suelen ser gratis, pero hay costos: abrir la cuenta, validar identidad, aprender a usarla, la desconfianza, las comisiones y el tiempo. En el TP, P = 0,16 |

**Detalle importante:** como la utilidad es **θ × nᵉ** (multiplicación), el efecto de red y la intensidad de uso **se potencian**. Si nᵉ = 0, la utilidad bruta es 0 para *todos*, incluso para el θ más alto.

### B.3 Expectativas: por qué aparece nᵉ y no n
**Qué es.** Cuando decido si me bajo la app, todavía **no sé** cuántos la van a adoptar. Decido según lo que **espero** (nᵉ).

**Por qué importa.** Las expectativas pueden **autocumplirse**:
- Si todos creen que la billetera va a fracasar, nadie la adopta, y efectivamente fracasa.
- Si todos creen que va a triunfar, todos la adoptan, y efectivamente triunfa.

Esto convierte a las **expectativas en una variable económica clave**, tan importante como el precio. Las empresas gastan en publicidad masiva, anuncios del tipo “ya somos 10 millones” y lanzamientos coordinados justamente para **mover expectativas**.

### B.4 Consigna 1 — El consumidor marginal (indiferente)
**Qué es.** Es la persona a la que **le da exactamente igual** adoptar o no (U = 0). Todas las personas “más intensas” que ella adoptan, y las “menos intensas”, no.

**Cómo se obtiene:**

$$\theta\cdot\alpha\, n^e-P=0\;\Rightarrow\;\bar\theta=\frac{P}{\alpha\,n^e}=\frac{0{,}16}{n^e}$$

**Demanda dada la expectativa** (fracción que adopta):

$$D(n^e)=1-\bar\theta=1-\frac{0{,}16}{n^e}$$

**Ejemplos numéricos para entenderlo:**

| Si la gente espera nᵉ = | θ̄ = 0,16/nᵉ | Adoptan D = 1 − θ̄ | ¿Se cumple la expectativa? |
|---|---|---|---|
| 0,10 | 1,6 (> 1) | 0 (nadie) | Esperaban 10 % y adopta 0 % → **baja** |
| 0,20 | 0,8 | 0,20 | Esperaban 20 % y adopta 20 % → **se cumple** |
| 0,50 | 0,32 | 0,68 | Esperaban 50 % y adopta 68 % → **sube** |
| 0,80 | 0,2 | 0,80 | Esperaban 80 % y adopta 80 % → **se cumple** |
| 1,00 | 0,16 | 0,84 | Esperaban 100 % y adopta 84 % → **baja** |

**Lecturas clave:**
- **Cuanto mayor es la red esperada, más bajo es el umbral θ̄**, porque hasta usuarios poco intensos se suman.
- **Cuanto mayor es P, más alto es θ̄**, porque solo los muy intensos adoptan.
- Si nᵉ < 0,16, θ̄ > 1 y **nadie adopta**: ni el usuario más fanático ve valor en una red tan chica. Esto es el **problema del huevo y la gallina**: nadie quiere ser el primero.

### B.5 Consigna 2 — Equilibrio de Expectativas Autocumplidas (EEA)
**Qué es.** Es una situación en la que **lo que la gente espera coincide con lo que efectivamente pasa**: nᵉ = n. Es el concepto de equilibrio de Katz y Shapiro (1985). En las filas “se cumple” de la tabla anterior hay EEA.

**Cómo se calcula:** se reemplaza nᵉ por n en la demanda y se pide que la demanda sea igual a n:

$$n=1-\frac{0{,}16}{n}\;\Rightarrow\;n^2-n+0{,}16=0\;\Rightarrow\;n_L=0{,}2;\ n_H=0{,}8$$

A esas dos soluciones se suma **n = 0**: si nadie espera nada, nadie adopta, y la expectativa se cumple.

**La curva de demanda de red en equilibrio.** Si se despeja P de la ecuación anterior:

$$P=\alpha\,n(1-n)$$

Esta curva tiene forma de **campana** (parábola invertida), con máximo en n = 0,5 y P_max = 0,25.
- **Tramo ascendente (n < 0,5):** domina el **efecto red**. Más usuarios hacen que la red valga más, así que se puede pagar más.
- **Tramo descendente (n > 0,5):** domina el **efecto de “quién queda por sumarse”**. Los que faltan son de θ bajo y valoran poco, así que solo entran con un P más bajo.

Gráficamente, los EEA son los **cortes de la campana con la recta horizontal P = 0,16**: hay dos cortes, en 0,2 y en 0,8 (Figura 1 del planteo).

**¿Por qué hay equilibrios múltiples?** En la demanda “normal” (decreciente) cada precio corresponde a una sola cantidad. Acá, como la curva **sube y después baja**, una misma recta de precio la corta dos veces. **Los equilibrios múltiples son la firma de los mercados de red.**

### B.6 Consigna 2 (cont.) — Estabilidad: ¿cuáles equilibrios se observan?
**Qué es la estabilidad.** Un equilibrio es **estable** si, cuando se lo “empuja” un poco, vuelve solo, como una bolita en el fondo de un pozo. Es **inestable** si al empujarlo se aleja cada vez más, como una bolita en la punta de una montaña.

**Método 1: comparar lo que adopta la gente con lo que se esperaba.**
- Si D(n) > n (adoptan *más* de lo esperado), las expectativas se corrigen hacia arriba y **n sube**.
- Si D(n) < n (adoptan *menos* de lo esperado), **n baja**.

| Zona | Ejemplo | D(n) vs n | Movimiento |
|---|---|---|---|
| 0 < n < 0,2 | n = 0,1 | D = 0 < 0,1 | Baja hacia **0** |
| 0,2 < n < 0,8 | n = 0,5 | D = 0,68 > 0,5 | Sube hacia **0,8** |
| 0,8 < n ≤ 1 | n = 1 | D = 0,84 < 1 | Baja hacia **0,8** |

Así se ve que **0 y 0,8 “atraen”** a la economía y **0,2 “repele”**:
- **n = 0: estable.** Es la trampa: “si nadie la usa, nadie la quiere”.
- **n = 0,2: inestable.** Es el **punto de quiebre** o **masa crítica**.
- **n = 0,8: estable.** Es el éxito de la red.

**Método 2 (más formal): la pendiente.** Se compara la pendiente de D(n) con la de la recta de 45°, que vale 1. D′(n) = P/n², así que D′(0,2) = 4 > 1 (**inestable**) y D′(0,8) = 0,25 < 1 (**estable**). Intuición: si la curva es más empinada que 45°, cualquier desvío se *amplifica*.

**Por qué importa:** en la realidad solo vemos equilibrios estables. n = 0,2 **nunca se observa**: es una frontera invisible entre el fracaso y el éxito. Es una gran pregunta para la defensa oral.

### B.7 Consigna 3 — Masa crítica
**Qué es.** Es la **mínima fracción de adoptantes** (o de adopción *esperada*) a partir de la cual la red **crece sola** hasta el equilibrio alto. Es el equilibrio inestable n_L:

$$n_L=\frac{1-\sqrt{1-4P/\alpha}}{2}=0{,}2$$

**Traducción:** si la billetera logra que el 20 % de la población la use (o que todos crean que la va a usar al menos el 20 %), después **no hace falta empujar más**: el efecto red la lleva sola al 80 %. Si se queda en 19 %, se cae a cero.

**Simulación** (la gente ajusta según lo que vio el período anterior):
- arrancando en 0,19: 0,19 → 0,158 → 0, y **colapsa**;
- arrancando en 0,21: 0,21 → 0,238 → 0,328 → 0,512 → 0,688 → … → **0,8**.

Una diferencia de apenas 2 puntos al inicio define el destino completo de la red. Esto se llama **dependencia de la trayectoria** (*path dependence*): la historia importa.

**De qué depende la masa crítica (estática comparativa):**
- **Sube con P:** si adoptar es más caro, hace falta una red inicial más grande para que valga la pena. Cada 0,01 de aumento en P sube la masa crítica en alrededor de 1,7 puntos porcentuales.
- **Baja con α:** si la red es más valiosa por usuario, alcanza con menos gente. Aquí entra la interoperabilidad (B.10).

**Estrategias para superar la masa crítica** (U9 §6.3):
- **Precio de penetración:** cobrar muy poco o nada al principio para atraer a los primeros.
- **Subsidiar al lado difícil:** cashback a usuarios o terminales gratis a comercios.
- **Compromisos y anuncios creíbles:** “30 bancos lanzan MODO el mismo día”.
- **Compatibilidad hacia atrás:** que funcione con lo que la gente ya usa (CBU/CVU, tarjetas).
- **Beneficios para los primeros en adoptar.**

### B.8 Eficiencia: la sub-adopción y la externalidad de red
**Qué es la externalidad.** Cuando yo adopto la billetera, **les agrego valor a todos los demás usuarios** (ahora pueden pagarme o cobrarme), pero **no cobro nada por eso** y por lo tanto **no lo tengo en cuenta** al decidir. Es una **externalidad positiva no internalizada**.

**Consecuencia:** el mercado genera **menos adopción que la socialmente óptima** (sub-adopción), igual que se produce “demasiado poco” de cualquier bien con externalidad positiva.

**En números (si P es un costo real de adoptar):**

| Situación | Adopción | Bienestar neto |
|---|---|---|
| Trampa | 0 | 0 |
| Equilibrio de mercado alto | 0,8 | 0,256 |
| Óptimo social | 1 | 0,34 |

El usuario marginal (θ = 0,2) obtiene de la red un beneficio privado de 0,16, pero les genera a los demás un beneficio extra de 0,48 que no tiene en cuenta. **Remedio económico:** un subsidio a la adopción (subsidio *pigouviano*), que “le paga” al adoptante por la externalidad que genera.

### B.9 *Lock-in*, costos de cambio e inercia
**Qué es el *lock-in*.** Es quedar **“atrapado”** en una red o tecnología porque cambiarse cuesta mucho, aunque exista una alternativa mejor.

**Costos de cambio (*switching costs*) en billeteras:**
- **Pérdida de red:** mis contactos y los comercios que frecuento están en la otra.
- **Aprendizaje:** una app nueva, nuevos menús.
- **Activos y datos:** saldo invertido, historial, préstamos o calificación crediticia dentro de la app.
- **Ecosistema:** Mercado Pago está integrado con Mercado Libre (compras, envíos, cuotas).

**Inercia excesiva (Farrell y Saloner, 1985).** Supongamos que aparece una billetera B **mejor** (α_B más alto). Si **todos** se pasaran juntos, todos estarían mejor. Pero **cada uno solo** no se pasa, porque en B no hay nadie todavía (n_Bᵉ ≈ 0). El mercado se queda en la tecnología inferior. Es un **fallo de coordinación**, no de preferencias.

**Caso clásico:** el teclado **QWERTY** frente a Dvorak (David, 1985). Dvorak sería más eficiente, pero nadie cambia porque todos aprendieron QWERTY. Otro ejemplo es la guerra **VHS frente a Beta**.

**Implicancia para la competencia:** el que llega primero y supera la masa crítica obtiene una **ventaja que se autorrefuerza**: el ganador se lleva casi todo (*winner-takes-most*). La base instalada funciona como **barrera a la entrada**.

### B.10 Consigna 4 — Políticas para pasar al equilibrio alto

**1) Interoperabilidad (compatibilidad).**
- **Qué es:** que los usuarios de una red puedan operar con los de otra. En Argentina, el **QR interoperable** permite pagar con cualquier billetera en cualquier QR, y **Transferencias 3.0** es el esquema del BCRA para pagos con transferencia inmediata.
- **Cómo actúa en el modelo:** el valor de mi billetera pasa a depender de la red **total**, no solo de la de mi marca. Se puede escribir como θ·α·(n_propia + β·n_otra), con β ∈ [0,1] como grado de compatibilidad. Con β = 1, las redes se suman.
- **Efectos:**
  - aumenta el valor efectivo de la red (sube la α efectiva), lo que **baja la masa crítica**;
  - un entrante **hereda** la base instalada, lo que reduce el *lock-in*;
  - la competencia pasa de ser **“por el mercado”** (ganar la guerra de redes) a ser **“en el mercado”** (competir en comisiones, cashback y servicios).
- **Dilema:** al incumbente **no le conviene** la interoperabilidad, porque pierde la ventaja de su red. Por eso suele hacer falta **regulación**. El riesgo es reducir el incentivo a invertir del pionero (vínculo con U10).

**2) Subsidios iniciales.**
- **Qué es:** bajar temporalmente el costo efectivo de adopción, de P a P − s, mediante reintegros, cashback, descuentos o terminales gratis.
- **Efecto en el modelo:** baja la masa crítica. Con s = 0,07 queda P = 0,09 y n_L baja de 0,2 a **0,1**. Con s ≥ 0,16 (adoptar sale gratis) desaparece la trampa n = 0.
- **Por qué alcanza con que sea transitorio:** una vez superado el 20 %, se retira el subsidio y la red **sigue creciendo sola** hasta 0,8. Esa es la magia de la masa crítica.
- **Subsidio focalizado:** alcanza con subsidiar a los usuarios más intensos (θ ≥ 0,8, el 20 % superior) para “sembrar” la red. Cuesta alrededor de 0,032 por persona y genera un bienestar de 0,256: rinde unas 8 veces lo invertido.

**3) Coordinación de expectativas.** Anuncios, alianzas y lanzamientos simultáneos. No cambian P ni α: mueven **nᵉ**. Si la gente cree que la red va a pasar el 20 %, la red pasa el 20 %.

### B.11 Mercados de dos lados (Rochet y Tirole)
**Qué es.** Una **plataforma** atiende a dos grupos distintos (usuarios y comercios) y cada grupo valora la presencia del otro (efecto **indirecto** o **cruzado**).

**La idea central:** en estos mercados no solo importa **cuánto** cobra la plataforma en total (el *nivel* de precios), sino **a quién** le cobra (la *estructura* de precios). Cambiar quién paga cambia la cantidad de transacciones.

**Regla de Rochet y Tirole:** **cobrarle poco (o subsidiar) al lado “difícil”**, cuya presencia vale mucho para el otro lado, y **cobrarle más al lado “fácil”**.
- **Tarjetas de crédito:** el titular no paga nada o hasta recibe millas, mientras el comercio paga una comisión.
- **Billeteras:** la app es gratis para el usuario, con cashback, mientras el comercio paga una comisión por cobro (*merchant discount rate*).

**Relación con el TP:** el modelo del TP es una **versión simplificada de un solo lado**, que resume ambos lados en una sola red. En las limitaciones del paper hay que aclararlo y mencionar que con dos lados existe una masa crítica **en cada lado**: el huevo y la gallina (Caillaud y Jullien, 2003).

### B.12 Monopolio de red (como punto de comparación)
Si una sola empresa elige el precio sabiendo que P = n(1 − n), maximiza su beneficio π = P·n = n²(1 − n).
- **CPO:** 2n − 3n² = 0, de donde n_m = 2/3 y P_m = 2/9 ≈ 0,222.
- Su masa crítica a ese precio es **1/3**.
- Genera pérdida de bienestar por dos vías: el **efecto precio** (excluye consumidores, como cualquier monopolio) y el **efecto red** (al haber menos usuarios, los que están valoran menos la red).

**Uso en el TP:** P = 0,16 es **menor** que 0,222, lo que sugiere **presión competitiva** (MODO y los bancos) o una **estrategia de penetración**.

---

## PARTE C — Las otras unidades: para qué sirven en este problema

> Las unidades marcadas con ★ son **imprescindibles** para resolver las consignas. Las demás **enriquecen** la discusión y la defensa oral.

### C.1 Unidad 1 — Introducción, ECD, barreras y mercado relevante
- **Externalidades y fallas de mercado:** el mercado competitivo es eficiente *solo* si no hay externalidades. Los efectos de red son una externalidad, así que el mercado falla (sub-adopción).
- **Paradigma Estructura–Conducta–Desempeño (ECD):** la *estructura* (concentración por efectos de red) condiciona la *conducta* (subsidios, exclusividad, compatibilidad) y esta el *desempeño* (bienestar, adopción).
- **Barreras a la entrada:** la base instalada y la masa crítica son **barreras endógenas**. No son legales ni tecnológicas: surgen del propio efecto red.
- **Mercado relevante y test SSNIP:** ¿compiten las billeteras solo entre ellas, o también con el efectivo, la tarjeta de débito y la transferencia bancaria? Definir esto cambia cuánta “concentración” hay.

### C.2 ★ Unidad 2 — Monopolio
- **Ingreso marginal y CPO:** son las mismas herramientas que se usan en B.12 para el monopolio de red.
- **Pérdida de peso muerto (DWL):** sirve para medir la ineficiencia del monopolio de red.
- **Índice de Lerner, (P − CMg)/P:** mide el poder de mercado.
- **Firma dominante con franja competitiva:** Mercado Pago como firma dominante y las billeteras bancarias más chicas como franja.
- **Precio de Ramsey y tarifa en dos partes:** se conectan con la estructura de precios de las plataformas (cobrar distinto a cada lado).

### C.3 Unidad 3 — Discriminación de precios
- **Tercer grado** (precios distintos por grupo observable): cashback distinto por banco, por día (“los miércoles 20 %”) o para jubilados.
- **Segundo grado:** *freemium*, versiones (cuenta básica frente a cuenta con inversiones y crédito), tarifa en dos partes (cargo fijo más comisión por cobro para comercios).
- **Intertemporal:** **precio de penetración**, barato hoy y más caro mañana. Es exactamente la estrategia para superar la masa crítica.
- Idea útil: un **subsidio focalizado** a los usuarios de θ alto es una forma de discriminación que maximiza el impacto sobre la masa crítica.

### C.4 ★ Unidad 4a — Teoría de juegos estáticos
Es **la clave conceptual** de “trampa de coordinación”.
- **Equilibrio de Nash:** cada jugador hace lo mejor que puede dado lo que hacen los demás. Los EEA son, en el fondo, equilibrios de Nash de un juego de adopción.
- **Caza del Ciervo** (*stag hunt*): dos cazadores pueden cazar juntos un ciervo, que vale mucho pero requiere a ambos, o cada uno una liebre, que vale poco pero es segura.
  - Hay **dos equilibrios de Nash**: (Ciervo, Ciervo) y (Liebre, Liebre).
  - (Ciervo, Ciervo) es **Pareto-dominante** (todos están mejor), pero si no confío en que el otro coopere, me conviene la liebre.
  - **Traducción al TP:** “Ciervo” = adoptar la billetera (n = 0,8) y “Liebre” = seguir con efectivo (n = 0). La trampa de coordinación **es** una Caza del Ciervo.
- **Batalla de los Sexos:** dos jugadores quieren **coordinar en lo mismo**, pero cada uno prefiere una opción distinta. **Traducción:** la sociedad quiere un estándar común de pagos, pero Mercado Pago prefiere el suyo y los bancos prefieren MODO.
- **Óptimo de Pareto:** una situación en la que no se puede mejorar a nadie sin empeorar a otro. El equilibrio alto Pareto-domina a la trampa.

### C.5 Unidad 4b — Juegos dinámicos
- **Forma extensiva, inducción hacia atrás y ENPS:** sirven para analizar decisiones secuenciales (primero entra uno, después reacciona el otro).
- **Ventaja del primero (Stackelberg):** Mercado Pago llegó primero, acumuló base instalada y condiciona a los que vienen después.
- **Compromisos creíbles:** una amenaza o promesa solo funciona si conviene cumplirla. Un lanzamiento masivo de 30 bancos es un **compromiso creíble** que mueve las expectativas (nᵉ).
- **Disuasión a la entrada:** la base instalada puede disuadir la entrada de rivales.

### C.6 Unidad 5 — Oligopolio
- **Bertrand con productos diferenciados:** con interoperabilidad, el efecto red deja de diferenciar a las billeteras y compiten en precio y beneficios (comisiones, cashback).
- **Cournot y concentración (HHI):** sirven para medir la estructura del mercado.
- **Equilibrios múltiples en oligopolio:** son análogos a los de los mercados de red.
- **Competencia “por el mercado” frente a “en el mercado”:** sin interoperabilidad la pelea es por quedarse con toda la red; con interoperabilidad, por cada cliente.

### C.7 Unidad 6 — Colusión, precio límite, predación y barreras (Dixit)
- **Cooperación entre competidores:** MODO es una iniciativa conjunta de bancos rivales. ¿Es eficiente (alcanzar la masa crítica juntos) o riesgosa (facilita coordinar comisiones)?
- **Precio predatorio frente a penetración:** subsidiar mucho para alcanzar la masa crítica ¿es una estrategia legítima o una forma de expulsar rivales? El criterio de la clase: ¿hay pérdidas hoy que solo se recuperan *eliminando* la competencia?
- **Modelo de Dixit:** la capacidad instalada funciona como compromiso disuasorio, y la **base de usuarios** cumple ese rol en los mercados de red.

### C.8 Unidad 7 — Diferenciación de productos
- **Hotelling (ciudad lineal):** las billeteras se “ubican” en distintos lugares; por ejemplo, ecosistema de e-commerce y comercios informales frente a cliente bancarizado tradicional. El “costo de transporte” equivale al costo de usar una billetera que no es tu preferida.
- **Diferenciación vertical:** todos prefieren más calidad, y en redes la **calidad depende del tamaño de la red**.
- **Multihoming:** usar varias billeteras a la vez reduce el *lock-in*.

### C.9 Unidad 8 — Relaciones entre empresas
- **Integración vertical:** Mercado Libre y Mercado Pago forman un ecosistema integrado (marketplace, pagos, crédito, logística).
- **Foreclosure (cierre de mercado):** una empresa integrada puede negar el acceso a rivales, por ejemplo con QR que solo funcionan con su billetera. El **QR interoperable** es una política **contra el foreclosure**.
- **Doble marginalización:** en la cadena de pagos (emisor, adquirente, procesador, comercio) cada eslabón agrega su margen.
- **Fusiones de conglomerado:** su análisis tiene en cuenta los efectos de red (como en el caso Facebook–WhatsApp).

### C.10 Unidad 10 — Innovación
- **Schumpeter (destrucción creativa):** las fintech desplazan a la banca tradicional.
- **Arrow (efecto reemplazo):** el incumbente innova menos porque “canibaliza” su propio negocio, lo que explica por qué los bancos reaccionaron tarde.
- **Tensión de política:** obligar a la interoperabilidad reduce el *lock-in*, pero también el premio del innovador. Es un buen dilema para la defensa.

### C.11 Unidad 11 — Aplicaciones empíricas
- **Diferencias en diferencias (DiD):** compara la evolución de un grupo afectado por una política con la de uno no afectado, antes y después. Se podría medir el efecto del QR interoperable sobre la adopción.
- **Panel con efectos fijos:** sirve para datos de muchas entidades a lo largo del tiempo, como las billeteras por mes en el *Informe de Pagos Minoristas* del BCRA.
- En el paper básico alcanza con **proponerlo** como trabajo futuro.

---

## PARTE D — Glosario rápido

| Concepto | Definición en una línea |
|---|---|
| **θ** | Intensidad de uso o tipo del consumidor, entre 0 y 1 |
| **α** | Cuánto valor aporta cada unidad de red (intensidad del efecto red) |
| **nᵉ** | Fracción de la población que se *espera* que adopte |
| **n** | Fracción que *efectivamente* adopta |
| **P** | Costo efectivo de adoptar (precio, comisiones, tiempo, aprendizaje, desconfianza) |
| **θ̄** | Consumidor indiferente; adoptan los θ ≥ θ̄ |
| **D(nᵉ)** | Fracción que adopta dada la expectativa: 1 − P/(αnᵉ) |
| **EEA** | Equilibrio en el que la expectativa se cumple: nᵉ = n |
| **p(n) = αn(1−n)** | Curva de demanda de red en equilibrio (campana) |
| **P_max = α/4** | Precio máximo compatible con alguna red positiva |
| **n_L** | Equilibrio bajo, inestable: **masa crítica** |
| **n_H** | Equilibrio alto, estable: red exitosa |
| **Estable / inestable** | Vuelve solo tras un empujón / se aleja tras un empujón |
| **Masa crítica** | Umbral mínimo para que la red crezca sola |
| **Externalidad de red** | Beneficio que mi adopción da a otros y que no considero al decidir |
| **Sub-adopción** | El mercado adopta menos que el óptimo social |
| **Lock-in** | Quedar atrapado en una red por los costos de cambio |
| **Inercia excesiva** | No migrar a una tecnología mejor por falta de coordinación |
| **Dependencia de la trayectoria** | El resultado final depende de la historia y de las condiciones iniciales |
| **Interoperabilidad** | Las redes se conectan entre sí y el efecto red pasa a ser del sistema |
| **Precio de penetración** | Precio bajo inicial para alcanzar la masa crítica |
| **Mercado de dos lados** | Plataforma que conecta dos grupos que se valoran mutuamente |
| **Estructura de precios** | A qué lado se le cobra y cuánto |
| **Trampa de coordinación** | Quedarse en un equilibrio malo aunque exista uno mejor para todos |
| **Pareto-dominante** | Equilibrio en el que todos están mejor que en otro |

---

## Resumen en 10 líneas (para estudiar antes de la defensa)

1. Las billeteras tienen **efectos de red**: valen más cuanto más gente y comercios las usan.
2. Cada persona decide según cuánto la usaría (**θ**), lo que **espera** que sea la red (**nᵉ**) y lo que le cuesta adoptarla (**P**).
3. Adopta quien tiene θ ≥ 0,16/nᵉ, así que cuanto más grande se espera la red, más gente adopta.
4. Cuando la expectativa se cumple (EEA) hay **tres equilibrios**: 0, 0,2 y 0,8.
5. **0 y 0,8 son estables**, mientras que **0,2 es inestable**: es la **masa crítica**.
6. Por debajo del 20 % la red muere; por encima, crece sola hasta el 80 %.
7. Es una **Caza del Ciervo**: todos estarían mejor adoptando, pero nadie quiere ser el primero.
8. Una vez que alguien domina, aparece el **lock-in**: aunque llegue algo mejor, nadie se cambia solo.
9. La **interoperabilidad** suma las redes y baja la masa crítica; los **subsidios transitorios** bajan P y empujan la red por encima del umbral.
10. Aun en el 80 % hay **sub-adopción** (externalidad no internalizada), lo que justifica cierto subsidio a la adopción.
