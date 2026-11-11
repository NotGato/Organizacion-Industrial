# Resumen para el Segundo Parcial — Organización Industrial (UADE)

Unidades 7 a 11, explicadas fácil. Armado a partir de los "A modo de resumen" de cada unidad y del AUTOTEST del Segundo Parcial.

**Cómo usarlo:** cada unidad tiene (1) la idea en criollo, (2) las fórmulas que hay que saber, (3) el paso a paso del ejercicio típico y (4) los errores comunes. Al final está el AUTOTEST resuelto para chequear tus cuentas.

## Qué entra según el AUTOTEST (5 ejercicios de 20 puntos, 120 minutos)

| Ej. | Unidad | Tema puntual |
|---|---|---|
| 1 | U7 | Monopolio en la ciudad lineal: cuántas tiendas abrir, cobertura, variedad privada vs. social |
| 2 | U7 | Menú de dos calidades: agrupación, exclusión, separación |
| 3 | U8 | Fusión en Cournot con sinergias + pregunta teórica de integración vertical y discriminación |
| 4 | U9 | Monopolista de red con costo marginal positivo: demanda, masa crítica, estabilidad |
| 5 | U10 | Innovación en Cournot, juego de I+D, Schumpeter vs. Arrow |

La Unidad 11 no aparece en el AUTOTEST, pero la guía de esa unidad dice que el parcial cubre las unidades 7 a 11. Conviene llevar al menos los conceptos (están resumidos abajo).

---

# Unidad 7 — Diferenciación de productos

## La idea

Los productos no son idénticos, y eso le da a cada empresa un poco de poder de mercado sobre "sus" clientes.

- **Diferenciación horizontal:** es cuestión de gustos. A igual precio, la gente elige cosas distintas (Coca vs. Pepsi, el kiosco que te queda cerca). Modelos: Hotelling y Salop.
- **Diferenciación vertical:** es cuestión de calidad. A igual precio, todos elegirían el mejor (iPhone Pro vs. estándar, 600 Mbps vs. 100 Mbps). Lo que cambia es cuánto está dispuesto a pagar cada uno.

**Truco para clasificar:** preguntate "si costaran lo mismo, ¿todos comprarían el mismo?". Si sí, es vertical. Si no, es horizontal.

## Hotelling (ciudad lineal)

Una calle de largo 1 con consumidores repartidos parejo. Cada uno compra una unidad. Utilidad: U = v − p − (costo de transporte). El parámetro **t** mide cuánto le duele al consumidor alejarse de su producto ideal. Cuanto más alto es t, más "fiel" es el cliente y más poder de mercado tiene la empresa.

**Sin competencia en precios** (precios fijos): las dos empresas se van al centro (a = b = 1/2). Es el **Principio de Mínima Diferenciación**. Explica por qué los partidos políticos se parecen o por qué dos heladerías se ponen juntas.

**Con competencia en precios** (empresas en los extremos, 0 y 1):

1. Buscás al consumidor indiferente igualando el costo total de comprarle a cada una.
2. Eso te da la demanda de cada empresa: D₁ = (P₂ − P₁ + t) / 2t.
3. Maximizás beneficio y sale la función de reacción: P₁ = (P₂ + c + t) / 2.
4. Equilibrio: **P = c + t**, cada una vende **1/2**, beneficio **t/2**.

Si las empresas están a distancia ℓ entre sí (y simétricas respecto del centro): **P = c + t·ℓ**. Más lejos, precio más alto.

**Por qué con precios se rompe la mínima diferenciación:** si se ponen juntas, se matan a precios. Alejarse suaviza la competencia. Con costo de transporte cuadrático y juego en dos etapas (primero ubicación, después precio), el resultado es **máxima diferenciación** (una en 0 y otra en 1).

## Monopolio en la ciudad lineal (Ejercicio 1 del AUTOTEST)

El monopolista decide cuánto mercado cubrir.

- **Cobertura total:** pone el precio más alto que todavía acepta el consumidor más lejano (ese queda con utilidad cero).
- **Cobertura parcial:** cobra más caro y deja afuera a los de las puntas.

**Ojo con el tipo de costo de transporte, porque la fórmula cambia:**

| | Costo cuadrático (t·d²), el del apunte | Costo lineal (t·d), el del AUTOTEST |
|---|---|---|
| 1 tienda en el centro, cobertura total | p = v − t/4 | p = v − t/2 |
| 2 tiendas en 1/4 y 3/4 | p = v − t/16 | p = v − t/4 |

No memorices: usá siempre la regla "el más lejano queda con utilidad cero". Con una tienda en el centro, el más lejano está a distancia 1/2. Con dos tiendas en 1/4 y 3/4, está a distancia 1/4.

**Paso a paso del ejercicio de tiendas:**

1. Calculá el precio de cobertura total con una tienda y el beneficio (restando el costo fijo F).
2. Chequeá la cobertura parcial: armá la demanda Q = 2·(distancia que cubre) y maximizá. Si la cantidad óptima te da mayor que 1, la cobertura total es la óptima.
3. Repetí con dos tiendas (precio más alto porque el más lejano está más cerca, pero pagás 2F).
4. Compará beneficios.
5. **Variedad privada vs. social:** a la sociedad le sirve la segunda tienda sólo si el ahorro en transporte promedio supera F. Al monopolista le sirve si lo que puede subir el precio supera F. El precio lo marca el consumidor **más lejano** (marginal) y el ahorro social es el del consumidor **promedio**. Como el más lejano ahorra más que el promedio, el monopolista puede abrir más tiendas de las socialmente convenientes.

## Salop (ciudad circular)

Igual que Hotelling pero en un círculo, con n empresas y costo fijo f de entrada.

- Precio: **P = c + t/n** (más empresas, menos margen).
- Cada una vende 1/n. Beneficio: t/n² − f.
- Con libre entrada (beneficio cero): **n = √(t/f)**.
- Óptimo social: la **mitad** de eso. O sea, la libre entrada genera **exceso de variedad**.

Por qué: el que entra le "roba" clientes a los vecinos (business stealing) y no tiene en cuenta ese daño.

## Diferenciación vertical (duopolio)

Dos calidades s₁ < s₂. Consumidores con θ uniforme entre 0 y 1, utilidad U = θ·s − p, costo cero. Llamamos Δs = s₂ − s₁.

- Indiferente: θ = (p₂ − p₁) / Δs.
- Equilibrio: **p₁ = Δs/3**, **p₂ = 2Δs/3**, indiferente en θ = 1/3.
- Demandas: 1/3 para la baja, 2/3 para la alta.
- Beneficios: Δs/9 y 4Δs/9. **La de alta calidad gana 4 veces más.**
- Las dos empresas quieren que Δs sea lo más grande posible (máxima diferenciación vertical).

## Menú de calidades (Ejercicio 2 del AUTOTEST)

Un monopolista tiene dos tipos de clientes (θ bajo y θ alto) y no sabe quién es quién. Tiene tres opciones:

| Estrategia | Qué hace | Precio | Quién se queda con excedente |
|---|---|---|---|
| **Agrupación** (pooling) | Un solo producto para todos | p = θ_bajo · s | El tipo alto se queda con renta |
| **Exclusión** | Sólo le vende al tipo alto | p = θ_alto · s | Nadie; el bajo queda afuera |
| **Separación** (menú) | Dos productos, cada tipo elige el suyo | Ver abajo | El tipo alto, pero menos |

**Precios del menú** (las dos restricciones que se cumplen con igualdad):

- Participación del tipo bajo: **p₁ = θ_bajo · s₁** (le sacás todo el excedente).
- Incentivos del tipo alto: **p₂ = θ_alto · s₂ − (θ_alto − θ_bajo) · s₁**.

Ese último término es la **renta de información**: el descuento que le tenés que dar al tipo alto para que no se haga pasar por tipo bajo.

**Paso a paso:**

1. Escribí el beneficio de cada estrategia en función de λ (proporción de tipo alto).
2. Para el λ que te dan, calculá los tres y elegí el mayor.
3. Verificá las dos restricciones que no usaste (participación del alto e incentivos del bajo).
4. Para los intervalos, igualá beneficios de a pares y despejá λ.

**Intuición del resultado:** pocos clientes de tipo alto → conviene agrupar. Muchos → conviene excluir a los bajos. En el medio → menú.

**Los dos efectos del menú (pregunta teórica):**

- **Expansión del mercado:** el producto barato permite venderle a gente que antes no comprabas (o venderle mejor).
- **Canibalización:** el producto barato tienta a tus clientes caros, así que tenés que bajarles el precio.

Si gana la expansión, hacés separación. Si gana la canibalización, te quedás con un solo producto.

## Errores comunes U7

- Confundir la **posición** del indiferente con la **demanda**. Si hay N consumidores, multiplicá por N.
- Usar p = v − t/4 cuando el costo de transporte es lineal.
- No verificar si la cobertura es total o parcial antes de seguir.
- Olvidarse de restar el costo fijo por cada tienda.

---

# Unidad 8 — Relación entre empresas

## La idea

Tres tipos de fusiones: **horizontal** (entre competidores), **vertical** (entre proveedor y cliente) y **conglomerado** (negocios no relacionados). La pregunta siempre es la misma: ¿quién gana y quién pierde? Participantes, rivales, consumidores y bienestar total.

## Fusiones horizontales y la paradoja de la fusión

Fórmulas de Cournot con n empresas iguales, demanda P = a − Q y costo c:

- q = (a − c) / (n + 1)
- P = (a + n·c) / (n + 1)
- π = (a − c)² / (n + 1)² (o sea, **π = q²**)

**La paradoja (Salant, Switzer y Reynolds):** si dos empresas se fusionan pasan a ser una sola, y esa una gana menos que lo que ganaban las dos por separado. Sólo conviene si la fusión arma un monopolio (n = 2).

**Por qué pasa:** la fusionada reduce la producción para subir el precio, pero las rivales **aumentan** la suya y se quedan con el negocio. Por eso **las que no se fusionan siempre ganan** (free rider).

Condición general para que convenga fusionar k de n empresas: **(n + 1)² > k · (n − k + 2)²**. En la práctica se necesita cerca del 80% del mercado.

## Qué rompe la paradoja

1. **Ahorro en costos fijos:** si la fusión ahorra F mayor que la pérdida, conviene. F mínimo = 2·π(n) − π(n − 1).
2. **Sinergias en costo marginal** (Ejercicio 3 del AUTOTEST): la fusionada pasa a tener costo más bajo, produce más y recupera mercado.
3. **Productos diferenciados con competencia en precios (Bertrand):** la fusión siempre conviene porque los precios son complementos estratégicos; cuando la fusionada sube el precio, las rivales también lo suben.

**Cournot asimétrico (para sinergias)**, con la empresa i de costo cᵢ y n empresas en total:

- qᵢ = (a − n·cᵢ + suma de los costos de las demás) / (n + 1)
- P = (a + suma de todos los costos) / (n + 1)
- Sigue valiendo πᵢ = qᵢ²

**Paso a paso del ejercicio de fusión con sinergias:**

1. Cournot antes (n empresas iguales): q, Q, P, π.
2. Fusión sin sinergia (n − 1 empresas iguales): mostrás que π nueva < 2·π vieja, y que la rival gana.
3. Fusión con sinergia: Cournot asimétrico. Comparás π de la fusionada contra 2·π vieja.
4. Excedente del consumidor = Q² / 2 (con demanda P = a − Q). Bienestar = EC + suma de beneficios.
5. Los consumidores no pierden sólo si el **precio no sube**. Planteás P nuevo ≤ P viejo y despejás la sinergia mínima.

**Trade-off de Williamson:** una fusión que baja costos pero sube precios se evalúa comparando el ahorro de costos (rectángulo) contra la pérdida por el mayor precio (triángulo). El bienestar total puede subir aunque los consumidores pierdan, porque el ahorro de costos es una ganancia real de recursos. Las agencias exigen que las eficiencias sean **específicas de la fusión** y **verificables**.

## Fusiones verticales: doble marginalización

Un fabricante monopolista le vende a un minorista monopolista. **Cada uno le pone su propio margen**, y el precio final termina más alto que con un solo monopolio. Demanda P = A − B·Q, costo del fabricante c:

| | Separados | Integrados |
|---|---|---|
| Precio mayorista | r = (A + c) / 2 | No hay |
| Precio final | (3A + c) / 4 | (A + c) / 2 |
| Cantidad | (A − c) / 4B | (A − c) / 2B (el doble) |
| Beneficio conjunto | 3(A − c)² / 16B | (A − c)² / 4B |

Se resuelve **de atrás para adelante**: primero el minorista elige dado r, después el fabricante elige r.

**Integrarse le conviene a todos:** baja el precio, sube la cantidad y sube el beneficio conjunto. La pérdida de eficiencia separados es 2,25 veces la de integrados (no el doble).

**Alternativas sin fusionarse:**

- **Tarifa en dos partes:** el fabricante vende al costo (r = c) y cobra un cargo fijo igual al beneficio integrado.
- **Precio máximo de reventa (RPM techo):** el fabricante le prohíbe al minorista cobrar de más.
- Reparto de beneficios o de ingresos.

**Foreclosure (cierre de mercado):** el lado malo de la integración. La empresa integrada le niega o le encarece el insumo a los rivales del minorista para sacarlos del mercado. **No lo confundas con doble marginalización**: son cosas distintas.

## Integración vertical y discriminación de precios (inciso teórico del AUTOTEST)

Un fabricante le vende a minoristas con demandas de distinta elasticidad. Quiere cobrarle caro al del mercado inelástico y barato al del elástico (discriminación de tercer grado).

- **El problema:** si no puede impedir el arbitraje, el minorista que compra barato le revende al otro y la discriminación se cae.
- **La solución:** integrarse con el minorista del **mercado elástico** (el del precio bajo). Así le vende ahí directamente al público a precio bajo, y al resto le cobra el precio alto sin que nadie pueda revender.
- **Por qué el bienestar es ambiguo:** la discriminación le sube el precio a unos y se lo baja a otros. Si permite atender un mercado que antes quedaba afuera o aumenta la cantidad total, el bienestar puede subir. Si sólo redistribuye y la cantidad no crece, baja. Además la integración elimina la doble marginalización en ese mercado (bueno), pero puede perjudicar a los minoristas no integrados (malo).

El apunte también muestra el caso sin arbitraje: en el mercado inelástico el minorista agrega un margen excesivo, y el fabricante lo corrige con un **precio máximo de reventa**.

## Errores comunes U8

- Comparar la π de la fusionada contra la π de **una** empresa. Hay que compararla contra la suma de las que se fusionaron.
- Decir que la integración reduce la pérdida de eficiencia "a la mitad". El ratio es 4/9.
- Confundir foreclosure con doble marginalización.

---

# Unidad 9 — Economías de red

## La idea

Un bien tiene **efectos de red** cuando vale más cuanta más gente lo usa. WhatsApp no sirve si tus contactos no lo tienen.

- **Efecto directo:** más usuarios del mismo tipo (teléfono, WhatsApp).
- **Efecto indirecto:** más usuarios del otro lado de una plataforma (compradores y vendedores en MercadoLibre, pasajeros y choferes en Uber).

## La demanda de red

Cada usuario tiene un tipo θ (uniforme entre 0 y 1). Utilidad: **U = θ · nᵉ − p**, donde nᵉ es la fracción de gente que **espera** que adopte.

Derivación en tres pasos (es la pregunta más frecuente):

1. Adopta el que tiene θ ≥ p / nᵉ.
2. La fracción que adopta es 1 − p / nᵉ.
3. **Expectativas autocumplidas** (lo que la gente espera es lo que pasa, nᵉ = n): n = 1 − p/n, y despejando, **p = n · (1 − n)**.

Es una **campana**: arranca en 0, llega al máximo en n = 1/2 con p = 1/4, y vuelve a 0 en n = 1.

- Tramo que sube: al sumarse gente la red vale más, así que la disposición a pagar crece.
- Tramo que baja: los que faltan sumar son los que menos lo valoran.

Si la utilidad viene multiplicada por un número (por ejemplo U = 100·θ·nᵉ − p), todo se multiplica: p = 100·n·(1 − n), precio máximo 25.

## Tres equilibrios y masa crítica

Para un precio entre 0 y el máximo, hay tres equilibrios:

| Equilibrio | Qué es | ¿Estable? |
|---|---|---|
| n = 0 | Nadie adopta | Sí |
| n bajo | **Masa crítica** | **No** |
| n alto | Red exitosa | Sí |

Se sacan resolviendo n² − n + p = 0 (con la versión normalizada). **Chequeos rápidos:** n bajo + n alto = 1, y n bajo × n alto = p.

**La masa crítica es el punto de quiebre.** Si la red arranca por encima, crece sola hasta el equilibrio alto. Si arranca por debajo, se desinfla hasta cero.

**Cómo probar estabilidad:** parate en un n cualquiera y compará la curva con el precio.

- Si la curva p(n) está **por encima** del precio: la red crece.
- Si está **por debajo**: la red se achica.

En el equilibrio bajo estás en el tramo que sube, entonces un empujoncito para arriba te aleja más: inestable. En el alto estás en el tramo que baja, y cualquier desvío se corrige: estable.

**Problema del huevo y la gallina:** nadie quiere ser el primero. Si todos esperan poco, se cumple y la red no arranca.

**Estrategias para pasar la masa crítica:** precio de penetración (gratis o muy barato al principio), subsidiar al lado difícil de atraer, compromisos de precio futuro, compatibilidad con lo que ya existe, beneficios para los primeros usuarios.

## El monopolista de red (Ejercicio 4 del AUTOTEST)

**Sin costo (caso del apunte):** maximiza n · p(n) = n²·(1 − n). Sale **n = 2/3, p = 2/9**, beneficio 4/27. La masa crítica a ese precio es 1/3.

**Con costo marginal c (caso del AUTOTEST):**

1. Beneficio: π = N · [p(n) − c] · n.
2. Derivás e igualás a cero. Queda una cuadrática con **dos raíces**.
3. Usás la condición de segundo orden para quedarte con la **raíz grande** (la chica es un mínimo).
4. Con ese n calculás el precio y el beneficio.
5. Con ese precio resolvés p(n) = precio. Te da dos valores: el alto es el que eligió el monopolista y el bajo es la masa crítica.

## Eficiencia

- **Bienestar** (versión normalizada, costo cero): W = n² · (2 − n) / 2. El óptimo social es **n = 1** (que todos adopten).
- El monopolio pierde 11/54 de bienestar, un 40,7% del máximo.

**Las dos fuentes de ineficiencia:**

1. **Efecto precio:** como cualquier monopolio, cobra por encima del costo y deja gente afuera.
2. **Efecto de red:** al dejar gente afuera, la red es más chica y vale menos **para los que sí están adentro**. Cada usuario nuevo beneficia a los demás y nadie se lo paga (externalidad positiva), por eso hay sub-adopción.

**Lock-in:** una vez que todos están en una red, cambiar sale caro aunque exista algo mejor (teclado QWERTY, VHS contra Beta). Las empresas prefieren la incompatibilidad; el regulador puede exigir interoperabilidad.

## Mercados de dos lados

Una plataforma atiende a dos grupos que se necesitan mutuamente. Lo importante no es sólo cuánto cobra en total sino **cómo lo reparte**. Regla de Rochet y Tirole: cobrarle menos (o subsidiar) al lado difícil de atraer y más al otro. Ejemplo: las tarjetas le dan beneficios al titular y le cobran comisión al comercio.

## Errores comunes U9

- Quedarse con la raíz chica en el problema del monopolista.
- Llamar "equilibrio" sin más a la masa crítica: es un equilibrio, pero inestable.
- Olvidarse de multiplicar por N al pasar de fracción a cantidad de usuarios o a beneficio.

---

# Unidad 10 — Innovación

## La idea

¿Quién innova más, el monopolio o la competencia? Hay dos respuestas enfrentadas y las dos hay que saberlas.

**Tipos de innovación:**

- **De proceso:** mismo producto, menor costo.
- **De producto:** un bien nuevo.
- **Mayor (drástica):** el costo baja tanto que el precio de monopolio del innovador queda por debajo del costo de los rivales, y los saca del mercado. Condición: (a + c′) / 2 < c.
- **Menor (no drástica):** los rivales siguen compitiendo.

**Patentes:** el conocimiento se copia gratis, así que sin protección nadie invertiría. La patente da un monopolio temporal. Beneficio: incentivo a innovar. Costo: pérdida de eficiencia mientras dura.

## Schumpeter vs. Arrow

| | Dice que | Argumento |
|---|---|---|
| **Schumpeter** | El poder de mercado favorece la innovación | Las empresas grandes tienen plata propia para financiar I+D, diversifican riesgo, aprovechan economías de escala y capturan mejor los retornos |
| **Arrow** | La competencia favorece la innovación | **Efecto de reemplazo**: el monopolista ya gana plata, innovar sólo reemplaza sus propias rentas. El competitivo parte de cero |

Schumpeter tiene dos ideas distintas: **destrucción creativa** (las innovaciones tiran abajo a los monopolios viejos y crean nuevos) y que **las empresas grandes innovan más**.

**Cómo cerrarlo en el examen:** Arrow tiene razón en los **incentivos**, Schumpeter puede tener razón en la **capacidad** (recursos). No hay una única respuesta correcta.

**Fórmulas de Arrow** (demanda P = a − Q, el costo baja en ε):

- Monopolista: V = π de monopolio nueva − π de monopolio vieja.
- Competitivo con innovación menor: V = ε · (a − c). Cobra apenas por debajo del costo viejo y se queda con todo el mercado.
- Competitivo con innovación mayor: V = π de monopolio nueva.
- Siempre el competitivo tiene más incentivo.

## Innovación en Cournot (Ejercicio 5 del AUTOTEST)

Duopolio, demanda P = a − Q. **Planteá siempre las condiciones de primer orden** (el docente pide derivar, no memorizar):

- Empresa 1: a − 2q₁ − q₂ = c₁
- Empresa 2: a − 2q₂ − q₁ = c₂

Solución: **q₁ = (a − 2c₁ + c₂) / 3**, **q₂ = (a − 2c₂ + c₁) / 3**, y **πᵢ = qᵢ²**.

**Paso a paso:**

1. Cournot antes (las dos con costo c).
2. Cournot después con una sola innovando (asimétrico).
3. Chequeá si es drástica: precio de monopolio con el costo nuevo contra el costo viejo.
4. Incentivo bruto: V = π después − π antes. Conviene innovar si K < V.
5. Efecto en consumidores: EC = Q² / 2. Si baja el precio, ganan.

**Qué pasa:** la que innova produce más y gana más; la rival produce menos y pierde; el precio baja y los consumidores ganan.

**El juego de I+D:** las dos deciden a la vez si invertir. Necesitás tres escenarios: ninguna innova, una sola innova, las dos innovan. Armás la matriz 2×2 restando K a quien invierte.

Es un **dilema del prisionero** si se cumplen las dos cosas:

- Innovar es estrategia dominante (conviene sin importar lo que haga la otra).
- Las dos terminan peor que si ninguna hubiera innovado.

Las empresas quedan atrapadas, pero **los consumidores ganan** porque el precio baja. Esto apoya a Arrow: la rivalidad empuja a innovar aunque a las empresas no les convenga en conjunto.

## Nivel óptimo de I+D y carreras por patentes

- Si la empresa elige cuánto bajar el costo (x) con costo γ·x², el monopolista elige x = (a − c) / (4γ − 1) y el óptimo social es 3(a − c) / (8γ − 3), que es **mayor**. El monopolista **subinvierte** porque no cuenta lo que ganan los consumidores.
- **Carrera por patentes:** varias empresas corren por un premio V que se lleva una sola. Resultado: **sobreinversión** y esfuerzos duplicados. Con libre entrada se gasta V en total (se disipa toda la renta). Con n empresas fijas se gasta (n − 1)/n de V.

Parece contradictorio pero no lo es: un monopolista solo invierte de menos, y muchas empresas corriendo por lo mismo invierten de más.

## Errores comunes U10

- No clasificar la innovación (mayor o menor) antes de calcular.
- Olvidarse de restar K en la matriz.
- Comparar el beneficio de innovar contra cero en vez de contra el beneficio de antes.

---

# Unidad 11 — Aplicaciones empíricas

## La idea

Cómo se miden con datos los modelos del curso. El problema central es la **endogeneidad**: la variable que usás para explicar está "contaminada" porque se determina junto con lo que querés explicar. Ejemplo clásico: precio y cantidad se determinan a la vez, entonces una regresión simple no te da la curva de demanda.

**Regla práctica:** si a la derecha de la ecuación aparece precio, concentración o publicidad, sospechá endogeneidad. Decí de dónde viene el sesgo, hacia dónde va y cómo se arregla.

## Los métodos, uno por uno

| Método | Para qué sirve | Supuesto clave |
|---|---|---|
| **MCO** | Punto de partida. Estima el efecto promedio | Que X no esté correlacionada con el error |
| **Variables instrumentales (2SLS)** | Arreglar endogeneidad usando una variable "de afuera" | Instrumento **relevante** (mueve a X; F > 10 en la primera etapa) y **exógeno** (afecta a Y sólo a través de X) |
| **Panel con efectos fijos** | Eliminar características fijas no observadas de cada empresa | Que lo no observado sea constante en el tiempo |
| **Diferencias en diferencias (DiD)** | Evaluar una política comparando tratados y control, antes y después | **Tendencias paralelas** |
| **Logit / Berry (1994)** | Estimar demanda de productos diferenciados | Transformar cuotas de mercado en una ecuación lineal |
| **BLP (1995)** | Lo mismo con gustos distintos entre consumidores | Coeficientes aleatorios |
| **UPP** | Ver si una fusión presiona los precios al alza | Tasa de desvío entre productos |
| **Regresión por cuantiles** | Ver si el efecto cambia entre los que consumen poco y mucho | No asume una distribución del error |
| **Experimento de campo** | Asignar al azar y medir. Es el estándar de oro | Problema: cuesta generalizar |
| **Modelo estructural** | Estimar costos y preferencias para simular escenarios que no pasaron | Que el modelo económico sea el correcto |

## Fórmulas y cuentas que pueden pedir

- **Pendiente por MCO:** β = Σ(x·y) / Σ(x²), con x e y medidos como desvíos respecto de su promedio.
- **Sesgo de MCO:** lo estimado = lo verdadero + Cov(X, error) / Var(X). En demanda, el sesgo es positivo (la pendiente sale menos negativa, o hasta positiva).
- **2SLS en dos pasos:** primero predecís el precio con el instrumento; después usás ese precio predicho en la ecuación de demanda.
- **Efectos fijos:** a cada dato le restás el promedio de su propia empresa y corrés MCO con eso. El test de Hausman decide entre efectos fijos y aleatorios.
- **DiD:** (cambio en el grupo tratado) − (cambio en el grupo control). Ejemplo del apunte: (18 − 25) − (23 − 24) = −6 puntos.
- **Berry:** δ = ln(cuota del producto) − ln(cuota del bien exterior). Después se estima δ contra precio y características, instrumentando el precio.
- **Problema del logit (IIA):** si sacás un producto, sus clientes se reparten en proporción a las cuotas sin importar qué tan parecidos son los productos. BLP lo atenúa.
- **UPP** del producto A = (tasa de desvío de A hacia B) × (margen de B) − (ahorro de costos de A). Si da positivo, la fusión empuja el precio de A para arriba. En logit, la tasa de desvío es cuota de B / (1 − cuota de A).
- **Modelo estructural:** se "da vuelta" la condición de equilibrio para recuperar el costo que no se observa (en el ejemplo, c = P − Q/2) y con eso se simula, por ejemplo, un precio máximo.

## La lógica del ejercicio integrador

El efecto de la publicidad sobre las ventas va bajando a medida que se limpia el problema: 1,8 con MCO → 1,2 con efectos fijos → 0,9 con instrumento → 0,7 con DiD. Cada paso saca una fuente distinta de sesgo. Que dos métodos distintos den parecido da confianza en el resultado.

---

# AUTOTEST resuelto (para chequear tus cuentas)

## Ejercicio 1 — Tiendas en la ciudad lineal (V = 30, t = 16 lineal, c = 10, F = 3)

- **a)** Una tienda en el centro: el más lejano está a 1/2. p = 30 − 16·(1/2) = **22**. Beneficio = (22 − 10)·1 − 3 = **9**.
- **b)** Cobertura parcial: Q = 2·(30 − p)/16. Maximizando sale p = 20 y Q = 1,25, que es mayor que 1, así que el mercado ya está todo cubierto y conviene el precio 22. Con dos tiendas: el más lejano está a 1/4. p = 30 − 16·(1/4) = **26**. Beneficio = 16 − 6 = **10**. Como 10 > 9, **abre dos**.
- **c)** Transporte promedio: con una tienda 16·(1/4) = 4; con dos 16·(1/8) = 2. Ahorro social = 2, menor que F = 3: **socialmente no conviene** la segunda. Ganancia privada = suba de precio de 4, mayor que 3: **al monopolista sí**. Hay exceso de variedad.

## Ejercicio 2 — Menú de calidades (s = 2 y 4, c = 8 y 20, θ = 10 y 16)

- **a)** Agrupación: p = 10·4 = 40, beneficio = **20**. Exclusión: p = 64, beneficio = **44·λ**. Separación: p₁ = 20, p₂ = 64 − 6·2 = 52, beneficio = (1 − λ)·12 + λ·32 = **12 + 20·λ**.
- **b)** Con λ = 0,45: agrupación 20; exclusión 19,8; separación **21** → gana la separación con precios 20 y 52. Verificación: el alto obtiene 64 − 52 = 12 ≥ 0; el bajo obtiene 0 con su producto y 40 − 52 = −12 con el otro, así que no se cambia. Intervalos: **agrupación si λ < 0,4; separación si 0,4 ≤ λ ≤ 0,5; exclusión si λ > 0,5**.

## Ejercicio 3 — Fusión con sinergias (P = 100 − Q, c = 40, tres empresas)

- **a)** Antes: q = 15, Q = 45, P = 55, π = 225 cada una. Fusión sin sinergia (duopolio): q = 20, P = 60, π = 400. La fusionada gana 400 contra 450 que sumaban antes: **no conviene**. La empresa 3 pasa de 225 a 400: **gana**.
- **b)** Con x = 6 (costo 34 contra 40): q fusionada = 24, q₃ = 18, Q = 42, P = 58. π fusionada = 576 > 450: **conviene**. π₃ = 324. Excedente del consumidor: 1.012,5 → 882 (**baja**). Bienestar: 1.687,5 → 1.782 (**sube**).
- **c)** P después = (180 − x) / 3. Para que no supere 55 hace falta **x ≥ 15**.

## Ejercicio 4 — Monopolista de red (U = 100·θ·nᵉ − p, N = 1.000, c = 12)

- **a)** p(n) = 100·n·(1 − n). Precio máximo = **25** en n = 1/2.
- **b)** Condición de primer orden: 200n − 300n² − 12 = 0. Raíces: (200 ± 160) / 600 → 0,6 y 0,067. La de segundo orden (200 − 600n < 0) elige **n = 0,6**. Precio = **24**. Beneficio = 1.000·(24 − 12)·0,6 = **7.200**. A precio 24: n² − n + 0,24 = 0 → 0,4 y 0,6. Equilibrios: 0 (estable), **0,4 = masa crítica, 400 usuarios (inestable)**, 0,6 (estable).
- **c)** El óptimo social es n = 1 (el beneficio social de sumar al último usuario sigue siendo mayor que el costo de 12). El monopolio se queda en 0,6. Si las expectativas arrancan por debajo de 400 usuarios, la red se cae a cero; la salida es un precio de penetración.

## Ejercicio 5 — Innovación en Cournot (P = 120 − Q, c = 30 → 15, K = 500)

- **a)** Antes: q = 30, P = 60, π = 900. Sólo la 1 innova: q₁ = 40, q₂ = 25, P = 55, π₁ = 1.600, π₂ = 625. Precio de monopolio con costo 15 = 67,5, mayor que 30: **no es drástica**. V = 1.600 − 900 = **700**. Conviene si K < 700.
- **b)** Las dos innovan: q = 35, P = 50, π = 1.225. Matriz de pagos netos:

| | 2 innova | 2 no innova |
|---|---|---|
| **1 innova** | 725 ; 725 | 1.100 ; 625 |
| **1 no innova** | 625 ; 1.100 | 900 ; 900 |

Innovar es dominante (1.100 > 900 y 725 > 625). Equilibrio: **las dos innovan** y ganan 725, menos que los 900 de no innovar: **es un dilema del prisionero**.

- **c)** Consumidores: el precio baja de 60 a 50 y el excedente sube de 1.800 a 2.450. La competencia las fuerza a innovar (punto para Arrow), aunque la innovación sólo es financiable porque el oligopolio deja margen (punto para Schumpeter).

---

# Machete de último momento

| Unidad | Lo que no te podés olvidar |
|---|---|
| U7 | Hotelling: P = c + t. Salop: n = √(t/f) y hay exceso de variedad. Vertical: precios Δs/3 y 2Δs/3. Menú: p₁ = θ_bajo·s₁ y p₂ = θ_alto·s₂ − (θ_alto − θ_bajo)·s₁ |
| U8 | Cournot: q = (a − c)/(n + 1) y π = q². Paradoja: fusionar no conviene salvo monopolio; las rivales ganan. Doble marginalización: integrados producen el doble |
| U9 | p = n·(1 − n). Tres equilibrios; el del medio es la masa crítica y es inestable. Monopolio sin costo: n = 2/3, p = 2/9. Óptimo social: n = 1 |
| U10 | Arrow: el competitivo tiene más incentivo (efecto de reemplazo). Cournot asimétrico: q₁ = (a − 2c₁ + c₂)/3. Dilema del prisionero en I+D |
| U11 | Endogeneidad → instrumento relevante y exógeno. DiD necesita tendencias paralelas. Berry: δ = ln s − ln s₀. UPP > 0 es mala señal para una fusión |
