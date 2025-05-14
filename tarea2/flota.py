from tarea2.vehiculos import IVehiculo
class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self):
        tipo = input("Tipo (auto/moto/camion): ").lower()
        color = input("Color: ")
        peso = float(input("Peso (kg): "))
        if tipo == 'moto':
            ruedas = 2
            capacidad = 2
        else:
            ruedas = 4
            capacidad = 5 if tipo == 'auto' else 2
        electrico = input("Es eléctrico? (s/n): ").lower() == 's'
        v = IVehiculo(tipo, color, peso, ruedas, electrico, capacidad)
        self.vehiculos.append(v)
        print("Vehículo agregado!")
        
