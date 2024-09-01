from colorama import Fore, Style, init
from AgenteIA.AgenteBuscador import AgenteBuscador
from AgenteIA.Bote.Bote_Acciones import BoteAcciones
from .Estado_Validador import EstadoValidador
from .Buscador_A_Estrella import BuscadorAEstrella

# Inicializa colorama
init(autoreset=True)

class AgenteMapu(AgenteBuscador):

    def __init__(self):
        AgenteBuscador.__init__(self)
        self.estado_inicial = (3, 3, 0)
        self.estado_meta = (0, 0, 1)
        self.bote_acciones = BoteAcciones()
        self.estado_validador = EstadoValidador()
        self.indice_accion = 0

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
                    # Log detallado del movimiento realizado
                    print(self.detalle_movimiento(estado, sucesor))
                    stack.append((sucesor, camino + [sucesor]))
        
        return None
    
    def obtener_proxima_accion(self):
        if self.indice_accion < len(self.acciones):
            accion = self.acciones[self.indice_accion]
            self.indice_accion += 1  # Avanzar al siguiente índice
            return accion
        return "No hay más acciones disponibles"

    def detalle_movimiento(self, estado, sucesor):
        m_izq, c_izq, bote_izq = estado
        m_der, c_der = 3 - m_izq, 3 - c_izq
        bote_der = 1 - bote_izq

        m_izq_n, c_izq_n, bote_izq_n = sucesor
        m_der_n, c_der_n = 3 - m_izq_n, 3 - c_izq_n

        lado_bote = "izquierda" if bote_izq else "derecha"
        lado_bote_n = "izquierda" if bote_izq_n else "derecha"

        return (f"{Fore.BLUE}Bote en la {Fore.YELLOW}{lado_bote}{Fore.RESET}: "
                f"{Fore.GREEN}{m_izq} misioneros, {c_izq} caníbales en la izquierda; "
                f"{Fore.RED}{m_der} misioneros, {c_der} caníbales en la derecha.{Fore.RESET} "
                f"-> {Fore.BLUE}Movimiento a la {Fore.YELLOW}{lado_bote_n}{Fore.RESET}: "
                f"{Fore.GREEN}{m_izq_n} misioneros, {c_izq_n} caníbales en la izquierda; "
                f"{Fore.RED}{m_der_n} misioneros, {c_der_n} caníbales en la derecha.{Fore.RESET}")

    def programa(self):
        buscador_a_estrella = BuscadorAEstrella(self.heuristica, self.sucesor, self.estado_inicial, self.estado_meta)
        solucion_dfs = self.buscar_profundidad()
        solucion_a_estrella = buscador_a_estrella.buscar()

        # Mostrar paso a paso la solución DFS
        print("Pasos de la solución DFS:")
        for i, paso in enumerate(solucion_dfs):
            print(f"Paso {i+1}: {self.detalle_movimiento(solucion_dfs[i-1] if i > 0 else self.estado_inicial, paso)}")
        print("Solución DFS:", solucion_dfs)

        # Mostrar paso a paso la solución A*
        print("Pasos de la solución A*:")
        for i, paso in enumerate(solucion_a_estrella):
            print(f"Paso {i+1}: {self.detalle_movimiento(solucion_a_estrella[i-1] if i > 0 else self.estado_inicial, paso)}")
        print("Solución A*:", solucion_a_estrella)

        self.acciones = solucion_a_estrella if solucion_a_estrella else "No se encontró solución"