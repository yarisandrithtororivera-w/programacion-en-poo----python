from modelo_animales import Animales
from modelo_caballo import modelo_caballo
from modelo_cocodrilo import modelo_cocodrilo
from modelo_escarabajo import modelo_escarabajo
from modelo_pato import modelo_pato
from modelo_pez import modelo_pez

objmodelo_animales=Animales("perro","el campo","canin")
objmodelo_animales.imprimir_info()

objmodelo_caballo= modelo_caballo("yegua","el campo","mamifero herbívoro no rumiante","aproximadamente entre el 15% y el 20% de su peso corporal")
objmodelo_caballo.imprimir_info()

objmodelo_cocodrilo= modelo_cocodrilo ("cocodrilo","en el agua","acuatico","3 metros")
objmodelo_cocodrilo.imprimir_info()

objmodelo_escarabajo= modelo_escarabajo ("escarabajo","enterrados en la tierra",,"insecto","6 patas")
objmodelo_escarabajo.imprimir_info()

objmodelo_pato=modelo_pato ("pato","patio","ave")
objmodelo_pato.imprimir_info()

objmodelo_pez= modelo_pez ("pez","agua","acuatico","3 aletas")
objmodelo_pez.imprimir_info()