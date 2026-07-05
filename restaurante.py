class Restaurante:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrar_todo(self):
        print("\n--- Menú del Restaurante ---")
        for p in self.productos:
            # Polimorfismo: el método mostrar_informacion se comporta diferente
            print(p.mostrar_informacion())