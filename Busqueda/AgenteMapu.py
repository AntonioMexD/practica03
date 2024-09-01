from AgenteIA.AgenteBuscador import AgenteBuscador
from AgenteIA.Bote.Bote_Acciones import BoteAcciones
from .Estado_Validador import EstadoValidador
from .Buscador_A_Estrella import BuscadorAEstrella

class AgenteMapu(AgenteBuscador):

    def __init__(self):
        AgenteBuscador.__init__(self)
        self.estado_inicial = (3, 3, 0)
        self.estado_meta = (0, 0, 1)
        self.bote_acciones = BoteAcciones()
        self.estado_validador = EstadoValidador()

    def sucesor(self, estado):
        return self.bote_acciones.generar_sucesores(estado, self.estado_validador.estado_valido)


    def heuristica(self, estado):
        misioneros_izq, canibales_izq, _ = estado
        return misioneros_izq + canibales_izq  # Heurística simple: número total de personas que deben cruzar

    def buscar_profundidad(self):
        stack = [(self.estado_inicial, [])]  # (estado, camino)
        visitados = set()

        while stack:
            estado, camino = stack.pop()
            
            if estado in visitados:
                continue
            
            visitados.add(estado)

            if estado == self.estado_meta:
                return camino
            
            for sucesor in self.sucesor(estado):
                if sucesor not in visitados:
                    stack.append((sucesor, camino + [sucesor]))
        
        return None

    def programa(self):
        buscador_a_estrella = BuscadorAEstrella(self.heuristica, self.sucesor, self.estado_inicial, self.estado_meta)
        solucion_dfs = self.buscar_profundidad()
        solucion_a_estrella = buscador_a_estrella.buscar()
        print("Solución DFS:", solucion_dfs)
        print("Solución A*:", solucion_a_estrella)
        self.acciones = solucion_a_estrella if solucion_a_estrella else "No se encontró solución"