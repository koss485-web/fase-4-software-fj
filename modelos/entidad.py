"""
Clase abstracta base para las entidades del sistema Software FJ.
"""

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Representa una entidad general del sistema.

    Esta clase no puede instanciarse directamente. Sus clases
    derivadas deben implementar el método mostrar_informacion.
    """

    def __init__(self, identificador):
        if identificador is None:
            raise ValueError("El identificador no puede ser nulo.")

        identificador = str(identificador).strip()

        if not identificador:
            raise ValueError("El identificador no puede estar vacío.")

        self._identificador = identificador

    @property
    def identificador(self):
        """Devuelve el identificador de la entidad."""
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Devuelve la información principal de la entidad."""