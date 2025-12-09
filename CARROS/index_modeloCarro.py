from modelo_carro import Vehiculo
from modelo_carroDeportivo import carroDeportivo
from modelo_carroVan import carroVan
from modelo_carroCargapesada import carroCargapesada
print(f"--------modelo de carro ---------")
objVehiculo=Vehiculo("negro","nissan","BR38DETT")
objVehiculo.imprimir_info()

#instancia de las hijas
print(f"--------carro Deportivo ---------")
objmodelo_carroDeportivo=carroDeportivo("rojo","lamborghini","B126.5L","roadster")
objmodelo_carroDeportivo.imprimir_info()

print(f"--------carro Van ---------")
objmodelo_carroVan=carroVan ("gris","mercedes","B88.0L","15")
objmodelo_carroVan.imprimir_info()

print(f"--------carro Carga pesada ---------")
objmodelo_carroCargapesada=carroCargapesada("verde","foton","W16","20 toneladas")
objmodelo_carroCargapesada.imprimir_info()