class Animales:
    def __init__(self,nombre,habitat,especie):
        self.nombre= nombre
        self.habitat= habitat
        self.especie= especie
    def  mover(self):
        print(f"los animales se mueven para ir a buscar su comida:{self.nombre}")
    def alimentar (self):
        print (f"los animales se alimentan dependiendo su especie:{self.especie}")    
    def imprimir_info (self):
        print(f" su nombre es :{self.nombre}")
        print(f"su habitat es :{self.habitat}")   
        print (f"su especie es:{self.especie}")