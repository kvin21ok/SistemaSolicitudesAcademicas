from dataclasses import dataclass


@dataclass
class Estudiante:
    id: int
    nombre: str
    legajo: str


@dataclass
class Responsable:
    id: int
    nombre: str
    area: str


@dataclass
class NuevaSolicitud:
    estudiante_id: int
    tipo: str
    descripcion: str
    prioridad: str


@dataclass
class Solicitud:
    id: int
    estudiante_id: int
    tipo: str
    descripcion: str
    prioridad: str
    estado: str = "Pendiente"
    responsable_id: int | None = None

    def to_dict(self):
        return {
            "id": self.id,
            "estudiante_id": self.estudiante_id,
            "tipo": self.tipo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad,
            "estado": self.estado,
            "responsable_id": self.responsable_id
        }