# Decisiones técnicas

## Lenguaje y tecnologías

Se decidió mantener Python como lenguaje de programación, ya que era la tecnología utilizada por el sistema base y permite realizar las mejoras necesarias sin cambiar la plataforma.

Se utilizaron las siguientes herramientas y recursos:

- Python.
- Programación Orientada a Objetos.
- Dataclasses para representar estructuras de datos.
- Protocol para definir abstracciones.
- Archivos JSON para persistencia.
- unittest para pruebas automatizadas.
- Git y GitHub para el control de versiones.

## Persistencia de datos

Se decidió conservar los archivos JSON como mecanismo de almacenamiento para mantener la compatibilidad con la versión inicial y evitar incorporar una base de datos que no era necesaria para el alcance del trabajo.

La responsabilidad de lectura y escritura se concentró en la clase `AlmacenamientoJSON`.

## Separación de responsabilidades

Se decidió dividir el sistema en componentes con responsabilidades específicas:

- `modelos.py`: define las estructuras de datos.
- `almacenamiento.py`: gestiona la persistencia JSON.
- `servicios.py`: concentra las operaciones y reglas de negocio.
- `interfaz.py`: gestiona la interacción con el usuario.
- `sistema.py`: coordina los componentes.
- `main.py`: inicia la aplicación.

Esta organización permite modificar una parte del sistema sin afectar directamente a las demás.

## Abstracción del repositorio

Se incorporó `RepositorioSolicitudes`, definido mediante Protocol, para establecer un contrato de operaciones de carga y guardado.

Esto permite desacoplar la lógica de negocio del mecanismo concreto de almacenamiento y facilita la utilización de repositorios alternativos, por ejemplo, uno en memoria para las pruebas.

## Introducción de objetos de datos

Se incorporaron dataclasses para representar las entidades principales y se creó `NuevaSolicitud` como objeto de parámetros.

Esta última decisión permite agrupar los datos necesarios para registrar una solicitud y evitar recibir múltiples parámetros independientes.

## Validaciones y manejo de errores

Se incorporaron validaciones para controlar:

- La existencia del estudiante.
- La obligatoriedad del tipo y la descripción.
- Los valores permitidos de prioridad y estado.
- La existencia de solicitudes y responsables.
- Los errores de lectura del archivo JSON.

Se utilizaron excepciones específicas para informar los problemas detectados.

## Pruebas

Se decidió utilizar `unittest`, incluido en la biblioteca estándar de Python, para verificar las operaciones principales del servicio sin depender del archivo JSON real.

Se implementó un repositorio en memoria para aislar las pruebas de la persistencia y facilitar su ejecución.

## Control de versiones

Se utilizó Git y GitHub para registrar la evolución del proyecto mediante commits y tags.

Se conservaron dos estados generales:

- `estado-inicial`: identifica la versión original del sistema.
- `estadorefactorizado`: identificará la versión final.

También se incorporaron tags específicos para identificar los hitos de diagnóstico, refactorización, pruebas y documentación.