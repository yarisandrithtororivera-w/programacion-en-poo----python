from modelo_animales import Animales
class modelo_pato (Animales):
    def __init__(self, nombre, habitat, especie, nadar):
        super().__init__(nombre, habitat, especie)
        self.nadar = nadar
    def imprimir_info(self):
        super().imprimir_info()
        print(f"nadar:{nadar}")