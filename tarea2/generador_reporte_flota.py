from flota import Flota
from i_vista_vehiculos import IVistaVehiculos

class GeneradorReporteFlota:
    def __init__(self, vista_vehiculos: IVistaVehiculos):
        self.vista_vehiculos = vista_vehiculos

    def generar_reporte(self, vehiculos: Flota):
        total = 0
        electricos = 0
        requiere_inspeccion = 0
        for v in vehiculos.vehiculos:
            self.vista_vehiculos.imprimir_datos_vehiculo(v)
            total += v.calcular_costo()
            if v.es_electrico:
                electricos += 1
            if v.requiere_inspeccion():
                requiere_inspeccion += 1
        print(f"\nRESUMEN FLOTA:")
        print(f"Total vehículos: {len(vehiculos.vehiculos)}")
        print(f"Vehículos eléctricos: {electricos}")
        print(f"Requieren inspección: {requiere_inspeccion}")
        print(f"Valor total: ${total}")