from vehiculo import IVehiculo
from i_inspector_vehiculos import IInspectorVehiculos

class GeneradorReporteFlota:
    def __init__(self, sistema_inspector: IInspectorVehiculos):
        self.sistema_inspector = sistema_inspector

    def generar_reporte(self, vehiculos: IVehiculo):
        total = 0
        electricos = 0
        requiere_inspeccion = 0
        for v in vehiculos.vehiculos:
            self.sistema_inspector.imprimir_datos_vehiculo(v)
            total += self.sistema_inspector.calcular_costo_vehiculo(v)
            if v.es_electrico:
                electricos += 1
            if v.necesita_inspeccion():
                requiere_inspeccion += 1
        print(f"\nRESUMEN FLOTA:")
        print(f"Total vehículos: {len(vehiculos.vehiculos)}")
        print(f"Vehículos eléctricos: {electricos}")
        print(f"Requieren inspección: {requiere_inspeccion}")
        print(f"Valor total: ${total}")