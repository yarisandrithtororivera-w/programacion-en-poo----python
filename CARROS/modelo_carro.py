class Vehiculo:
    def __init__(self,color,marca,motor):
        self.color= color
        self.marca=marca
        self.motor=motor
    def arrancar(self):
     print(f"El vehiculo{self.marca} esta arrancando.")
    def apagar(self):
        print(f"el vehiculo {self.marca} se apagó.")
        
    def imprimir_info(self):
        print(f"la marca es:{self.marca}")
        print(f"el color del vehiculo es:{self.color}")
        print(f"el tipo de motor es:{self.motor}")