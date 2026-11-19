"""
Servicio especializado para asesorías profesionales de Software FJ.
"""

from excepciones import DuracionInvalidaError, ServicioInvalidoError
from modelos.servicio import Servicio
from utilidades.configuracion_logging import configurar_logging


logger = configurar_logging()


class AsesoriaEspecializada(Servicio):
    """Representa una asesoría especializada contratada por horas."""

    MODALIDADES_PERMITIDAS = {
        "presencial",
        "virtual",
        "híbrida",
    }

    def __init__(
        self,
        codigo,
        nombre,
        tarifa_por_hora,
        especialidad,
        profesional,
        modalidad="virtual",
        disponible=True,
    ):
        super().__init__(
            codigo=codigo,
            nombre=nombre,
            tarifa_base=tarifa_por_hora,
            disponible=disponible,
        )

        self.__especialidad = especialidad
        self.__profesional = profesional
        self.__modalidad = modalidad

        self.validar_parametros()

    @staticmethod
    def _validar_texto(valor, nombre_campo):
        """Valida los campos de texto de la asesoría."""

        if not isinstance(valor, str):
            raise ServicioInvalidoError(
                f"El campo {nombre_campo} debe ser texto."
            )

        valor = " ".join(valor.split())

        if len(valor) < 3:
            raise ServicioInvalidoError(
                f"El campo {nombre_campo} debe tener "
                "al menos 3 caracteres."
            )

        return valor

    def validar_parametros(self):
        """Valida los datos específicos de la asesoría."""

        self.__especialidad = self._validar_texto(
            self.__especialidad,
            "especialidad",
        )

        self.__profesional = self._validar_texto(
            self.__profesional,
            "profesional",
        )

        self.__modalidad = self._validar_texto(
            self.__modalidad,
            "modalidad",
        ).lower()

        if self.__modalidad not in self.MODALIDADES_PERMITIDAS:
            modalidades = ", ".join(
                sorted(self.MODALIDADES_PERMITIDAS)
            )

            raise ServicioInvalidoError(
                "La modalidad debe ser una de estas opciones: "
                f"{modalidades}."
            )

        return True

    @staticmethod
    def _validar_horas(horas):
        """Valida las horas contratadas para la asesoría."""

        try:
            horas = float(horas)

        except (TypeError, ValueError) as error_original:
            raise DuracionInvalidaError(
                "La duración de la asesoría debe ser numérica."
            ) from error_original

        if horas <= 0:
            raise DuracionInvalidaError(
                "Las horas de asesoría deben ser mayores que cero."
            )

        if horas > 40:
            raise DuracionInvalidaError(
                "Una asesoría no puede superar las 40 horas."
            )

        return horas

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        """
        Calcula el costo de la asesoría.

        El subtotal corresponde a la tarifa por hora multiplicada
        por las horas contratadas.
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
            "Costo de asesoría calculado: codigo=%s, horas=%s, total=%s",
            self.identificador,
            horas,
            total,
        )

        return total

    def describir_servicio(self):
        """Devuelve la información completa de la asesoría."""

        return (
            f"{self.mostrar_informacion()} | "
            f"Especialidad: {self.__especialidad} | "
            f"Profesional: {self.__profesional} | "
            f"Modalidad: {self.__modalidad.title()}"
        )

    @property
    def especialidad(self):
        return self.__especialidad

    @property
    def profesional(self):
        return self.__profesional

    @property
    def modalidad(self):
        return self.__modalidad

    def __str__(self):
        return self.describir_servicio()