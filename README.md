# Sistema de Gestión de Mascotas - Proyecto Modular

**Integrantes:**
- Mero Loor Milena Mayerli
- Mendoza Vélez Grace Rosalinda

## Descripción del Proyecto
Este proyecto es una aplicación modular en Python diseñada para gestionar el registro de mascotas. El objetivo principal ha sido aplicar los pilares de la Programación Orientada a Objetos (POO) para crear un código robusto, escalable y fácil de mantener.

## Estructura del Proyecto
La organización modular nos permite separar las responsabilidades de cada componente del sistema:
- `modelos/`: Contiene la definición de las clases entidad. Aquí se implementan la **herencia** y el **encapsulamiento**.
- `servicios/`: Contiene la clase `GestionMascotas`, encargada de la lógica de negocio y el manejo de los objetos.
- `main.py`: Punto de entrada de la aplicación que ejecuta el sistema.

## Conceptos de POO Aplicados
Para cumplir con los estándares de desarrollo profesional, hemos implementado los siguientes pilares de la POO:

1. **Herencia:** Definimos una clase base `Mascota` que contiene los atributos generales, mientras que las clases `Perro` y `Gato` heredan esta estructura, extendiendo su funcionalidad.
2. **Encapsulamiento:** Protegemos la integridad de los datos utilizando atributos privados (prefijo `__`). Esto evita la modificación directa de los atributos fuera de la clase y asegura un control total a través de métodos de acceso (getters).
3. **Polimorfismo:** Implementamos el método `hablar()` en la clase base. Cada clase hija (`Perro`, `Gato`) sobrescribe este método, permitiendo que un mismo llamado produzca comportamientos distintos según el objeto.

## Cómo ejecutar el proyecto
1. Asegúrate de tener instalado Python en tu computadora.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Ejecuta el comando:
   `py main.py`

## Reflexión sobre la Modularidad
La modularidad es fundamental en el desarrollo de software. Al separar las responsabilidades en diferentes archivos (modelos y servicios), logramos un código más limpio, fácil de mantener y escalar. Esta estructura no solo evita que el sistema sea un "bloque" difícil de modificar, sino que permite trabajar de forma colaborativa y ordenada, facilitando la detección de errores y la implementación de nuevas funcionalidades en el futuro.