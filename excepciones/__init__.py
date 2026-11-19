"""Paquete de excepciones personalizadas de Software FJ."""

from excepciones.excepciones import (
    SistemaFJError,
    ClienteInvalidoError,
    DocumentoInvalidoError,
    CorreoInvalidoError,
    ServicioInvalidoError,
    ServicioNoDisponibleError,
    DuracionInvalidaError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    CalculoCostoError,
    DescuentoInvalidoError,
    ImpuestoInvalidoError,
)

__all__ = [
    "SistemaFJError",
    "ClienteInvalidoError",
    "DocumentoInvalidoError",
    "CorreoInvalidoError",
    "ServicioInvalidoError",
    "ServicioNoDisponibleError",
    "DuracionInvalidaError",
    "ReservaInvalidaError",
    "OperacionNoPermitidaError",
    "CalculoCostoError",
    "DescuentoInvalidoError",
    "ImpuestoInvalidoError",
]