class BoteAcciones:
    def __init__(self):
        self.acciones = [
            (2, 0),  # Dos misioneros cruzan
            (0, 2),  # Dos caníbales cruzan
            (1, 1),  # Un misionero y un caníbal cruzan
            (1, 0),  # Un misionero cruza
            (0, 1)   # Un caníbal cruza
        ]

    def generar_sucesores(self, estado, estado_valido_func):
        sucesores = []
        misioneros_izq, canibales_izq, bote = estado

        for accion in self.acciones:
            nuevo_estado = (
                misioneros_izq - accion[0] if bote == 0 else misioneros_izq + accion[0],
                canibales_izq - accion[1] if bote == 0 else canibales_izq + accion[1],
                1 - bote
            )

            if estado_valido_func(nuevo_estado):
                sucesores.append(nuevo_estado)

        return sucesores
