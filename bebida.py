from modelos.producto import Producto
class Bebida(Producto):
    def mostrar_informacion(self):
        return f"Bebida: {self._nombre}, Precio: ${self.get_precio()}"