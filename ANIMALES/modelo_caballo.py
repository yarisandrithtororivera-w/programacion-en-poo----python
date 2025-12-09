from modelo_animales import Animales
class modelo_caballo(Animales):
    def __init__(self, nombre, habitat, especie,capacidad_carga):
        super().__init__(nombre, habitat, especie)
        self.capacidad_carga=capacidad_carga
    def correr (self):
        print(f"el caballo puede llegar a correr mas de 25 kilometros en un dia{self.nombre}")   
    def peso (self):
        print(f" el caballo puede llegar a cargar entre el 15% y el 20% de su peso corporal:{self.capacidad_carga}") 
        
        def imprimir_info(self):
                super().imprimir_info()
                print(f"capacidad_carga:{self.capacidad_carga}")    