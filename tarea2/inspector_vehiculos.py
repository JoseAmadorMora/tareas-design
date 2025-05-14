from i_inspector_vehiculos import IInspectorVehiculos
from vehiculo import IVehiculo

class InspectorVehiculos(IInspectorVehiculos):
    def imprimir_datos_vehiculo(self, vehiculo: IVehiculo):
        print(f"Vehículo tipo: {vehiculo.tipo}")
        print(f"Color: {vehiculo.color}")
        print(f"Peso: {vehiculo.peso} kg")
        print(f"Ruedas: {vehiculo.ruedas}")
        print(f"Eléctrico: {'Sí' if vehiculo.es_electrico else 'No'}")
        print(f"Capacidad: {vehiculo.capacidad_pasajeros} pasajeros")
        print(f"Costo: ${self.calcular_costo_vehiculo()}")
        print(f"Requiere inspección: {'Sí' if self.verificar_si_vehiculo_requiere_inspeccion() else 'No'}")
        print("------------------------")
