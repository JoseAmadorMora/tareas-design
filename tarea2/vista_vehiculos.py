from tarea2.i_vista_vehiculos import IVistaVehiculos
from tarea2.vehiculos import IVehiculo

class VistaVehiculos(IVistaVehiculos):
    def imprimir_datos_vehiculo(self, vehiculo: IVehiculo):
        print(f"Vehículo tipo: {vehiculo.tipo}")
        print(f"Color: {vehiculo.color}")
        print(f"Peso: {vehiculo.peso} kg")
        print(f"Ruedas: {vehiculo.ruedas}")
        print(f"Eléctrico: {'Sí' if vehiculo.es_electrico else 'No'}")
        print(f"Capacidad: {vehiculo.capacidad_pasajeros} pasajeros")
        print(f"Costo: ${vehiculo.calcular_costo()}")
        print(f"Requiere inspección: {'Sí' if vehiculo.requiere_inspeccion() else 'No'}")
        print("------------------------")
