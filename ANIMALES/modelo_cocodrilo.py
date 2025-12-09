from modelo_animales import Animales
class modelo_cocodrilo (Animales):
    def __init__(self, nombre, habitat, especie, tamaño):
        super().__init__(nombre, habitat, especie)
        self.tamaño= tamaño
    def medir (self):
        print(f"los cocodrilos pueden llegar a medir mas de tres metros de largo{self.nombre}") 
           
    def imprimir_info(self):
            super().imprimir_info()
            print(f"tamaño:{tamaño}") 