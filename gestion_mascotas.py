class GestionMascotas:
    def __init__(self):
        self.lista_mascotas = []

    def agregar(self, mascota):
        self.lista_mascotas.append(mascota)

    def mostrar_todo(self):
        print("\n--- Lista de Mascotas ---")
        for m in self.lista_mascotas:
            # Polimorfismo: el objeto sabe qué decir al llamar a .hablar()
            print(f"{m.get_nombre()} dice: {m.hablar()}")