# Revisión técnica del sistema

## Objetivo

Realizar una revisión técnica de la versión refactorizada del Sistema de Gestión de Solicitudes Académicas, verificando la calidad interna del código, el cumplimiento de buenas prácticas y la conservación de las funcionalidades originales.
Esta revisión se realizó como una autorrevisión técnica, utilizando criterios habituales de Code Review.

## Checklist de revisión

| Criterio                        | Resultado | Observación                                                                   |
|---------------------------------|-----------|-------------------------------------------------------------------------------|
| Separación de responsabilidades | Cumple    | Se separaron interfaz, servicios y almacenamiento.                            |
| Nombres claros y descriptivos   | Cumple    | Se utilizaron nombres que representan las responsabilidades de cada elemento. |
| Métodos pequeños y específicos  | Cumple    | Se extrajeron métodos auxiliares para reducir la complejidad.                 |
| Reducción de código duplicado   | Cumple    | Se centralizaron operaciones comunes.                                         |
| Manejo de excepciones           | Cumple    | Se reemplazaron capturas genéricas por excepciones específicas.               |
| Validación de datos             | Cumple    | Se incorporaron validaciones para los datos ingresados.                       |
| Separación del almacenamiento   | Cumple    | La persistencia JSON quedó aislada en una clase específica.                   |
| Uso de abstracciones            | Cumple    | Se incorporó Protocol para definir el contrato del repositorio.               |
| Pruebas automatizadas           | Cumple    | Se implementaron seis pruebas unitarias.                                      |
| Conservación del comportamiento | Cumple    | Se verificó el funcionamiento de las operaciones principales.                 |

## Observaciones de la revisión

La refactorización permitió mejorar la organización del proyecto y distribuir las responsabilidades entre diferentes componentes.

Se identificaron oportunidades de mejora para futuras versiones:

- Incorporar pruebas adicionales para los casos de error al cambiar estados y asignar responsables.
- Reemplazar progresivamente los diccionarios utilizados para representar datos por objetos de dominio.
- Permitir configurar la ubicación del archivo JSON sin modificar el código fuente.

## Feedback técnico

La nueva estructura presenta una separación más clara entre la interfaz de usuario, la lógica de negocio y la persistencia de datos.

Las validaciones incorporadas permiten controlar situaciones incorrectas sin interrumpir la ejecución del programa. Además, las pruebas automatizadas facilitan la verificación de las operaciones principales.

Se considera que la versión refactorizada cumple con los criterios establecidos para esta revisión, aunque existen mejoras adicionales que podrían implementarse en futuras iteraciones.

## Criterios de aceptación

- Las funcionalidades originales continúan disponibles.
- La información se conserva mediante archivos JSON.
- Las responsabilidades principales se encuentran separadas.
- Se ejecutan correctamente las seis pruebas unitarias.
- Los cambios realizados no alteran el funcionamiento esperado del sistema.