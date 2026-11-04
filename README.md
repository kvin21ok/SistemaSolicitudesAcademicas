# Sistema de Gestión de Solicitudes Académicas

Sistema de consola desarrollado en Python para gestionar solicitudes realizadas por estudiantes de una institución educativa.

## Funcionalidades

- Registrar solicitudes.
- Cambiar el estado de las solicitudes.
- Asignar responsables.
- Buscar solicitudes por estado, prioridad o tipo.
- Generar reportes básicos.
- Guardar la información mediante archivos JSON.

## Tecnologías utilizadas

- Python
- Programación Orientada a Objetos (POO).
- Dataclasses.
- Protocol.
- Persistencia mediante archivos JSON.
- unittest para pruebas automatizadas.

## Estructura del proyecto

- `src/`: contiene el código fuente del sistema.
- `data/`: contiene el archivo JSON con los datos.
- `tests/`: contiene las pruebas automatizadas.
- `evidencias/`: contiene capturas del proceso y resultados de las pruebas.

## Instalación y ejecución

Clonar el repositorio:

```
git clone https://github.com/kvin21ok/SistemaSolicitudesAcademicas.git
```

Ingresar a la carpeta del proyecto:

```
cd Sistema Solicitudes Academicas
```
## Ejecución del sistema

Desde la carpeta raíz del proyecto, ejecutar:

```
python src/main.py
```

## Ejecución de las pruebas

Para ejecutar las pruebas automatizadas:

```
python -m unittest discover -s tests -v
```

El proyecto cuenta con seis pruebas unitarias que verifican las principales operaciones del sistema, incluyendo el registro de solicitudes, cambio de estado, asignación de responsables, búsqueda, generación de reportes y validación de estudiantes inexistentes.

## Objetivo del proyecto

Analizar y mejorar la calidad interna de un sistema existente mediante la identificación de deuda técnica y code smells, la aplicación de principios SOLID y Clean Code, y la realización de refactorings seguros, verificando que las funcionalidades originales continúen funcionando correctamente.
