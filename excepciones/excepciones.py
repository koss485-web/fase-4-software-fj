"""
Excepciones personalizadas del sistema Software FJ.

Estas clases permiten identificar y controlar los errores
específicos que pueden presentarse durante la ejecución.
"""


class SistemaFJError(Exception):
    """Clase base para todas las excepciones del sistema."""


class ClienteInvalidoError(SistemaFJError):
    """Se genera cuando los datos de un cliente no son válidos."""


class DocumentoInvalidoError(ClienteInvalidoError):
    """Se genera cuando el documento del cliente no es válido."""


class CorreoInvalidoError(ClienteInvalidoError):
    """Se genera cuando el correo electrónico no es válido."""


class ServicioInvalidoError(SistemaFJError):
    """Se genera cuando los datos de un servicio son incorrectos."""


class ServicioNoDisponibleError(SistemaFJError):
    """Se genera cuando un servicio no se encuentra disponible."""


class DuracionInvalidaError(SistemaFJError):
    """Se genera cuando la duración indicada no es válida."""


class ReservaInvalidaError(SistemaFJError):
    """Se genera cuando una reserva contiene información inválida."""


class OperacionNoPermitidaError(SistemaFJError):
    """Se genera cuando se intenta realizar una operación no permitida."""


class CalculoCostoError(SistemaFJError):
    """Se genera cuando ocurre un error al calcular el costo."""


class DescuentoInvalidoError(CalculoCostoError):
    """Se genera cuando el porcentaje de descuento no es válido."""


class ImpuestoInvalidoError(CalculoCostoError):
    """Se genera cuando el porcentaje de impuesto no es válido."""