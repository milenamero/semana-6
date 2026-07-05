class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self.__precio = precio  # Encapsulamiento

    def get_precio(self):
        return self.__precio

    def mostrar_informacion(self):
        pass # Se define en clases hijas