from modelos import Solicitud, NuevaSolicitud
from almacenamiento import RepositorioSolicitudes


class SolicitudesService:

    ESTADOS = ["Pendiente", "En proceso", "Resuelta"]
    PRIORIDADES = ["Baja", "Media", "Alta"]

    def __init__(self, repositorio: RepositorioSolicitudes):
        self.repositorio = repositorio
        self.datos = repositorio.cargar()

    def _guardar(self):
        self.repositorio.guardar(self.datos)

    def _buscar_solicitud(self, id_solicitud):
        for solicitud in self.datos["solicitudes"]:
            if solicitud["id"] == id_solicitud:
                return solicitud
        return None

    def obtener_estudiantes(self):
        return self.datos["estudiantes"]

    def obtener_responsables(self):
        return self.datos["responsables"]

    def obtener_solicitudes(self):
        return self.datos["solicitudes"]

    def registrar_solicitud(self, nueva: NuevaSolicitud):
        if not any(
            e["id"] == nueva.estudiante_id
            for e in self.datos["estudiantes"]
        ):
            raise ValueError("Estudiante inexistente.")

        if not nueva.tipo.strip() or not nueva.descripcion.strip():
            raise ValueError("El tipo y la descripción son obligatorios.")

        if nueva.prioridad not in self.PRIORIDADES:
            raise ValueError("Prioridad incorrecta.")

        nuevo_id = max(
            (s["id"] for s in self.datos["solicitudes"]),
            default=0
        ) + 1

        solicitud = Solicitud(
            id=nuevo_id,
            estudiante_id=nueva.estudiante_id,
            tipo=nueva.tipo.strip(),
            descripcion=nueva.descripcion.strip(),
            prioridad=nueva.prioridad
        )

        self.datos["solicitudes"].append(solicitud.to_dict())
        self._guardar()

    def cambiar_estado(self, id_solicitud, nuevo_estado):
        solicitud = self._buscar_solicitud(id_solicitud)

        if solicitud is None:
            raise ValueError("Solicitud no encontrada.")

        if nuevo_estado not in self.ESTADOS:
            raise ValueError("Estado incorrecto.")

        solicitud["estado"] = nuevo_estado
        self._guardar()

    def asignar_responsable(self, id_solicitud, id_responsable):
        solicitud = self._buscar_solicitud(id_solicitud)

        if solicitud is None:
            raise ValueError("Solicitud no encontrada.")

        responsable_existe = any(
            r["id"] == id_responsable
            for r in self.datos["responsables"]
        )

        if not responsable_existe:
            raise ValueError("Responsable inexistente.")

        solicitud["responsable_id"] = id_responsable
        self._guardar()

    def buscar_solicitudes(self, criterio, valor):
        campos = {
            "estado": "estado",
            "prioridad": "prioridad",
            "tipo": "tipo"
        }

        if criterio not in campos:
            raise ValueError("Criterio de búsqueda incorrecto.")

        campo = campos[criterio]

        return [
            s for s in self.datos["solicitudes"]
            if str(s[campo]).lower() == valor.lower()
        ]

    def generar_reporte(self):
        solicitudes = self.datos["solicitudes"]

        cantidades = {
            estado: sum(
                1 for s in solicitudes if s["estado"] == estado
            )
            for estado in self.ESTADOS
        }

        return {
            "solicitudes": solicitudes,
            "total": len(solicitudes),
            "por_estado": cantidades
        }