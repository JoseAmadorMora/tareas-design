from abc import ABC, abstractmethod
from vehiculo import IVehiculo

class IInspectorVehiculos:
    @abstractmethod
    def calcular_costo_vehiculo(self, vehiculo: IVehiculo) -> float:
        pass
    @abstractmethod
    def verificar_si_vehiculo_requiere_inspeccion(self, vehiculo: IVehiculo) -> bool:
        pass
    @abstractmethod
    def imprimir_datos_vehiculo(self, vehiculo: IVehiculo):
        pass