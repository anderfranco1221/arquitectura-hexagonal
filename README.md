
## Descripción

Este proyecto tiene como objetivo indagar y implementar en la arquitectura hexagonal con el framework de fast api.  Con el fin de mejorar la escalabilidad, mantenibilidad y separación de responsabilidades, se ha decidido investigar e implementar una arquitectura hexagonal.

## Objetivo

El objetivo principal de esta iniciativa es adaptar el proyecto a una arquitectura hexagonal, también conocida como arquitectura de puertos y adaptadores. Esta arquitectura busca desacoplar la lógica de negocio del resto del sistema, permitiendo que los cambios en la infraestructura no afecten el núcleo del negocio.

## Tareas

1. **Investigación**:
   - Indagar sobre los principios fundamentales de la arquitectura hexagonal.
   - Revisar ejemplos y patrones comunes de implementación.
   - Evaluar las herramientas y frameworks que faciliten la implementación.

2. **Implementación**:
   - Diseñar una estructura de directorios que refleje la arquitectura hexagonal.
   - Desarrollar el núcleo del negocio, asegurando que esté completamente desacoplado de la infraestructura.
   - Crear puertos que definan las interfaces necesarias para interactuar con el núcleo del negocio.
   - Implementar adaptadores para interactuar con bases de datos, APIs externas, interfaces de usuario, etc.
   - Realizar pruebas para asegurar que los módulos están correctamente desacoplados y cumplen con sus responsabilidades.

3. **Documentación**:
   - Documentar las decisiones arquitectónicas.
   - Proveer ejemplos de código y explicación de cómo interactúan los diferentes componentes.
   - Incluir instrucciones sobre cómo añadir nuevas funcionalidades sin comprometer la arquitectura.

## Beneficios Esperados

- **Flexibilidad**: Al desacoplar el núcleo del negocio del resto de la infraestructura, es más fácil adaptar o reemplazar partes del sistema.
- **Mantenibilidad**: La clara separación de responsabilidades facilita la comprensión y modificación del código.
- **Escalabilidad**: La arquitectura hexagonal permite un crecimiento más orgánico del sistema sin comprometer su integridad.

## Requisitos

- Conocimientos básicos de patrones de diseño y principios SOLID.
- Familiaridad con el lenguaje de programación y frameworks utilizados en el proyecto.
- Disposición para aprender y aplicar nuevos conceptos arquitectónicos.
- Conocimientos en python y el framework de fast api
- Conocimientos básicos de Docker y las acciones de git hub

## Conclusión

La implementación de una arquitectura hexagonal en este proyecto es un paso clave para garantizar su sostenibilidad a largo plazo. Se espera que la investigación y adaptación a esta arquitectura ofrezcan mejoras significativas en la calidad y flexibilidad del código.

