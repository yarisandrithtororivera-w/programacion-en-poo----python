from modelo_carro import Vehiculo
class carroDeportivo(Vehiculo):
    def __init__(self,color,marca,motor,convertible):
        super().__init__(color,marca,motor)
        self.convertible=convertible
        def acelerar_rapido(self):
            print(f"el {self.marca}acelera muy rapido por ser deporitvo")
            
            def imprimir_info(self):
                super().imprimir_info()
                print(f"convertible:{self.convertible}")