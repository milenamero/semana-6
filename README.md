# Sistema de Gestión de Restaurante - Proyecto Modular

**Integrantes:**
- Mero Loor Milena Mayerli
- Mendoza Vélez Grace Rosalinda

## Descripción del Proyecto
Este proyecto es una aplicación modular en Python desarrollada como parte de la asignatura de Programación Orientada a Objetos (POO). El objetivo es gestionar el inventario de productos de un restaurante, aplicando una arquitectura limpia que separa las responsabilidades en modelos y servicios.

## Estructura del Proyecto
El proyecto está organizado para facilitar la mantenibilidad y escalabilidad:
- `modelos/`: Contiene la jerarquía de clases (`producto.py`, `platillo.py`, `bebida.py`).
- `servicios/`: Contiene la clase `Restaurante`, encargada de la lógica de administración y listado de productos.
- `main.py`: Punto de entrada del sistema que ejecuta la simulación.

## Principios de POO Aplicados
Para cumplir con los requisitos académicos, hemos implementado los pilares fundamentales:

1. **Herencia:** Hemos creado una clase padre `Producto` que centraliza los atributos comunes. Las clases `Platillo` y `Bebida` heredan esta estructura, permitiendo reutilizar código eficientemente.
2. **Encapsulamiento:** Protegemos la integridad de los datos sensibles (como el precio) utilizando el prefijo `__`. El acceso y modificación de estos valores se realiza exclusivamente a través de métodos de validación (`get_precio` y `cambiar_precio`), garantizando que no se introduzcan valores negativos o no válidos.
3. **Polimorfismo:** Implementamos el método `mostrar_informacion()` en las clases hijas. Esto permite que, al iterar sobre una lista de productos, cada objeto responda de manera única según su tipo (platillo o bebida), demostrando el uso de polimorfismo.

## Cómo ejecutar el proyecto
1. Asegúrate de tener instalado Python en tu entorno.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Ejecuta el programa mediante el comando:
   ```bash
   py main.py