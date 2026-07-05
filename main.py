from servicios.gestion_mascotas import GestionMascotas

def ejecutar():
    sistema = GestionMascotas()
    sistema.agregar_mascota("Firulais", "Perro")
    sistema.agregar_mascota("Michi", "Gato")
    sistema.listar_mascotas()

if __name__ == "__main__":
    ejecutar()