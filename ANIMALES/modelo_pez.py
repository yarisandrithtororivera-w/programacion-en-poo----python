from modelo_animales import Animales
class modelo_pez (Animales):
    def __init__(self, nombre, habitat, especie,aletas):
        super().__init__(nombre, habitat, especie)
        self.aletas= aletas
        
    def imprimir_info(self):
        super().imprimir_info()
        print(f"aletas:{aletas}")
        
