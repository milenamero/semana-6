class Mascota:
    def __init__(self, nombre, edad):
        # Encapsulamiento: atributo privado con __
        self.__nombre = nombre
        self.__edad = edad

    # Método para acceder al nombre (Encapsulamiento)
    def get_nombre(self):
        return self.__nombre

    # Método base para Polimorfismo
    def hablar(self):
        pass

# Herencia: Perro y Gato heredan de Mascota
class Perro(Mascota):
    def hablar(self):
        return "¡Guau!"

class Gato(Mascota):
    def hablar(self):
        return "¡Miau!"