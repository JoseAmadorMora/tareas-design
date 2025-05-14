from abc import ABC, abstractmethod

class IVehiculo(ABC):
    def __init__(self, color, peso, ruedas, es_electrico, capacidad_pasajeros, estado="nuevo"):
        self.color = color
        self.peso = peso
        self.ruedas = ruedas
        self.es_electrico = es_electrico
        self.capacidad_pasajeros = capacidad_pasajeros
        self.estado = estado
        self.tipo = ""

    @abstractmethod
    def calcular_costo(self) -> float:
        pass

    @abstractmethod
    def requiere_inspeccion(self) -> bool:
        pass


class Auto(IVehiculo):
    costo_base = 15000
    multiplicador_extra = 100
    recargo_electrico = 5000

    def __init__(self, color, peso, es_electrico=False, capacidad_pasajeros=5):
        super().__init__(color, peso, ruedas=4, es_electrico=es_electrico, capacidad_pasajeros=capacidad_pasajeros)
        self.tipo = "auto"

    def calcular_costo(self):
        extra = self.peso * self.multiplicador_extra
        if self.es_electrico:
            extra += self.recargo_electrico
        return self.costo_base + extra

    def requiere_inspeccion(self):
        return self.peso > 2000


class Moto(IVehiculo):
    costo_base = 8000
    multiplicador_extra = 50
    recargo_electrico = 3000

    def __init__(self, color, peso, es_electrico=False):
        super().__init__(color, peso, ruedas=2, es_electrico=es_electrico, capacidad_pasajeros=2)
        self.tipo = "moto"

    def calcular_costo(self):
        extra = self.peso * self.multiplicador_extra
        if self.es_electrico:
            extra += self.recargo_electrico
        return self.costo_base + extra

    def requiere_inspeccion(self):
        return self.peso > 300


class Camion(IVehiculo):
    costo_base = 45000
    multiplicador_extra = 200

    def __init__(self, color, peso, capacidad_pasajeros=2):
        super().__init__(color, peso, ruedas=6, es_electrico=False, capacidad_pasajeros=capacidad_pasajeros)
        self.tipo = "camión"

    def calcular_costo(self):
        return self.costo_base + self.peso * self.multiplicador_extra

    def requiere_inspeccion(self):
        return True

