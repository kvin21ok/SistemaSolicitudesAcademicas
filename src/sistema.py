from almacenamiento import AlmacenamientoJSON
from servicios import SolicitudesService
from interfaz import InterfazConsola


class SistemaSolicitudes:

    def __init__(self):
        repositorio = AlmacenamientoJSON("data/solicitudes.json")
        servicio = SolicitudesService(repositorio)
        self.interfaz = InterfazConsola(servicio)

    def iniciar(self):
        self.interfaz.iniciar()