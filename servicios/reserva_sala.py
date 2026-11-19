"""
Servicio especializado para la reserva de salas.
"""

from excepciones import DuracionInvalidaError, ServicioInvalidoError
from modelos.servicio import Servicio
from utilidades.configuracion_logging import configurar_logging


logger = configurar_logging()


class ReservaSala(Servicio):
    """Representa el servicio de reserva de una sala."""

    def __init__(
        self,
        codigo,
        nombre,
        tarifa_por_hora,
        capacidad,
        tipo_sala,
        disponible=True,
    ):
        super().__init__(
            codigo=codigo,
            nombre=nombre,
            tarifa_base=tarifa_por_hora,
            disponible=disponible,
        )

        self.__capacidad = capacidad
        self.__tipo_sala = tipo_sala

        self.validar_parametros()

    def validar_parametros(self):
        """Valida la capacidad y el tipo de sala."""

        try:
            self.__capacidad = int(self.__capacidad)

        except (TypeError, ValueError) as error_original:
            raise ServicioInvalidoError(
                "La capacidad de la sala debe ser un número entero."
            ) from error_original

        if self.__capacidad <= 0:
            raise ServicioInvalidoError(
                "La capacidad de la sala debe ser mayor que cero."
            )

        if not isinstance(self.__tipo_sala, str):
            raise ServicioInvalidoError(
                "El tipo de sala debe ser texto."
            )

        self.__tipo_sala = self.__tipo_sala.strip()

        if len(self.__tipo_sala) < 3:
            raise ServicioInvalidoError(
                "El tipo de sala debe tener al menos 3 caracteres."
            )

        return True

    @staticmethod
    def _validar_horas(horas):
        """Valida la cantidad de horas de la reserva."""

        try:
            horas = float(horas)

        except (TypeError, ValueError) as error_original:
            raise DuracionInvalidaError(
                "La duración de la reserva debe ser numérica."
            ) from error_original

        if horas <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        if horas > 12:
            raise DuracionInvalidaError(
                "Una sala no puede reservarse por más de 12 horas."
            )

        return horas

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        """
        Calcula el costo de reservar la sala.

        Costo base = tarifa por hora multiplicada por las horas.
        Después se aplican el descuento y el impuesto.
        """

        self.verificar_disponibilidad()
        horas = self._validar_horas(horas)

        subtotal = self.tarifa_base * horas
        total = self.aplicar_ajustes(
            subtotal,
            descuento=descuento,
            impuesto=impuesto,
        )

        logger.info(
            "Costo de sala calculado: codigo=%s, horas=%s, total=%s",
            self.identificador,
            horas,
            total,
        )

        return total

    def describir_servicio(self):
        """Describe las características de la sala."""

        return (
            f"{self.mostrar_informacion()} | "
            f"Tipo: {self.__tipo_sala} | "
            f"Capacidad: {self.__capacidad} personas"
        )

    @property
    def capacidad(self):
        return self.__capacidad

    @property
    def tipo_sala(self):
        return self.__tipo_sala

    def __str__(self):
        return self.describir_servicio()