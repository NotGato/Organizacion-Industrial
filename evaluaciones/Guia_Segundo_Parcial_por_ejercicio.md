# Guía para el Segundo Parcial — ejercicio por ejercicio

Organización Industrial (UADE). Armada sobre el AUTOTEST del Segundo Parcial: 5 ejercicios de 20 puntos, 120 minutos (unos 24 minutos por ejercicio).

Para cada ejercicio vas a encontrar:

1. **La idea** en dos líneas.
2. **La receta** general, que sirve aunque cambien los números.
3. **El modelo resuelto** paso a paso.
4. **La respuesta teórica** lista para escribir.
5. **Qué puede cambiar** en el parcial real.

Las resoluciones son propias, no una clave oficial del docente.

## Herramientas que se repiten en todo el parcial

| Herramienta | Fórmula | Dónde se usa |
|---|---|---|
| Cournot con n empresas iguales (P = a − Q) | q = (a − c) / (n + 1) | Ej. 3 y 5 |
| Cournot con costos distintos, 2 empresas | q₁ = (a − 2c₁ + c₂) / 3 | Ej. 3 y 5 |
| Beneficio en Cournot | π = q² | Ej. 3 y 5 |
| Precio | P = a − Q | Ej. 3 y 5 |
| Excedente del consumidor | EC = Q² / 2 | Ej. 3 y 5 |
| Bienestar | W = EC + suma de beneficios | Ej. 3 y 5 |
| "El más difícil de convencer queda con utilidad cero" | U = 0 para ese consumidor | Ej. 1, 2 y 4 |

Las fórmulas con π = q² y EC = Q² / 2 valen sólo cuando la demanda es P = a − Q (pendiente 1). Si la pendiente es otra, calculá π = (P − c)·q y EC = (a − P)·Q / 2.

---

# Ejercicio 1 — Monopolista en la ciudad lineal (Unidad 7)

## La idea

Los consumidores están repartidos en una calle. Comprar lejos les cuesta (transporte). El monopolista cobra un precio único, así que el precio lo define el consumidor **más lejano**. Abrir más tiendas acerca el producto y permite cobrar más, pero cada tienda tiene un costo fijo.

## La receta

1. **Ubicá al consumidor más lejano.** Una tienda en el centro: distancia 1/2. Dos tiendas en 1/4 y 3/4: distancia 1/4.
2. **Precio de cobertura total:** dejá a ese consumidor con utilidad cero. V − p − t·d = 0.
3. **Beneficio:** (p − c)·1 − F por cada tienda.
4. **Chequeá la cobertura parcial:** demanda Q = 2·(V − p)/t por tienda, maximizá (p − c)·Q. Si el precio óptimo queda por debajo del de cobertura total (o Q da más que el mercado), gana la cobertura total.
5. **Repetí con dos tiendas** y compará beneficios.
6. **Transporte promedio** = t × (mitad de la distancia máxima).
7. **Privado contra social:** al monopolista le importa cuánto sube el precio; a la sociedad, cuánto baja el transporte promedio. Compará cada uno contra F.

## El modelo resuelto

Datos: V = 30, t = 16 (lineal), c = 10, F = 3.

**a) Una tienda, cobertura total**

- Más lejano a 1/2: 30 − p − 16·(1/2) = 0 → **p = 22**
- Beneficio: (22 − 10)·1 − 3 = **9**

**b) ¿Cobertura parcial? ¿Una o dos tiendas?**

- Demanda parcial: compra quien está a d ≤ (30 − p)/16. Hacia los dos lados: Q = (30 − p)/8.
- Maximizo (p − 10)·(30 − p)/8: sale 40 − 2p = 0 → p = 20.
- Con p = 20, Q = 1,25 > 1. No es posible: el óptimo cae fuera del tramo parcial (que empieza en p = 22). Por encima de 22 el beneficio baja, así que **conviene p = 22 y cubrir todo**.
- Dos tiendas, más lejano a 1/4: 30 − p − 16·(1/4) = 0 → **p = 26**
- Beneficio: (26 − 10)·1 − 2·3 = **10**
- Como 10 > 9, **abre dos tiendas**.

**c) Transporte y variedad**

- Transporte promedio: una tienda 16·(1/4) = **4**; dos tiendas 16·(1/8) = **2**.
- Ganancia social de la segunda tienda: ahorro de 2 contra costo fijo de 3 → **no conviene**. Bienestar: 30 − 10 − 4 − 3 = 13 con una; 30 − 10 − 2 − 6 = 12 con dos.
- Ganancia privada: sube el precio en 4 contra costo fijo de 3 → **sí conviene**.

## Respuesta teórica

> El monopolista decide cuántas tiendas abrir según cuánto puede subir el precio, y el precio depende del consumidor marginal (el más lejano). El beneficio social depende del ahorro de transporte del consumidor promedio. Como el consumidor marginal ahorra más (4) que el promedio (2), el incentivo privado supera al social. La diferencia es una transferencia desde los consumidores inframarginales, no creación de valor. Por eso el monopolista puede ofrecer más variedad que la socialmente óptima.

## Qué puede cambiar

- **Costo de transporte cuadrático (t·d²):** mismo método, pero el más lejano paga t·(1/2)² = t/4 con una tienda y t·(1/4)² = t/16 con dos. El apunte usa este caso.
- **Que gane la cobertura parcial:** pasa cuando t es alto respecto de V − c. Ahí usás el precio que sale de maximizar.
- **Tres tiendas:** ubicadas en 1/6, 1/2 y 5/6, el más lejano está a 1/6.
- **Duopolio de Hotelling** en vez de monopolio: empresas en los extremos, P = c + t, cada una vende 1/2, beneficio t/2.

---

# Ejercicio 2 — Menú de calidades (Unidad 7)

## La idea

Hay clientes que valoran mucho la calidad (tipo alto) y otros que la valoran poco (tipo bajo), y el monopolista no sabe quién es quién. Puede vender un solo producto a todos, venderle sólo a los que pagan más, o armar dos versiones para que cada uno se elija solo. El problema de las dos versiones: la barata tienta al cliente caro.

## La receta

Calculá el beneficio de las tres estrategias en función de λ (proporción de tipo alto):

| Estrategia | Precio | Beneficio |
|---|---|---|
| **Agrupación:** calidad alta para todos | p = θ_bajo · s₂ | p − c₂ |
| **Exclusión:** calidad alta sólo al tipo alto | p = θ_alto · s₂ | λ · (p − c₂) |
| **Separación:** menú de dos calidades | p₁ = θ_bajo · s₁ ; p₂ = θ_alto · s₂ − (θ_alto − θ_bajo) · s₁ | (1 − λ)·(p₁ − c₁) + λ·(p₂ − c₂) |

De dónde salen los precios del menú:

- **Participación del tipo bajo** con igualdad: θ_bajo·s₁ − p₁ = 0. Le sacás todo el excedente.
- **Incentivos del tipo alto** con igualdad: θ_alto·s₂ − p₂ = θ_alto·s₁ − p₁. Lo dejás indiferente entre su producto y el barato.

Después:

1. Reemplazá el λ que te dan y elegí el beneficio más alto.
2. Verificá las dos restricciones que no usaste: que el alto quiera comprar y que el bajo no quiera el producto caro.
3. Para los intervalos, igualá los beneficios de a pares y despejá λ.

## El modelo resuelto

Datos: s₁ = 2, s₂ = 4, c₁ = 8, c₂ = 20, θ_bajo = 10, θ_alto = 16.

**a) Beneficios**

- Agrupación: p = 10·4 = 40 → beneficio = 40 − 20 = **20**
- Exclusión: p = 16·4 = 64 → beneficio = **44·λ**
- Separación: p₁ = 10·2 = **20**; p₂ = 64 − (16 − 10)·2 = **52**
  beneficio = (1 − λ)·(20 − 8) + λ·(52 − 20) = **12 + 20·λ**

**b) Con λ = 0,45**

- Agrupación: 20
- Exclusión: 44·0,45 = 19,8
- Separación: 12 + 9 = **21** → es la óptima, con precios 20 y 52

Verificación de las restricciones no activas:

- Participación del alto: 16·4 − 52 = 12 ≥ 0 ✓
- Incentivos del bajo: con su producto obtiene 10·2 − 20 = 0; con el caro, 10·4 − 52 = −12. No se cambia ✓

Intervalos:

- Separación contra agrupación: 12 + 20λ ≥ 20 → λ ≥ 0,4
- Separación contra exclusión: 12 + 20λ ≥ 44λ → λ ≤ 0,5

| λ | Estrategia óptima |
|---|---|
| Menor a 0,4 | Agrupación |
| Entre 0,4 y 0,5 | Separación |
| Mayor a 0,5 | Exclusión |

## Respuesta teórica

> Al pasar de un producto al menú aparecen dos efectos opuestos. **Expansión del mercado:** la versión de baja calidad permite atender al tipo bajo con un producto más barato de producir y a un precio que acepta. **Canibalización:** esa versión tienta al tipo alto, y para que no se cambie hay que bajarle el precio (de 64 a 52), cediéndole una renta de información igual a (θ_alto − θ_bajo)·s₁. Si domina la expansión, el monopolista ofrece el menú y cada tipo se autoselecciona (equilibrio de separación). Si domina la canibalización, ofrece una sola calidad: a todos si hay pocos tipos altos (agrupación), o sólo a los altos si son muchos (exclusión).

Lectura de los intervalos: con pocos tipos altos no vale la pena complicarse por ellos; con muchos, no vale la pena regalarles renta para atender a los bajos.

## Qué puede cambiar

- **Otros números:** la receta es idéntica.
- **Agrupación con calidad baja para todos:** si te lo piden, p = θ_bajo·s₁ y beneficio p − c₁.
- **Duopolio vertical** en vez de monopolio: con θ uniforme entre 0 y 1 y costo cero, p₁ = Δs/3, p₂ = 2Δs/3, la de calidad alta vende 2/3 y gana 4 veces más.

---

# Ejercicio 3 — Fusión horizontal con sinergias (Unidad 8)

## La idea

En Cournot, fusionarse no suele convenir: la fusionada achica su producción para subir el precio, pero las rivales aprovechan y producen más. Eso es la **paradoja de la fusión**. Deja de pasar si la fusión baja el costo marginal, porque entonces la fusionada quiere producir más, no menos.

## La receta

1. **Antes:** Cournot con n empresas iguales. q = (a − c)/(n + 1), P = a − n·q, π = q².
2. **Fusión sin sinergia:** queda una empresa menos, todas iguales. Compará la π de la fusionada contra **la suma** de lo que ganaban las dos antes.
3. **Fusión con sinergia:** Cournot con costos distintos. Con dos empresas: q₁ = (a − 2c₁ + c₂)/3.
4. **Rentabilidad:** π fusionada contra 2·π de antes.
5. **Consumidores:** EC = Q²/2. Lo único que les importa es si el precio subió o bajó.
6. **Bienestar:** EC + todos los beneficios.
7. **Sinergia mínima para no dañar al consumidor:** escribí el precio post-fusión en función de x, pedí que no supere el de antes y despejá.

## El modelo resuelto

Datos: P = 100 − Q, c = 40, tres empresas. Se fusionan la 1 y la 2.

**a) Antes y fusión sin sinergia**

- Antes: q = (100 − 40)/4 = **15**; Q = 45; P = **55**; π = 15² = **225** cada una.
- Después (duopolio igual): q = 60/3 = **20**; Q = 40; P = **60**; π = **400** cada una.
- Fusionada: 400 contra 225 + 225 = 450 → **pierde 50, no conviene**.
- Empresa 3: pasa de 225 a 400 → **gana sin hacer nada**.

**b) Con sinergia x = 6** (fusionada con costo 34, empresa 3 con 40)

- q fusionada = (100 − 2·34 + 40)/3 = **24**
- q₃ = (100 − 2·40 + 34)/3 = **18**
- Q = 42; P = **58**
- π fusionada = 24² = **576** > 450 → **conviene**
- π₃ = 18² = 324

| | Antes | Después |
|---|---|---|
| Precio | 55 | 58 |
| Excedente del consumidor | 45²/2 = 1.012,5 | 42²/2 = 882 |
| Beneficios totales | 675 | 900 |
| Bienestar | 1.687,5 | 1.782 |

Los consumidores pierden 130,5 y el bienestar total sube 94,5.

**c) Sinergia mínima**

P después = (100 + (40 − x) + 40)/3 = (180 − x)/3. Para que no supere 55: 180 − x ≤ 165 → **x ≥ 15**.

## Respuestas teóricas

**c) Por qué las sinergias rompen la paradoja**

> Sin sinergias, la fusionada restringe producción y las rivales la expanden, porque las cantidades son sustitutos estratégicos; la fusionada termina con una porción menor de un mercado apenas más caro. Con sinergias en costos variables baja su costo marginal, lo que la vuelve más agresiva: produce más, las rivales se retraen y gana margen por unidad. El bienestar total puede subir aunque los consumidores pierdan porque el ahorro de costos es una ganancia real de recursos (6 por unidad sobre 24 unidades = 144) que supera la pérdida por producir menos (49,5). Es el trade-off de Williamson. Para que los consumidores no se perjudiquen el precio no debe subir, lo que requiere x ≥ 15.

**d) Integración vertical y discriminación de precios**

> El fabricante quiere cobrar caro al minorista del mercado inelástico y barato al del elástico. Si no puede impedir el arbitraje, el minorista que compra barato revende al otro y los precios se igualan. Integrándose con el minorista del mercado elástico, vende ahí directamente al público a precio bajo y deja de vender el insumo barato, con lo que nadie puede revender; al resto le cobra el precio mayorista alto. El efecto sobre el bienestar es ambiguo: la discriminación baja el precio en el mercado elástico y lo sube en el inelástico. El bienestar puede mejorar si aumenta la cantidad total o se atiende un mercado que con precio uniforme quedaba afuera, y además se elimina la doble marginalización en el mercado integrado. Empeora si sólo redistribuye cantidades entre mercados sin aumentar el total.

## Qué puede cambiar

- **Más empresas:** con n empresas y costos distintos, qᵢ = (a − n·cᵢ + suma de los otros costos)/(n + 1) y P = (a + suma de todos los costos)/(n + 1).
- **Ahorro en costos fijos** en vez de marginales: el equilibrio no cambia; la fusión conviene si el ahorro F supera la pérdida (acá, F > 50).
- **Doble marginalización como ejercicio numérico** (P = A − Q, costo c):
  - Separados: precio mayorista (A + c)/2, precio final (3A + c)/4, cantidad (A − c)/4.
  - Integrados: precio (A + c)/2, cantidad (A − c)/2 (el doble).
  - Se resuelve de atrás para adelante: primero el minorista, después el fabricante.
- **Condición general de la paradoja:** fusionar k de n conviene si (n + 1)² > k·(n − k + 2)².

---

# Ejercicio 4 — Monopolista de red (Unidad 9)

## La idea

El servicio vale más cuanta más gente lo usa. Por eso la gente decide según cuántos **espera** que lo usen. Si todos esperan poco, la red no arranca; si esperan mucho, despega. Entre medio hay un umbral: la **masa crítica**.

## La receta

1. **Demanda de red.** Con U = A·θ·nᵉ − p:
   - Adopta quien tiene θ ≥ p/(A·nᵉ).
   - Fracción que adopta: n = 1 − p/(A·nᵉ).
   - Expectativas autocumplidas (nᵉ = n): **p = A·n·(1 − n)**.
2. **Precio máximo:** la curva es una campana con pico en n = 1/2. p máx = A/4.
3. **Problema del monopolista:** π = N·[p(n) − c]·n. Derivá e igualá a cero. Te queda una cuadrática con dos raíces.
4. **Segunda derivada negativa:** descarta la raíz chica (es un mínimo). Te quedás con la grande.
5. **Precio y beneficio** con ese n.
6. **Equilibrios a ese precio:** resolvé p(n) = precio. La raíz alta es el n del monopolista; la baja es la **masa crítica**. Chequeo: las dos raíces suman 1.
7. **Estabilidad:** n = 0 estable, masa crítica inestable, n alto estable.

## El modelo resuelto

Datos: U = 100·θ·nᵉ − p, N = 1.000, c = 12.

**a) Demanda y precio máximo**

- n = 1 − p/(100·n) → **p(n) = 100·n·(1 − n)**
- Máximo en n = 1/2: p = 100·(1/2)·(1/2) = **25**

**b) Monopolista**

- π = 1.000·[100n(1 − n) − 12]·n = 1.000·(100n² − 100n³ − 12n)
- Primera derivada igual a cero: 200n − 300n² − 12 = 0 → 300n² − 200n + 12 = 0
- n = (200 ± √(40.000 − 14.400)) / 600 = (200 ± 160)/600 → **0,6** y 0,067
- Segunda derivada: 200 − 600n. En 0,6 da −160 (máximo ✓). En 0,067 da +160 (mínimo ✗).
- **n = 0,6** (600 usuarios)
- **p = 100·0,6·0,4 = 24**
- **π = 1.000·(24 − 12)·0,6 = 7.200**

Equilibrios a p = 24: 100n(1 − n) = 24 → n² − n + 0,24 = 0 → n = (1 ± √0,04)/2 = (1 ± 0,2)/2

| Equilibrio | Usuarios | Estabilidad |
|---|---|---|
| n = 0 | 0 | Estable |
| n = 0,4 | 400 | **Inestable: es la masa crítica** |
| n = 0,6 | 600 | Estable |

Cómo justificar la estabilidad: en un n cualquiera, si la curva p(n) está por encima del precio la red crece, y si está por debajo se achica. Justo por encima de 0,4 la curva supera 24, así que la red crece hasta 0,6. Justo por debajo queda abajo de 24 y la red cae a 0.

**c) Eficiencia**

- Bienestar: W = N·[100·n²·(2 − n)/2 − 12·n]. Su derivada en n = 1 vale 50 − 12 = 38 > 0, así que el óptimo social es **n = 1** (todos adoptan).
- W con monopolio = 18.000; W con n = 1 = 38.000.

## Respuesta teórica

> El monopolista elige una red (n = 0,6) menor que la socialmente óptima (n = 1). Hay dos fuentes de ineficiencia. **Efecto precio:** como cualquier monopolio, cobra por encima del costo marginal (24 contra 12) y excluye a consumidores que valoran el servicio más de lo que cuesta atenderlos. **Efecto de red:** cada usuario adicional aumenta el valor del servicio para todos los demás, y ni el usuario ni el monopolista internalizan por completo esa externalidad positiva; al quedar gente afuera, la red vale menos para los que están adentro. Si las expectativas iniciales se coordinan por debajo de la masa crítica (400 usuarios), adoptan menos de los esperados, las expectativas se revisan a la baja y la red converge a cero aunque el equilibrio alto sea viable: es un problema de coordinación. El monopolista puede usar un precio de penetración (bajo o nulo al inicio) para reducir la masa crítica y superar el umbral, y subirlo a 24 una vez alcanzada; también subsidios a los primeros usuarios o compromisos creíbles de precio.

## Qué puede cambiar

- **Sin costo marginal (caso del apunte):** n = 2/3, p = (2/9)·A, masa crítica 1/3.
- **Te dan un precio y un tamaño inicial:** calculá la masa crítica a ese precio. Si el inicial está por encima, la red llega al equilibrio alto; si está por debajo, colapsa.
- **Precio de penetración:** te piden el precio que baja la masa crítica a cierto nivel n₀. Es p = A·n₀·(1 − n₀).
- **Mercados de dos lados (teórico):** importa cómo se reparte el precio entre los dos lados; se cobra menos al lado difícil de atraer.

---

# Ejercicio 5 — Innovación en Cournot (Unidad 10)

## La idea

Una empresa que baja su costo le saca mercado a la rival. Por eso cada una quiere innovar, sobre todo para no quedar atrás. Pero si innovan las dos, compiten más fuerte, el precio cae y pueden terminar peor que si ninguna lo hubiera hecho. Los que ganan seguro son los consumidores.

## La receta

Necesitás tres equilibrios de Cournot:

| Escenario | Cantidades |
|---|---|
| Ninguna innova | q = (a − c)/3 cada una |
| Sólo la 1 innova | q₁ = (a − 2c′ + c)/3 ; q₂ = (a − 2c + c′)/3 |
| Las dos innovan | q = (a − c′)/3 cada una |

En todos, π = q² y P = a − Q.

1. **¿Es drástica?** Calculá el precio de monopolio con el costo nuevo: (a + c′)/2. Si es menor que el costo viejo c, es drástica (la rival sale del mercado). Si no, no lo es.
2. **Incentivo bruto:** V = π innovando sola − π de antes. Conviene innovar si K < V.
3. **Matriz de pagos:** restale K a quien innova en cada casillero.
4. **Equilibrio de Nash:** fijate si innovar conviene haga lo que haga la otra (estrategia dominante).
5. **¿Dilema del prisionero?** Sí, si innovar es dominante **y** las dos terminan peor que sin innovar.
6. **Consumidores:** EC = Q²/2 en cada escenario.

## El modelo resuelto

Datos: P = 120 − Q, c = 30, c′ = 15, K = 500.

**a) Una sola innova**

- Antes: q = 90/3 = **30**; Q = 60; P = **60**; π = **900**
- Sólo la 1 innova:
  - q₁ = (120 − 30 + 30)/3 = **40**
  - q₂ = (120 − 60 + 15)/3 = **25**
  - Q = 65; P = **55**
  - π₁ = 40² = **1.600**; π₂ = 25² = **625**
- ¿Drástica? Precio de monopolio con costo 15 = (120 + 15)/2 = 67,5 > 30 → **no es drástica**. La rival sigue produciendo (q₂ = 25 > 0).
- V = 1.600 − 900 = **700**. Conviene innovar si **K < 700**. Con K = 500 gana 200 neto.

**b) Juego simultáneo**

- Las dos innovan: q = (120 − 15)/3 = **35**; Q = 70; P = **50**; π = **1.225**

Pagos netos (empresa 1 ; empresa 2):

| | 2 innova | 2 no innova |
|---|---|---|
| **1 innova** | 725 ; 725 | 1.100 ; 625 |
| **1 no innova** | 625 ; 1.100 | 900 ; 900 |

- Si la 2 no innova: a la 1 le conviene innovar (1.100 > 900).
- Si la 2 innova: a la 1 le conviene innovar (725 > 625).
- Innovar es **estrategia dominante**. Equilibrio de Nash: **las dos innovan**, con 725 cada una.
- Como 725 < 900, **es un dilema del prisionero**.

**c) Consumidores**

| Escenario | Precio | Excedente del consumidor |
|---|---|---|
| Ninguna innova | 60 | 1.800 |
| Una innova | 55 | 2.112,5 |
| Las dos innovan | 50 | 2.450 |

## Respuesta teórica

> Schumpeter sostiene que el poder de mercado favorece la innovación: las empresas grandes tienen fondos propios para financiar I+D, diversifican el riesgo y capturan mejor los retornos. Arrow sostiene lo contrario: quien ya tiene rentas gana menos innovando, porque la innovación reemplaza beneficios que ya tenía (efecto de reemplazo), mientras que quien enfrenta competencia tiene más para ganar. El ejercicio apoya a Arrow en los incentivos: cada empresa innova no tanto por lo que gana sino por lo que pierde si la rival innova y ella no (pasaría de 900 a 625); la rivalidad las empuja a invertir aunque juntas estarían mejor sin hacerlo. Un monopolio o un cártel no tendría esa presión. A favor de Schumpeter, la inversión de 500 sólo es financiable porque el oligopolio deja beneficios positivos; con competencia perfecta y beneficio cero no habría con qué pagarla sin una patente. La síntesis: Arrow tiene razón sobre el incentivo y Schumpeter sobre la capacidad. Los consumidores se benefician sin ambigüedad: el precio baja de 60 a 50 y su excedente sube de 1.800 a 2.450.

## Qué puede cambiar

- **K distinto:** si K > 700 nadie innova. Rehacé la matriz y fijate si sigue siendo dominante: hace falta 1.600 − K > 900 y 1.225 − K > 625, o sea K < 600 para que innovar sea dominante.
- **Innovación drástica:** si (a + c′)/2 < c, la innovadora queda sola y cobra precio de monopolio.
- **Comparación de Arrow:** monopolista V = π monopolio nueva − π monopolio vieja; competitivo con innovación no drástica V = (c − c′)·(a − c). Siempre gana el competitivo.
- **Bienestar:** W = EC + π₁ + π₂ − costos de I+D.

---

# Plan para el día del parcial

1. **Leé los cinco enunciados primero** (2 minutos) y empezá por el que mejor te sale.
2. **Hacé primero los incisos analíticos (a y b).** Suman cerca del 75% de cada ejercicio.
3. **Mostrá el planteo aunque no llegues al número:** la condición de primer orden, la utilidad igual a cero, la matriz.
4. **En los teóricos, usá tus propios números** como evidencia ("el precio sube de 55 a 58, por lo tanto...").
5. **Chequeos rápidos que salvan puntos:**
   - Ej. 1: ¿restaste un costo fijo por cada tienda?
   - Ej. 2: ¿verificaste las dos restricciones no activas?
   - Ej. 3: ¿comparaste contra la suma de las dos empresas?
   - Ej. 4: ¿elegiste la raíz grande? ¿Las dos raíces del equilibrio suman 1?
   - Ej. 5: ¿restaste K en la matriz?

# Resumen en una tabla

| Ej. | Pregunta central | Clave para resolver | Conclusión típica |
|---|---|---|---|
| 1 | ¿Cuántas tiendas abre? | El más lejano queda con utilidad cero | Puede abrir más tiendas que las socialmente óptimas |
| 2 | ¿Un producto o un menú? | p₁ agota al tipo bajo; p₂ deja indiferente al alto | Pocos altos: agrupar. Intermedio: separar. Muchos: excluir |
| 3 | ¿Conviene fusionarse? | Cournot antes y después; comparar contra la suma | Sin sinergias no; con sinergias sí, y el consumidor puede perder igual |
| 4 | ¿Qué tamaño de red elige? | p = A·n·(1 − n), raíz grande, masa crítica | Red más chica que la óptima; riesgo de no despegar |
| 5 | ¿Innovan? | Tres equilibrios de Cournot y matriz 2×2 | Las dos innovan, ganan menos, y el consumidor gana |
