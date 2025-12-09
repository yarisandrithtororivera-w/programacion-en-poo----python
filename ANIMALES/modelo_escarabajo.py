from modelo_animales import Animales
class modelo_escarabajo (Animales):
    def __init__(self, nombre, habitat, especie,cantidad_patas):
        super().__init__(nombre, habitat, especie)
        self.cantidad_patas=cantidad_patas
    def imprimir_info(self):
                super().imprimir_info()
                print(f"cantidad_patas:{self.cantidad_patas}") 