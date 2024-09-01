from AgenteIA.AgenteBuscador import AgenteBuscador
from queue import PriorityQueue

class AgenteMapu(AgenteBuscador):

    def __init__(self):
        super().__init__()
        self.estado_inicial = [3, 3, 1]  # [pacifistas, verdugos, bote_posicion]
        self.estado_meta = [0, 0, 0]  # [pacifistas, verdugos, bote_posicion]
        self.acciones = []

    def es_estado_valido(self, estado):
        pi, vi, bote = estado
        pd = 3 - pi
        vd = 3 - vi
        if pi < 0 or vi < 0 or pd < 0 or vd < 0:
            return False
        if (pi > 0 and pi < vi) or (pd > 0 and pd < vd):
            return False
        return True

    def es_estado_meta(self, estado):
        return estado == self.estado_meta

    def sucesor(self, estado):
        pi, vi, bote = estado
        sucesores = []
        movimientos = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        
        for m in movimientos:
            if bote == 1:
                nuevo_estado = [pi - m[0], vi - m[1], 0]
            else:
                nuevo_estado = [pi + m[0], vi + m[1], 1]
            
            if self.es_estado_valido(nuevo_estado):
                sucesores.append((m, nuevo_estado))
        
        return sucesores

    def heuristica(self, estado):
        # Heurística simple: número de personas restantes en la orilla izquierda
        pi, vi, _ = estado
        return pi + vi

    def programa(self):
        # Implementación del algoritmo A*
        open_list = PriorityQueue()
        open_list.put((0, self.estado_inicial))
        came_from = {}
        g_cost = {tuple(self.estado_inicial): 0}

        while not open_list.empty():
            _, estado_actual = open_list.get()
            estado_actual = tuple(estado_actual)

            if estado_actual == tuple(self.estado_meta):
                print("Solución encontrada:", estado_actual)
                break

            print(f"Explorando estado: {estado_actual}")

            for accion, sucesor in self.sucesor(list(estado_actual)):
                sucesor = tuple(sucesor)
                nuevo_costo = g_cost[estado_actual] + 1
                if sucesor not in g_cost or nuevo_costo < g_cost[sucesor]:
                    g_cost[sucesor] = nuevo_costo
                    prioridad = nuevo_costo + self.heuristica(sucesor)
                    open_list.put((prioridad, list(sucesor)))
                    came_from[sucesor] = (estado_actual, accion)
                    print(f"  Generando sucesor: {sucesor} con acción: {accion}")

        # Reconstruir el camino desde el estado meta
        estado = tuple(self.estado_meta)
        camino = []
        while estado in came_from:
            estado, accion = came_from[estado]
            camino.append(accion)
        camino.reverse()
        self.acciones = camino

        print("Camino de acciones:", self.acciones)