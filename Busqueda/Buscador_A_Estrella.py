import heapq

class BuscadorAEstrella:
    def __init__(self, heuristica_func, sucesor_func, estado_inicial, estado_meta):
        self.heuristica_func = heuristica_func
        self.sucesor_func = sucesor_func
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta

    def buscar(self):
        open_set = []
        heapq.heappush(open_set, (0 + self.heuristica_func(self.estado_inicial), self.estado_inicial, []))
        visitados = set()
        costos = {self.estado_inicial: 0}

        while open_set:
            _, estado, camino = heapq.heappop(open_set)

            if estado in visitados:
                continue

            visitados.add(estado)

            if estado == self.estado_meta:
                return camino

            for sucesor in self.sucesor_func(estado):
                nuevo_costo = costos[estado] + 1
                if sucesor not in costos or nuevo_costo < costos[sucesor]:
                    costos[sucesor] = nuevo_costo
                    heapq.heappush(open_set, (nuevo_costo + self.heuristica_func(sucesor), sucesor, camino + [sucesor]))

        return None
