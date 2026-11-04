import json
from typing import Protocol


class RepositorioSolicitudes(Protocol):

    def cargar(self) -> dict:
        ...

    def guardar(self, datos: dict) -> None:
        ...


class AlmacenamientoJSON:

    def __init__(self, archivo):
        self.archivo = archivo

    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)

        except FileNotFoundError:
            return {
                "estudiantes": [],
                "responsables": [],
                "solicitudes": []
            }

        except json.JSONDecodeError as error:
            raise ValueError("El archivo JSON contiene datos inválidos.") from error

    def guardar(self, datos):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)