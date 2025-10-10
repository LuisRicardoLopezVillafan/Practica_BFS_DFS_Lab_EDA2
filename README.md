**Nota 1.** A continuacion, se dan los problemas de la practica de DFS y BFS. Para cada algoritmo, se incluye un esqueleto sugerido para las implementaciones en Python con pistas conceptuales y referencias a la documentacion del lenguaje. Tambien se extiende el tiempo de realizacion de esta primera practica de Python hasta el miercoles de la siguiente semana.

**Nota 2.** El lenguaje sugerido para esta practica es Python. Sin embargo, pueden usar el lenguaje de su preferencia que sea adecuado para POO (como Java o C++). Esto es por el uso de atributos de los grafos en los algoritmos.

**Nota 3.** El mapa de Rumania para el ejercicio de BFS ya se encuentra en el Classroom en la seccion de Practicas.

# Parte I. Búsqueda en Profundidad (DFS)

## Problema de las N Reinas

El **problema de las N reinas** consiste en colocar `N` reinas en un tablero de ajedrez de `N × N` de manera que **ninguna reina pueda atacar a otra**.  
Es decir, no puede haber dos reinas en la misma fila, columna o diagonal.

El uso de **DFS** para resolver el problema de las `N` reinas consiste en colocar una reina en una posición y luego explorar posiciones consecutivas que sean válidas según la definición del problema.

---

### Planteamiento de los ejercicios

En esta práctica se resolverán **tres ejercicios**, dos relacionados con el algoritmo DFS y uno relacionado con el algoritmo BFS:

---

#### Ejercicio 1

Definir una función en **Python** que reciba como entrada un entero `N` (`1 ≤ N ≤ 8`) correspondiente al tamaño del tablero.

La salida de la función es un **arreglo `P`** de tamaño `N` con enteros menores que `N` indicando una posible posición de las `N` reinas que soluciona el problema.

Si `i` es un valor menor a `N`, entonces el valor `P[i]` indica en qué **renglón de la i-ésima columna** del tablero colocar una reina para obtener una solución.

**Referencia:** además del pseudocódigo visto en clase, pueden revisar el siguiente enlace:  
[Visualización del problema de las N reinas (USFCA)](https://www.cs.usfca.edu/~galles/visualization/RecQueens.html)

---

##### Ejemplo

Supongamos que la función se llama `nreinas`, y la entrada de la función es `N = 4`.  
Una posible salida es:

`P = [1, 3, 0, 2]`

Esto corresponde al siguiente tablero:

|   |   | Q |   |
|---|---|---|---|
| Q |   |   |   |
|   |   |   | Q |
|   | Q |   |   |

Por lo tanto, el resultado de `nreinas(4)` es:

`[1, 3, 0, 2]`

---

#### Ejercicio 2

Definir una función en **Python** que reciba **dos entradas**:

1. Un entero `N` (`1 ≤ N ≤ 8`) correspondiente al tamaño del tablero.  
2. Un arreglo `A` de enteros tal que `0 ≤ len(A) ≤ N`.  
   (Es decir, puede ser un arreglo vacío, y puede tener a lo más `N` enteros que indican **posiciones no disponibles**.)

La salida de la función es un **arreglo `P`** de tamaño `N` que indica posiciones posibles para las `N` reinas que solucionan el problema.

---

##### Ejemplo

Supongamos que nuestra función se llama `nreinas2`, y que recibe como entradas:

`N = 4`  
`A = [1, 3, 0, 2]`

Una posible salida es:

`[2, 0, 3, 1]`

correspondiente al siguiente tablero:

|   | Q | X |   |
|---|---|---|---|
| X |   |   | Q |
| Q |   |   | X |
|   | X | Q |   |

> Las **X** indican posiciones no disponibles.

Por lo tanto, el resultado de `nreinas2(4, A)` es:

`[2, 0, 3, 1]`

---

### Punto Extra

Para cada uno de los dos problemas de las `N` reinas, si además del resultado que pide cada inciso, la función devuelve **todas las soluciones posibles**, entonces se obtiene **un punto extra** en la **tarea** correspondiente a estos temas.

---

## Problema del intervalo

Definir una función que reciba **dos datos de entrada**:

- Un arreglo `A` de enteros no negativos de tamaño `N > 0`.
- Un número racional no negativo `q`.

La salida producida por la función es **una lista con las dos posiciones** en el arreglo `A`, señalando el intervalo más pequeño que contiene al número `q`.

Para la definición de la función, dividir de manera **recursiva** el arreglo de entrada hasta obtener subarreglos con un solo dato (como en Merge Sort).

---

### Ejemplo

Supongamos que el número de entrada es:

`q = 8.13`  
`A = [4, 0, 7, 11, 9, 12, 56, 3]`

Para encontrar el intervalo más pequeño, la función divide el arreglo buscando:

- el entero que se aproxima **por abajo** de `q`, y  
- el que se aproxima **por arriba** de `q`.

El proceso interno puede visualizarse así:


```
[4, 0, 7, 11, 9, 12, 56, 3]
[4, 0, 7, 11]   [9, 12, 56, 3]
[4, 0] [7, 11]   [9, 12] [56, 3]
[4] [0] [7] [11]   [9] [12] [56] [3]
```



La función identifica que **7** y **9** son los enteros más cercanos a `q` por debajo y por arriba, respectivamente.

Por lo tanto, el resultado de la función con esas entradas es:

`[2, 4]`

donde los valores son las posiciones que ocupan el **7** y el **9** en el arreglo original.


---

# Parte II. Búsqueda en Anchura (BFS)

## Descripción del problema

Considera el siguiente **mapa de las ciudades de Rumania** (ver figura).  
Los valores que aparecen en las aristas corresponden al **tiempo promedio en minutos** que toma llegar desde un punto a otro con el que tenga conexión directa.  

Estos tiempos varían a lo largo del día, de acuerdo con el horario y las condiciones de tráfico.  
De manera específica, los tiempos de traslado se comportan así:

-  **De 00:00 a 5:59** → El tiempo de traslado es el que aparece en el mapa.  
-  **De 6:00 a 15:59** → El tiempo de traslado es **el doble** del que aparece en el mapa.  
  - Ejemplo: de **Bucharest a Giurgiu**, el tiempo de traslado es **180 minutos**.  
-  **De 16:00 a 23:59** → El tiempo de traslado entre cada dos puntos es **1.5 veces** el que aparece en el mapa.  
  - Ejemplo: de **Bucharest a Giurgiu**, el tiempo de traslado es **135 minutos**.

---

### Figura

**Figura 1.** Mapa de las ciudades de Rumania.  
*(Los valores en las aristas indican el tiempo promedio de traslado en minutos.)*

![Mapa de Rumania](https://image1.slideserve.com/2592244/road-map-of-romania-l.jpg)

---

## Ejercicio

El objetivo de este ejercicio es **implementar un sistema** que pueda responder **cuál es el tiempo total de traslado** entre dos ciudades dadas, **considerando la hora de inicio del viaje**.

El cálculo debe **respetar los horarios** en los que cambian los tiempos estimados de traslado, de modo que si el viaje cruza un intervalo horario distinto, se debe ajustar el tiempo restante en consecuencia.

---

### Ejemplos

- **Ejemplo 1.**  
  Si el viaje es de **Giurgiu a Urziceni** y comienza a las **5:00 am**, entonces:
  - La primera parte del viaje (Giurgiu → Bucharest) dura **90 minutos**, porque inicia antes de las 6:00 am.  
  - Sin embargo, al llegar a Bucharest ya son **6:30 am**, y la segunda parte (Bucharest → Urziceni) ocurre después de las 6:00 am.  
    Por lo tanto, su duración se calcula con el **doble del tiempo** que aparece en el mapa, es decir **170 minutos**.

- **Ejemplo 2.**  
  Si el mismo viaje comienza a las **4:00 am**, ambos trayectos se calculan con el tiempo **original** del mapa, porque la llegada a Bucharest ocurre **antes de las 6:00 am**.

---

## Requisitos de implementación

- Utiliza el **algoritmo de Búsqueda en Anchura (BFS)** para recorrer el grafo de ciudades y determinar el camino más corto en número de aristas (no necesariamente en tiempo).
- Una vez encontrado el camino, **calcula el tiempo total del recorrido** ajustando los tiempos de cada tramo según el horario en que inicia.
- Se recomienda representar el grafo mediante **listas o matrices de adyacencia** en Python.
- Considera representar el **horario de inicio** en formato de 24 horas (por ejemplo, `5.0` para 5:00 am o `13.5` para 13:30 pm).

---

### Sugerencias

- Puedes comenzar implementando una función `bfs_path(graph, start, goal)` que devuelva el camino más corto (lista de ciudades).
- Luego, define una función `travel_time(path, start_hour)` que calcule el tiempo total del recorrido considerando los horarios y ajustes de tráfico.
- Si lo deseas, imprime el recorrido y el tiempo acumulado entre cada ciudad intermedia.

---
# Esqueletos de sugerencia para los programas en Python de los ejercicios
## Ejercicios DFS
```
"""
(El siguiente script es un esqueleto que se sugiere para sus implementaciones, pueden hacer todas las modificaciones que consideren necesarias. Se incluyen referencias a la documentacion de Python.)
Práctica DFS — Problema de las N reinas
-----------------------
Completa los TODO para implementar búsquedas en profundidad (DFS) con retroceso (backtracking).

Convenciones del problema:
- Representamos una solución como una lista P de tamaño N.
  P[c] = r significa: en la columna c colocamos una reina en el renglón r.
- Las columnas se recorren de 0 a N-1.
- Para el ejercicio 2 (con obstáculos), A es una lista de longitud 0..N.
  Interpretación: si A[j] existe, el renglón A[j] en la columna j está BLOQUEADO.
  (Ejemplo: A = [1,3,0,2] bloquea (col=0,row=1), (1,3), (2,0), (3,2).)
"""

from typing import List, Optional


# --------------------------------------------------------
# Función auxiliar para verificar conflictos entre reinas
# --------------------------------------------------------
def en_conflicto(parcial: List[int], fila: int, col: int) -> bool:
    """
    Regresa True si colocar una reina en (fila, col) entra en conflicto
    con alguna reina ya colocada en el arreglo parcial (columnas 0..col-1).

    Conflictos:
      - misma fila
      - misma diagonal (|Δfila| == |Δcol|)

    TODO: implementar las condiciones de conflicto.

     Referencia: https://docs.python.org/3/tutorial/datastructures.html
    """
    for c_prev, r_prev in enumerate(parcial):
        # misma fila
        # misma diagonal
        pass  # TODO: reemplazar por return True si hay conflicto
    return False


# --------------------------------------------------------
# Ejercicio 1 — DFS para encontrar UNA solución
# --------------------------------------------------------
def nreinas(N: int) -> Optional[List[int]]:
    """
    Regresa una solución válida P (lista de tamaño N) o None si no existe.

    Estrategia:
      - DFS por columnas: intenta colocar en cada columna una fila válida.
      - Usa backtracking: si una elección no lleva a solución, deshaz y prueba otra.

     Concepto: El backtracking es una búsqueda en profundidad (DFS)
    que explora todas las combinaciones posibles, retrocediendo cuando
    una elección lleva a un callejón sin salida.
    """
    parcial: List[int] = []

    def dfs(col: int) -> bool:
        if col == N:
            return True  # se colocaron N reinas

        for fila in range(N):
            if not en_conflicto(parcial, fila, col):
                parcial.append(fila)          # elegir
                if dfs(col + 1):             # explorar
                    return True
                parcial.pop()                 # deshacer (retroceso)
        return False

    if N < 1:
        return None

    if dfs(0):
        return parcial
    return None


# --------------------------------------------------------
# Ejercicio 2 — N reinas con obstáculos
# --------------------------------------------------------
def nreinas_con_obstaculos(N: int, A: List[int]) -> Optional[List[int]]:
    """
    Regresa una solución válida P considerando obstáculos.

    Obstáculos:
      - Si 0 <= j < len(A), entonces (fila=A[j], col=j) está BLOQUEADO.
      - Si j >= len(A), esa columna no tiene bloqueo explícito.

    TODO:
      - En cada columna 'col', salta la fila bloqueada (si aplica).
      - Reusar en_conflicto + backtracking.

     Referencia: enumerate, range y listas
    https://docs.python.org/3/library/functions.html#enumerate
    https://docs.python.org/3/library/stdtypes.html#range
    """
    parcial: List[int] = []

    def fila_bloqueada(col: int) -> Optional[int]:
        if 0 <= col < len(A):
            return A[col]
        return None

    def dfs(col: int) -> bool:
        if col == N:
            return True

        bloqueada = fila_bloqueada(col)
        for fila in range(N):
            if bloqueada is not None and fila == bloqueada:
                continue  # saltar fila bloqueada
            if not en_conflicto(parcial, fila, col):
                parcial.append(fila)
                if dfs(col + 1):
                    return True
                parcial.pop()
        return False

    if N < 1:
        return None

    if dfs(0):
        return parcial
    return None


# --------------------------------------------------------
#  Pistas conceptuales
# --------------------------------------------------------
# - DFS (Depth-First Search) recorre todas las posibilidades posibles en un árbol de decisiones.
# - El retroceso (backtracking) se logra con recursión: probar → explorar → deshacer.
# - Conflictos en N reinas: misma fila o diagonales.
# - En Python, las listas son mutables; usa copy() si vas a guardar estados intermedios.

#  Referencias oficiales:
# - Listas y operaciones: https://docs.python.org/3/tutorial/datastructures.html
# - Tipos (typing): https://docs.python.org/3/library/typing.html
# - Recursión y funciones: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# --------------------------------------------------------


if __name__ == "__main__":
    print("Una solución para N=4:", nreinas(4))
    A = [1, 3, 0, 2]
    print("Una solución con obstáculos:", nreinas_con_obstaculos(4, A))
```

## Ejercicio BFS
```
"""
(El siguiente esqueleto es una sugerencia de la manera en la que pueden organizar su script, pero tienen la libertad de hacer todas las modificaciones que consideren pertinentes. Al final del script, se incluyen sugerencias conceptuales y referencias de Python.)
Práctica BFS — Tiempos de viaje con horarios variables
------------------------------------------------------
Completa los TODO para:
1) Encontrar el camino (en número de aristas) entre dos ciudades usando BFS.
2) Calcular el tiempo total considerando que el factor de tiempo cambia según la hora.

Modelo:
- Grafo no dirigido con pesos base (minutos "sin tráfico").
- Tres franjas horarias:
  [00:00, 06:00) => factor 1.0
  [06:00, 16:00) => factor 2.0
  [16:00, 24:00) => factor 1.5

Sugerencias de sintaxis:
- Cola BFS: collections.deque → https://docs.python.org/3/library/collections.html#collections.deque
- Diccionarios: dict → https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- Módulo datetime (opcional): https://docs.python.org/3/library/datetime.html
"""

from collections import deque
from typing import Dict, List, Tuple, Optional

Ciudad = str
Grafo = Dict[Ciudad, Dict[Ciudad, int]]  # adyacentes con peso base en minutos


# ---------- (1) BFS para camino en número de aristas ----------
def bfs_path(g: Grafo, origen: Ciudad, destino: Ciudad) -> Optional[List[Ciudad]]:
    """
    Regresa una lista de ciudades que representa el camino desde 'origen' hasta 'destino'
    minimizando el número de aristas. Si no hay camino, regresa None.

    TODO:
      - Implementar BFS con una cola (deque).
      - Llevar un diccionario de predecesores para reconstruir el camino.
    """
    if origen not in g or destino not in g:
        return None

    visitado = set([origen])
    pred: Dict[Ciudad, Optional[Ciudad]] = {origen: None}
    q = deque([origen])

    while q:
        u = q.popleft()
        if u == destino:
            break
        for v in g[u]:
            if v not in visitado:
                visitado.add(v)
                pred[v] = u
                q.append(v)

    if destino not in pred:
        return None

    # reconstruir
    camino: List[Ciudad] = []
    actual: Optional[Ciudad] = destino
    while actual is not None:
        camino.append(actual)
        actual = pred[actual]
    camino.reverse()
    return camino


# ---------- (2) Factor horario ----------
def factor_horario(minutos: int) -> float:
    """
    Regresa el factor multiplicativo según el minuto del día (0..1439).
    [00:00, 06:00) => 1.0
    [06:00, 16:00) => 2.0
    [16:00, 24:00) => 1.5

    TODO: implementar los intervalos.
    """
    minutos = minutos % (24 * 60)  # normalizar
    # TODO: retorna 1.0, 2.0 o 1.5 según el intervalo
    if 0 <= minutos < 6 * 60:
        return 1.0
    if 6 * 60 <= minutos < 16 * 60:
        return 2.0
    return 1.5


def siguiente_cambio(minutos: int) -> int:
    """
    Dado 'minutos' desde las 00:00, regresa el minuto (absoluto, 0..infinito)
    en que ocurre el PRÓXIMO cambio de franja (6:00, 16:00 o 24:00).

    Pista:
      - Calcula minuto del día (mod 1440) y desde ahí qué borde viene después.
    """
    md = minutos % (24 * 60)
    dia_base = minutos - md
    bordes = [6 * 60, 16 * 60, 24 * 60]
    for b in bordes:
        if md < b:
            return dia_base + b
    return dia_base + 24 * 60  # siguiente día 00:00


# ---------- (3) Tiempo de viaje respetando cambios de franja ----------
def tiempo_tramo_respetando_horario(inicio: int, duracion_base: int) -> int:
    """
    Calcula los minutos reales de un tramo con 'duracion_base' (minutos sin tráfico),
    iniciando en 'inicio' (minuto absoluto desde 00:00 del día 0),
    aplicando el factor correspondiente y respetando cambios de franja si cruza.

    Estrategia:
      - Simula el avance en bloques hasta consumir 'duracion_base' ponderada.
      - Cada bloque llega al siguiente cambio de franja o consume lo que resta.

    Nota: trabajamos en "tiempo real", no en "tiempo base". Para una simulación simple,
    dividimos la duración real en porciones: real = base * factor.
    """
    real_total = 0
    base_restante = duracion_base

    t = inicio
    while base_restante > 0:
        f = factor_horario(t)
        cambio = siguiente_cambio(t)
        # ¿cuánto tiempo REAL cabe hasta el cambio, si consumiéramos solo en esta franja?
        # Si avanzamos x minutos reales en esta franja, consumimos x/f minutos base.
        # No queremos pasarnos del borde: límite_real = cambio - t.
        limite_real = max(0, cambio - t)

        # ¿cuánto real se necesita para consumir TODO el base_restante con factor f?
        real_necesario = int((base_restante * f) + 0.9999)  # ceil aproximado

        if real_necesario <= limite_real:
            # todo cabe antes del cambio de franja
            real_total += real_necesario
            t += real_necesario
            base_restante = 0
        else:
            # llegamos al borde de franja, consumimos una parte
            # base_consumida = limite_real / f
            base_consumida = limite_real / f
            base_restante = max(0.0, base_restante - base_consumida)
            real_total += limite_real
            t = cambio  # saltar al comienzo de la siguiente franja

    return int(real_total)


def tiempo_total(g: Grafo, camino: List[Ciudad], inicio_min: int) -> int:
    """
    Suma el tiempo real de todos los tramos del 'camino' respetando las franjas.
    - inicio_min: minuto absoluto en el que se arranca (ej: 5:00 => 5*60).

    TODO: iterar pares consecutivos (u,v), tomar peso base g[u][v],
    y acumular usando tiempo_tramo_respetando_horario.
    """
    total = 0
    t_actual = inicio_min
    for u, v in zip(camino, camino[1:]):
        base = g[u][v]
        real = tiempo_tramo_respetando_horario(t_actual, base)
        total += real
        t_actual += real
    return total


# ---------- Grafo de ejemplo (puedes modificarlo) ----------
def grafo_rumania_demo() -> Grafo:
    """
    Devuelve un subgrafo de ejemplo.
    Sustituye con tus datos reales del mapa si los tienes disponibles.
    """
    g: Grafo = {
        "Giurgiu":   {"Bucharest": 90},
        "Bucharest": {"Giurgiu": 90, "Urziceni": 85},
        "Urziceni":  {"Bucharest": 85},
        # Agrega más aristas según tu mapa...
    }
    return g


# ---------- Pruebas rápidas (puedes comentar o borrar) ----------
if __name__ == "__main__":
    g = grafo_rumania_demo()
    path = bfs_path(g, "Giurgiu", "Urziceni")
    print("Camino (BFS, aristas):", path)

    # Ejemplo del enunciado:
    # Viaje a las 5:00 → primera franja (factor 1.0) para Giurgiu→Bucharest,
    # luego cruza 6:00 y la segunda tiene factor 2.0.
    inicio_5am = 5 * 60
    if path:
        print("Tiempo total iniciando 5:00:", tiempo_total(g, path, inicio_5am), "min")

    # Mismo viaje iniciando 4:00 (ambos tramos antes de 6:00 si el primer tramo termina a tiempo):
    inicio_4am = 4 * 60
    if path:
        print("Tiempo total iniciando 4:00:", tiempo_total(g, path, inicio_4am), "min")


# Pistas conceptuales:
# - BFS garantiza el camino más corto en aristas.
# - Los pesos aquí son tiempos, pero el algoritmo base no los usa directamente.
# - La función factor_horario ajusta según la hora del día.
# - Convierte horas a minutos: 5:00 → 300, 16:00 → 960.
#  Referencias:
# - https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# - https://docs.python.org/3/library/datetime.html
# - https://docs.python.org/3/library/collections.html#collections.deque
```
