from modelos.mascota import Mascota

class GestionMascotas:
    def __init__(self):
        self._lista_mascotas = []

    def agregar_mascota(self, nombre, especie):
        nueva = Mascota(nombre, especie)
        self._lista_mascotas.append(nueva)
        print(f"Mascota {nombre} agregada.")

    def listar_mascotas(self):
        print("\n--- Lista de Mascotas ---")
        for m in self._lista_mascotas:
            print(m)