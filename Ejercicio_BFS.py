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

