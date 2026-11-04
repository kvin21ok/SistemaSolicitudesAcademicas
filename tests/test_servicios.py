import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from servicios import SolicitudesService
from modelos import NuevaSolicitud


class RepositorioPrueba:

    def __init__(self):
        self.datos = {
            "estudiantes": [
                {"id": 1, "nombre": "Juan Perez", "legajo": "1001"}
            ],
            "responsables": [
                {"id": 1, "nombre": "Administracion", "area": "Administracion"}
            ],
            "solicitudes": []
        }

    def cargar(self):
        return self.datos

    def guardar(self, datos):
        self.datos = datos


class TestSolicitudesService(unittest.TestCase):

    def setUp(self):
        self.repositorio = RepositorioPrueba()
        self.servicio = SolicitudesService(self.repositorio)

        self.nueva = NuevaSolicitud(
            estudiante_id=1,
            tipo="Academica",
            descripcion="Solicitud de equivalencia",
            prioridad="Alta"
        )

    def test_registrar_solicitud(self):
        self.servicio.registrar_solicitud(self.nueva)

        solicitudes = self.servicio.obtener_solicitudes()

        self.assertEqual(len(solicitudes), 1)
        self.assertEqual(solicitudes[0]["estado"], "Pendiente")

    def test_cambiar_estado(self):
        self.servicio.registrar_solicitud(self.nueva)
        self.servicio.cambiar_estado(1, "En proceso")

        self.assertEqual(
            self.servicio.obtener_solicitudes()[0]["estado"],
            "En proceso"
        )

    def test_asignar_responsable(self):
        self.servicio.registrar_solicitud(self.nueva)
        self.servicio.asignar_responsable(1, 1)

        self.assertEqual(
            self.servicio.obtener_solicitudes()[0]["responsable_id"],
            1
        )

    def test_buscar_solicitudes(self):
        self.servicio.registrar_solicitud(self.nueva)

        resultados = self.servicio.buscar_solicitudes("prioridad", "Alta")

        self.assertEqual(len(resultados), 1)

    def test_generar_reporte(self):
        self.servicio.registrar_solicitud(self.nueva)

        reporte = self.servicio.generar_reporte()

        self.assertEqual(reporte["total"], 1)
        self.assertEqual(reporte["por_estado"]["Pendiente"], 1)

    def test_rechazar_estudiante_inexistente(self):
        solicitud = NuevaSolicitud(
            estudiante_id=99,
            tipo="Academica",
            descripcion="Prueba",
            prioridad="Alta"
        )

        with self.assertRaises(ValueError):
            self.servicio.registrar_solicitud(solicitud)


if __name__ == "__main__":
    unittest.main()