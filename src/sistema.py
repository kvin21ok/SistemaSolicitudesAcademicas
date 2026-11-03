import json

class SistemaSolicitudes:

    def __init__(self):
        self.archivo = "data/solicitudes.json"
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.datos = json.load(f)
        except:
            self.datos = {
                "estudiantes": [],
                "responsables": [],
                "solicitudes": []
            }

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.datos, f, indent=4, ensure_ascii=False)

    def registrar_solicitud(self):
        print("\n--- REGISTRAR SOLICITUD ---")
        print("Estudiantes disponibles:")
        for e in self.datos["estudiantes"]:
            print(e["id"], "-", e["nombre"], "- Legajo:", e["legajo"])

        estudiante = int(input("ID del estudiante: "))
        existe = False
        for e in self.datos["estudiantes"]:
            if e["id"] == estudiante:
                existe = True

        if existe == False:
            print("Estudiante inexistente")
            return

        tipo = input("Tipo de solicitud (Academica/Administrativa/Tecnica): ")
        descripcion = input("Descripcion: ")
        prioridad = input("Prioridad (Baja/Media/Alta): ")

        if tipo == "" or descripcion == "" or prioridad == "":
            print("Todos los campos son obligatorios")
            return

        if prioridad != "Baja" and prioridad != "Media" and prioridad != "Alta":
            print("Prioridad incorrecta")
            return

        nuevo = {
            "id": len(self.datos["solicitudes"]) + 1,
            "estudiante_id": estudiante,
            "tipo": tipo,
            "descripcion": descripcion,
            "prioridad": prioridad,
            "estado": "Pendiente",
            "responsable_id": None
        }

        self.datos["solicitudes"].append(nuevo)
        self.guardar()
        print("Solicitud registrada correctamente")

    def cambiar_estado(self):
        print("\n--- CAMBIAR ESTADO ---")
        id_solicitud = int(input("ID de solicitud: "))
        encontrado = False

        for s in self.datos["solicitudes"]:
            if s["id"] == id_solicitud:
                encontrado = True
                print("1. Pendiente")
                print("2. En proceso")
                print("3. Resuelta")
                opcion = input("Nuevo estado: ")

                if opcion == "1":
                    s["estado"] = "Pendiente"
                elif opcion == "2":
                    s["estado"] = "En proceso"
                elif opcion == "3":
                    s["estado"] = "Resuelta"
                else:
                    print("Opcion incorrecta")
                    return

                self.guardar()
                print("Estado actualizado")
                break

        if encontrado == False:
            print("Solicitud no encontrada")

    def asignar_responsable(self):
        print("\n--- ASIGNAR RESPONSABLE ---")
        id_solicitud = int(input("ID de solicitud: "))
        encontrado = False

        for s in self.datos["solicitudes"]:
            if s["id"] == id_solicitud:
                encontrado = True
                print("Responsables disponibles:")
                for r in self.datos["responsables"]:
                    print(r["id"], "-", r["nombre"])

                id_responsable = int(input("ID del responsable: "))
                existe = False

                for r in self.datos["responsables"]:
                    if r["id"] == id_responsable:
                        existe = True

                if existe:
                    s["responsable_id"] = id_responsable
                    self.guardar()
                    print("Responsable asignado")
                else:
                    print("Responsable inexistente")
                break

        if encontrado == False:
            print("Solicitud no encontrada")

    def buscar_solicitudes(self):
        print("\n--- BUSCAR SOLICITUDES ---")
        print("1. Buscar por estado")
        print("2. Buscar por prioridad")
        print("3. Buscar por tipo")
        opcion = input("Opcion: ")

        if opcion == "1":
            valor = input("Estado: ")
            for s in self.datos["solicitudes"]:
                if s["estado"].lower() == valor.lower():
                    print(s)

        elif opcion == "2":
            valor = input("Prioridad: ")
            for s in self.datos["solicitudes"]:
                if s["prioridad"].lower() == valor.lower():
                    print(s)

        elif opcion == "3":
            valor = input("Tipo: ")
            for s in self.datos["solicitudes"]:
                if s["tipo"].lower() == valor.lower():
                    print(s)
        else:
            print("Opcion incorrecta")

    def generar_reporte(self):
        print("\n--- REPORTE DE SOLICITUDES ---")
        total = len(self.datos["solicitudes"])
        pendientes = 0
        proceso = 0
        resueltas = 0

        for s in self.datos["solicitudes"]:
            print(
                "ID:", s["id"],
                "| Tipo:", s["tipo"],
                "| Prioridad:", s["prioridad"],
                "| Estado:", s["estado"],
                "| Estudiante:", s["estudiante_id"],
                "| Responsable:", s["responsable_id"]
            )

            if s["estado"] == "Pendiente":
                pendientes += 1
            elif s["estado"] == "En proceso":
                proceso += 1
            elif s["estado"] == "Resuelta":
                resueltas += 1

        print("\nTotal:", total)
        print("Pendientes:", pendientes)
        print("En proceso:", proceso)
        print("Resueltas:", resueltas)

    def iniciar(self):
        while True:
            print("\n===== SISTEMA DE SOLICITUDES ACADEMICAS =====")
            print("1. Registrar solicitud")
            print("2. Cambiar estado")
            print("3. Asignar responsable")
            print("4. Buscar solicitudes")
            print("5. Generar reporte")
            print("0. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar_solicitud()
            elif opcion == "2":
                self.cambiar_estado()
            elif opcion == "3":
                self.asignar_responsable()
            elif opcion == "4":
                self.buscar_solicitudes()
            elif opcion == "5":
                self.generar_reporte()
            elif opcion == "0":
                print("Hasta luego")
                break
            else:
                print("Opcion incorrecta")
