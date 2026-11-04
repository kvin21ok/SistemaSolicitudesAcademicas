from modelos import NuevaSolicitud


class InterfazConsola:

    def __init__(self, servicio):
        self.servicio = servicio

    def _leer_entero(self, mensaje):
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número válido.")
            return None

    def _mostrar_solicitudes(self, solicitudes):
        if not solicitudes:
            print("No se encontraron solicitudes.")
            return

        for s in solicitudes:
            print(
                f"ID: {s['id']} | Tipo: {s['tipo']} | "
                f"Prioridad: {s['prioridad']} | Estado: {s['estado']} | "
                f"Estudiante: {s['estudiante_id']} | "
                f"Responsable: {s['responsable_id']}"
            )

    def registrar_solicitud(self):
        print("\n--- REGISTRAR SOLICITUD ---")

        for e in self.servicio.obtener_estudiantes():
            print(e["id"], "-", e["nombre"], "- Legajo:", e["legajo"])

        estudiante_id = self._leer_entero("ID del estudiante: ")

        if estudiante_id is None:
            return

        tipo = input("Tipo de solicitud: ")
        descripcion = input("Descripción: ")
        prioridad = input("Prioridad (Baja/Media/Alta): ")

        try:
            nueva = NuevaSolicitud(
                estudiante_id,
                tipo,
                descripcion,
                prioridad
            )

            self.servicio.registrar_solicitud(nueva)
            print("Solicitud registrada correctamente.")

        except ValueError as error:
            print(error)

    def cambiar_estado(self):
        print("\n--- CAMBIAR ESTADO ---")

        id_solicitud = self._leer_entero("ID de solicitud: ")

        if id_solicitud is None:
            return

        print("1. Pendiente")
        print("2. En proceso")
        print("3. Resuelta")

        opciones = {
            "1": "Pendiente",
            "2": "En proceso",
            "3": "Resuelta"
        }

        opcion = input("Nuevo estado: ")

        try:
            estado = opciones.get(opcion)

            if estado is None:
                raise ValueError("Opción incorrecta.")

            self.servicio.cambiar_estado(id_solicitud, estado)
            print("Estado actualizado correctamente.")

        except ValueError as error:
            print(error)

    def asignar_responsable(self):
        print("\n--- ASIGNAR RESPONSABLE ---")

        id_solicitud = self._leer_entero("ID de solicitud: ")

        if id_solicitud is None:
            return

        for r in self.servicio.obtener_responsables():
            print(r["id"], "-", r["nombre"])

        id_responsable = self._leer_entero("ID del responsable: ")

        if id_responsable is None:
            return

        try:
            self.servicio.asignar_responsable(
                id_solicitud,
                id_responsable
            )
            print("Responsable asignado correctamente.")

        except ValueError as error:
            print(error)

    def buscar_solicitudes(self):
        print("\n--- BUSCAR SOLICITUDES ---")
        print("1. Buscar por estado")
        print("2. Buscar por prioridad")
        print("3. Buscar por tipo")

        opciones = {
            "1": "estado",
            "2": "prioridad",
            "3": "tipo"
        }

        opcion = input("Opción: ")
        criterio = opciones.get(opcion)

        if criterio is None:
            print("Opción incorrecta.")
            return

        valor = input(f"Ingrese {criterio}: ")

        try:
            resultados = self.servicio.buscar_solicitudes(
                criterio,
                valor
            )
            self._mostrar_solicitudes(resultados)

        except ValueError as error:
            print(error)

    def generar_reporte(self):
        print("\n--- REPORTE DE SOLICITUDES ---")

        reporte = self.servicio.generar_reporte()

        self._mostrar_solicitudes(reporte["solicitudes"])

        print("\nTotal:", reporte["total"])

        for estado, cantidad in reporte["por_estado"].items():
            print(f"{estado}: {cantidad}")

    def iniciar(self):
        opciones = {
            "1": self.registrar_solicitud,
            "2": self.cambiar_estado,
            "3": self.asignar_responsable,
            "4": self.buscar_solicitudes,
            "5": self.generar_reporte
        }

        while True:
            print("\n===== SISTEMA DE SOLICITUDES ACADEMICAS =====")
            print("1. Registrar solicitud")
            print("2. Cambiar estado")
            print("3. Asignar responsable")
            print("4. Buscar solicitudes")
            print("5. Generar reporte")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                print("Hasta luego.")
                break

            accion = opciones.get(opcion)

            if accion:
                accion()
            else:
                print("Opción incorrecta.")