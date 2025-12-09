from modelo_carro import Vehiculo
class carroVan(Vehiculo):
    def __init__(self,color,marca,motor,capacidad_pasajeros):
        super().__init__(color,marca,motor)
        self.capacidad_pasajeros=capacidad_pasajeros
        
        def imprimir_info(self):
            super().imprimir_info()
            print(f"capacidad_pasajeros:{capacidad_pasajeros}")