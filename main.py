from modelos.mascota import Perro, Gato
from servicios.gestion_mascotas import GestionMascotas

def ejecutar():
    mi_gestion = GestionMascotas()
    
    # Agregando objetos (Herencia)
    mi_gestion.agregar(Perro("Firulais", 3))
    mi_gestion.agregar(Gato("Michi", 2))
    
    # Mostrar resultados
    mi_gestion.mostrar_todo()

if __name__ == "__main__":
    ejecutar()