class Mascota:
    def __init__(self, nombre, especie):
        self._nombre = nombre
        self._especie = especie

    def __str__(self):
        return f"Mascota: {self._nombre} | Especie: {self._especie}"
    