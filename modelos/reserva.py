"""
Modelo de reserva del sistema Software FJ.

Una reserva relaciona un cliente con un servicio y controla
su procesamiento, confirmación, cancelación y costo total.
"""

from excepciones import (
    OperacionNoPermitidaError,
    ReservaInvalidaError,
)
from modelos.cliente import Cliente
from modelos.entidad import Entidad
from modelos.servicio import Servicio
from utilidades.configuracion_logging import configurar_logging


logger = configurar_logging()


class Reserva(Entidad):
    """Representa una reserva realizada por un cliente."""

    ESTADO_PENDIENTE = "pendiente"
    ESTADO_CONFIRMADA = "confirmada"
    ESTADO_CANCELADA = "cancelada"
    ESTADO_PROCESADA = "procesada"

    def __init__(
        self,
        codigo,
        cliente,
        servicio,
        duracion,
        descuento=0,
        impuesto=0,
    ):
        super().__init__(codigo)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__descuento = descuento
        self.__impuesto = impuesto
        self.__estado = self.ESTADO_PENDIENTE
        self.__costo_total = 0.0

        self._validar_datos()

        logger.info(
            "Reserva creada: codigo=%s, cliente=%s, servicio=%s",
            self.identificador,
            self.__cliente.documento,
            self.__servicio.identificador,
        )

    def _validar_datos(self):
        """Valida los objetos y datos principales de la reserva."""

        if not isinstance(self.__cliente, Cliente):
            raise ReservaInvalidaError(
                "La reserva debe estar asociada a un cliente válido."
            )

        if not isinstance(self.__servicio, Servicio):
            raise ReservaInvalidaError(
                "La reserva debe estar asociada a un servicio válido."
            )

        if self.__duracion is None:
            raise ReservaInvalidaError(
                "La duración de la reserva es obligatoria."
            )

        return True

    def procesar(self):
        """
        Verifica la disponibilidad y calcula el costo de la reserva.

        El método calcular_costo se ejecuta de forma polimórfica:
        cada servicio aplica su propio cálculo.
        """

        if self.__estado != self.ESTADO_PENDIENTE:
            raise OperacionNoPermitidaError(
                "Solo se pueden procesar reservas pendientes."
            )

        try:
            self.__servicio.verificar_disponibilidad()

            self.__costo_total = self.__servicio.calcular_costo(
                self.__duracion,
                descuento=self.__descuento,
                impuesto=self.__impuesto,
            )

        except Exception as error_original:
            logger.error(
                "No fue posible procesar la reserva %s: %s",
                self.identificador,
                error_original,
            )

            raise ReservaInvalidaError(
                f"No fue posible procesar la reserva: {error_original}"
            ) from error_original

        else:
            self.__estado = self.ESTADO_PROCESADA

            logger.info(
                "Reserva procesada: codigo=%s, costo=%s",
                self.identificador,
                self.__costo_total,
            )

            return self.__costo_total

        finally:
            logger.info(
                "Finalizó el procesamiento de la reserva %s",
                self.identificador,
            )

    def confirmar(self):
        """Confirma una reserva previamente procesada."""

        if self.__estado == self.ESTADO_CANCELADA:
            raise OperacionNoPermitidaError(
                "No se puede confirmar una reserva cancelada."
            )

        if self.__estado == self.ESTADO_CONFIRMADA:
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra confirmada."
            )

        if self.__estado != self.ESTADO_PROCESADA:
            raise OperacionNoPermitidaError(
                "La reserva debe procesarse antes de confirmarla."
            )

        self.__estado = self.ESTADO_CONFIRMADA
        self.__servicio.cambiar_disponibilidad(False)

        logger.info(
            "Reserva confirmada: codigo=%s",
            self.identificador,
        )

        return True

    def cancelar(self):
        """Cancela una reserva y libera el servicio."""

        if self.__estado == self.ESTADO_CANCELADA:
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        estado_anterior = self.__estado
        self.__estado = self.ESTADO_CANCELADA

        if estado_anterior == self.ESTADO_CONFIRMADA:
            self.__servicio.cambiar_disponibilidad(True)

        logger.info(
            "Reserva cancelada: codigo=%s, estado_anterior=%s",
            self.identificador,
            estado_anterior,
        )

        return True

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo_total(self):
        return self.__costo_total

    def mostrar_informacion(self):
        """Devuelve la información principal de la reserva."""

        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duración: {self.__duracion} | "
            f"Estado: {self.__estado.title()} | "
            f"Costo: ${self.__costo_total:,.2f}"
        )

    def __str__(self):
        return self.mostrar_informacion()