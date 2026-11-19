"""
Clase abstracta para los servicios ofrecidos por Software FJ.
"""

from abc import abstractmethod

from excepciones import (
    DescuentoInvalidoError,
    ImpuestoInvalidoError,
    ServicioInvalidoError,
    ServicioNoDisponibleError,
)
from modelos.entidad import Entidad
from utilidades.configuracion_logging import configurar_logging


logger = configurar_logging()


class Servicio(Entidad):
    """
    Representa un servicio general de Software FJ.

    Las clases derivadas deben implementar los métodos
    calcular_costo, describir_servicio y validar_parametros.
    """

    def __init__(self, codigo, nombre, tarifa_base, disponible=True):
        super().__init__(codigo)

        self._nombre = self._validar_nombre(nombre)
        self._tarifa_base = self._validar_tarifa(tarifa_base)
        self._disponible = bool(disponible)

        logger.info(
            "Servicio creado: codigo=%s, tipo=%s",
            self.identificador,
            self.__class__.__name__,
        )

    @staticmethod
    def _validar_nombre(nombre):
        """Valida el nombre del servicio."""

        if not isinstance(nombre, str):
            raise ServicioInvalidoError(
                "El nombre del servicio debe ser texto."
            )

        nombre = " ".join(nombre.split())

        if len(nombre) < 3:
            raise ServicioInvalidoError(
                "El nombre del servicio debe tener al menos 3 caracteres."
            )

        return nombre

    @staticmethod
    def _validar_tarifa(tarifa):
        """Valida que una tarifa sea numérica y mayor que cero."""

        try:
            tarifa = float(tarifa)

        except (TypeError, ValueError) as error_original:
            raise ServicioInvalidoError(
                "La tarifa debe ser un valor numérico."
            ) from error_original

        if tarifa <= 0:
            raise ServicioInvalidoError(
                "La tarifa debe ser mayor que cero."
            )

        return tarifa

    @staticmethod
    def _validar_descuento(descuento):
        """Valida un descuento entre 0 y 100."""

        try:
            descuento = float(descuento)

        except (TypeError, ValueError) as error_original:
            raise DescuentoInvalidoError(
                "El descuento debe ser numérico."
            ) from error_original

        if not 0 <= descuento <= 100:
            raise DescuentoInvalidoError(
                "El descuento debe estar entre 0 y 100."
            )

        return descuento

    @staticmethod
    def _validar_impuesto(impuesto):
        """Valida un impuesto entre 0 y 100."""

        try:
            impuesto = float(impuesto)

        except (TypeError, ValueError) as error_original:
            raise ImpuestoInvalidoError(
                "El impuesto debe ser numérico."
            ) from error_original

        if not 0 <= impuesto <= 100:
            raise ImpuestoInvalidoError(
                "El impuesto debe estar entre 0 y 100."
            )

        return impuesto

    def verificar_disponibilidad(self):
        """Comprueba si el servicio está disponible."""

        if not self._disponible:
            raise ServicioNoDisponibleError(
                f"El servicio '{self._nombre}' no está disponible."
            )

        return True

    def aplicar_ajustes(self, subtotal, descuento=0, impuesto=0):
        """
        Aplica un descuento y posteriormente un impuesto.

        Esta variante con parámetros opcionales permite calcular
        costos básicos, con descuento, con impuesto o con ambos.
        """

        descuento = self._validar_descuento(descuento)
        impuesto = self._validar_impuesto(impuesto)

        valor_descuento = subtotal * descuento / 100
        subtotal_descontado = subtotal - valor_descuento
        valor_impuesto = subtotal_descontado * impuesto / 100

        return round(subtotal_descontado + valor_impuesto, 2)

    def cambiar_disponibilidad(self, disponible):
        """Cambia el estado de disponibilidad del servicio."""

        self._disponible = bool(disponible)

        logger.info(
            "Disponibilidad modificada: servicio=%s, disponible=%s",
            self.identificador,
            self._disponible,
        )

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @property
    def disponible(self):
        return self._disponible

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        """Calcula el costo del servicio."""

    @abstractmethod
    def describir_servicio(self):
        """Devuelve una descripción del servicio."""

    @abstractmethod
    def validar_parametros(self):
        """Valida los parámetros específicos del servicio."""

    def mostrar_informacion(self):
        estado = "Disponible" if self._disponible else "No disponible"

        return (
            f"Código: {self.identificador} | "
            f"Servicio: {self._nombre} | "
            f"Tarifa base: ${self._tarifa_base:,.2f} | "
            f"Estado: {estado}"
        )