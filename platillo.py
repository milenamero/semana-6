from modelos.producto import Producto
class Platillo(Producto):
    def mostrar_informacion(self):
        return f"Platillo: {self._nombre}, Precio: ${self.get_precio()}"