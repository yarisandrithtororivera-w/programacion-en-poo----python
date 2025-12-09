from modelo_carro import Vehiculo
class carroCargapesada(Vehiculo):
    def __init__(self,color,marca,motor,capacidad_carga):
        super().__init__(color,marca,motor)
        self.capacidad_carga=capacidad_carga
        def descargar(self):
            print(f"el camion {self.marca} esta descargando el material")
        def imprimir_info(self):
            super().imprimir_info()
            print(f"capacidad_carga:{capacidad_carga}")
    