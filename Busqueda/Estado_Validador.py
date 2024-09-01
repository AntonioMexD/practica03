class EstadoValidador:
    def estado_valido(self, estado):
        misioneros_izq, canibales_izq, _ = estado
        misioneros_der = 3 - misioneros_izq
        canibales_der = 3 - canibales_izq

        if (misioneros_izq < canibales_izq and misioneros_izq > 0) or \
           (misioneros_der < canibales_der and misioneros_der > 0):
            return False

        if not (0 <= misioneros_izq <= 3 and 0 <= canibales_izq <= 3):
            return False

        return True
