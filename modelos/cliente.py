"""
Modelo de cliente para el sistema Software FJ.

La clase aplica herencia, encapsulación y validaciones robustas
sobre los datos personales.
"""

import re

from excepciones import (
    ClienteInvalidoError,
    CorreoInvalidoError,
    DocumentoInvalidoError,
)
from modelos.entidad import Entidad
from utilidades.configuracion_logging import configurar_logging


logger = configurar_logging()


class Cliente(Entidad):
    """Representa un cliente registrado en Software FJ."""

    PATRON_CORREO = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def __init__(self, nombre, documento, correo, telefono):
        """
        Inicializa y valida los datos del cliente.

        Args:
            nombre: Nombre completo del cliente.
            documento: Número de identificación.
            correo: Correo electrónico.
            telefono: Número telefónico.
        """

        documento_validado = self._validar_documento(documento)
        super().__init__(documento_validado)

        self.__nombre = self._validar_nombre(nombre)
        self.__documento = documento_validado
        self.__correo = self._validar_correo(correo)
        self.__telefono = self._validar_telefono(telefono)

        logger.info(
            "Cliente creado correctamente: documento=%s",
            self.__documento,
        )

    @staticmethod
    def _validar_nombre(nombre):
        """Valida que el nombre contenga únicamente caracteres válidos."""

        if not isinstance(nombre, str):
            raise ClienteInvalidoError(
                "El nombre debe ser una cadena de texto."
            )

        nombre = " ".join(nombre.split())

        if len(nombre) < 3:
            raise ClienteInvalidoError(
                "El nombre debe tener al menos 3 caracteres."
            )

        if not all(
            caracter.isalpha() or caracter in " '-"
            for caracter in nombre
        ):
            raise ClienteInvalidoError(
                "El nombre contiene caracteres no permitidos."
            )

        return nombre.title()

    @staticmethod
    def _validar_documento(documento):
        """Valida que el documento tenga entre 6 y 12 dígitos."""

        documento = str(documento).strip()

        if not documento.isdigit():
            raise DocumentoInvalidoError(
                "El documento debe contener únicamente números."
            )

        if not 6 <= len(documento) <= 12:
            raise DocumentoInvalidoError(
                "El documento debe tener entre 6 y 12 dígitos."
            )

        return documento

    @classmethod
    def _validar_correo(cls, correo):
        """Valida el formato del correo electrónico."""

        if not isinstance(correo, str):
            raise CorreoInvalidoError(
                "El correo debe ser una cadena de texto."
            )

        correo = correo.strip().lower()

        if not cls.PATRON_CORREO.fullmatch(correo):
            raise CorreoInvalidoError(
                "El formato del correo electrónico no es válido."
            )

        return correo

    @staticmethod
    def _validar_telefono(telefono):
        """Valida que el teléfono tenga entre 7 y 15 dígitos."""

        telefono = str(telefono).strip()
        telefono_normalizado = (
            telefono.replace(" ", "")
            .replace("-", "")
            .replace("+", "")
        )

        if not telefono_normalizado.isdigit():
            raise ClienteInvalidoError(
                "El teléfono contiene caracteres no permitidos."
            )

        if not 7 <= len(telefono_normalizado) <= 15:
            raise ClienteInvalidoError(
                "El teléfono debe tener entre 7 y 15 dígitos."
            )

        return telefono

    @property
    def nombre(self):
        """Devuelve el nombre del cliente."""
        return self.__nombre

    @property
    def documento(self):
        """Devuelve el documento del cliente."""
        return self.__documento

    @property
    def correo(self):
        """Devuelve el correo del cliente."""
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        """Actualiza el correo después de validarlo."""
        correo_anterior = self.__correo
        self.__correo = self._validar_correo(nuevo_correo)

        logger.info(
            "Correo actualizado para documento=%s: %s -> %s",
            self.__documento,
            correo_anterior,
            self.__correo,
        )

    @property
    def telefono(self):
        """Devuelve el teléfono del cliente."""
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        """Actualiza el teléfono después de validarlo."""
        self.__telefono = self._validar_telefono(nuevo_telefono)

        logger.info(
            "Teléfono actualizado para documento=%s",
            self.__documento,
        )

    def mostrar_informacion(self):
        """Devuelve una representación segura del cliente."""

        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

    def __str__(self):
        return self.mostrar_informacion()