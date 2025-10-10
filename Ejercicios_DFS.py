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
