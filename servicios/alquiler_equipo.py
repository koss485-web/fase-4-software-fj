"""
Servicio especializado para el alquiler de equipos.
"""

from excepciones import DuracionInvalidaError, ServicioInvalidoError
from modelos.servicio import Servicio
from utilidades.configuracion_logging import configurar_logging


logger = configurar_logging()


class AlquilerEquipo(Servicio):
    """Representa el servicio de alquiler de un equipo."""

    ESTADOS_PERMITIDOS = {
        "nuevo",
        "excelente",
        "bueno",
        "regular",
    }

    def __init__(
        self,
        codigo,
        nombre,
        tarifa_por_dia,
        tipo_equipo,
        marca,
        estado_equipo="bueno",
        disponible=True,
    ):
        super().__init__(
            codigo=codigo,
            nombre=nombre,
            tarifa_base=tarifa_por_dia,
            disponible=disponible,
        )

        self.__tipo_equipo = tipo_equipo
        self.__marca = marca
        self.__estado_equipo = estado_equipo

        self.validar_parametros()

    @staticmethod
    def _validar_texto(valor, nombre_campo):
        """Valida los campos de texto del equipo."""

        if not isinstance(valor, str):
            raise ServicioInvalidoError(
                f"El campo {nombre_campo} debe ser texto."
            )

        valor = " ".join(valor.split())

        if len(valor) < 2:
            raise ServicioInvalidoError(
                f"El campo {nombre_campo} debe tener al menos "
                "2 caracteres."
            )

        return valor

    def validar_parametros(self):
        """Valida los datos específicos del equipo."""

        self.__tipo_equipo = self._validar_texto(
            self.__tipo_equipo,
            "tipo de equipo",
        )

        self.__marca = self._validar_texto(
            self.__marca,
            "marca",
        )

        self.__estado_equipo = self._validar_texto(
            self.__estado_equipo,
            "estado del equipo",
        ).lower()

        if self.__estado_equipo not in self.ESTADOS_PERMITIDOS:
            estados = ", ".join(sorted(self.ESTADOS_PERMITIDOS))

            raise ServicioInvalidoError(
                f"El estado del equipo debe ser uno de estos: {estados}."
            )

        return True

    @staticmethod
    def _validar_dias(dias):
        """Valida la cantidad de días del alquiler."""

        try:
            dias = int(dias)

        except (TypeError, ValueError) as error_original:
            raise DuracionInvalidaError(
                "La duración del alquiler debe ser un número entero."
            ) from error_original

        if dias <= 0:
            raise DuracionInvalidaError(
                "La cantidad de días debe ser mayor que cero."
            )

        if dias > 30:
            raise DuracionInvalidaError(
                "Un equipo no puede alquilarse por más de 30 días."
            )

        return dias

    def calcular_costo(self, dias, descuento=0, impuesto=0):
        """
        Calcula el costo del alquiler.

        El subtotal se obtiene multiplicando la tarifa diaria
        por la cantidad de días.
        """

        self.verificar_disponibilidad()
        dias = self._validar_dias(dias)

        subtotal = self.tarifa_base * dias

        total = self.aplicar_ajustes(
            subtotal,
            descuento=descuento,
            impuesto=impuesto,
        )

        logger.info(
            "Costo de equipo calculado: codigo=%s, dias=%s, total=%s",
            self.identificador,
            dias,
            total,
        )

        return total

    def describir_servicio(self):
        """Devuelve la información completa del equipo."""

        return (
            f"{self.mostrar_informacion()} | "
            f"Tipo: {self.__tipo_equipo} | "
            f"Marca: {self.__marca} | "
            f"Condición: {self.__estado_equipo.title()}"
        )

    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    @property
    def marca(self):
        return self.__marca

    @property
    def estado_equipo(self):
        return self.__estado_equipo

    def __str__(self):
        return self.describir_servicio()
    