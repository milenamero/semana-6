from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def ejecutar():
    mi_restaurante = Restaurante()
    
    # Crear objetos usando las clases heredadas
    p1 = Platillo("Pizza", 10.0)
    b1 = Bebida("Refresco", 2.0)
    
    # Agregar productos al servicio
    mi_restaurante.agregar(p1)
    mi_restaurante.agregar(b1)
    
    # Mostrar resultados
    mi_restaurante.mostrar_todo()

if __name__ == "__main__":
    ejecutar()