"""
Punto de entrada del Sistema Integral de Gestión Software FJ.

Este archivo ejecuta simulaciones válidas e inválidas para comprobar
clientes, reservas de salas, alquileres de equipos y asesorías.
"""

from excepciones import SistemaFJError
from modelos import Cliente
from servicios import (
    AlquilerEquipo,
    AsesoriaEspecializada,
    ReservaSala,
)
from utilidades.configuracion_logging import configurar_logging


logger = configurar_logging()


def probar_cliente_valido():
    """Crea un cliente con información correcta."""

    cliente = Cliente(
        nombre="Juan Sebastian Rojas Badillo",
        documento="1234567890",
        correo="juan.rojas@email.com",
        telefono="3001234567",
    )

    print("\nPRUEBA 1: CLIENTE VÁLIDO")
    print(cliente)


def probar_cliente_invalido():
    """Intenta crear un cliente con un correo incorrecto."""

    print("\nPRUEBA 2: CLIENTE INVÁLIDO")

    try:
        Cliente(
            nombre="Cliente de prueba",
            documento="987654321",
            correo="correo-invalido",
            telefono="3109876543",
        )

    except SistemaFJError as error:
        logger.error(
            "Error controlado al crear el cliente: %s",
            error,
        )
        print(f"Resultado esperado: {error}")

    else:
        logger.info(
            "El cliente de prueba fue creado correctamente."
        )

    finally:
        logger.info(
            "Finalizó la prueba del cliente inválido."
        )


def probar_reserva_sala_valida():
    """Crea una sala y calcula correctamente su costo."""

    print("\nPRUEBA 3: RESERVA DE SALA VÁLIDA")

    sala = ReservaSala(
        codigo="SAL-001",
        nombre="Sala ejecutiva",
        tarifa_por_hora=50000,
        capacidad=20,
        tipo_sala="Ejecutiva",
    )

    costo = sala.calcular_costo(
        horas=3,
        descuento=10,
        impuesto=19,
    )

    print(sala)
    print(f"Costo total: ${costo:,.2f}")


def probar_reserva_sala_invalida():
    """Intenta calcular una reserva con duración negativa."""

    print("\nPRUEBA 4: RESERVA DE SALA INVÁLIDA")

    try:
        sala = ReservaSala(
            codigo="SAL-002",
            nombre="Sala de capacitación",
            tarifa_por_hora=40000,
            capacidad=30,
            tipo_sala="Capacitación",
        )

        sala.calcular_costo(horas=-2)

    except SistemaFJError as error:
        logger.error(
            "Error controlado en reserva de sala: %s",
            error,
        )
        print(f"Resultado esperado: {error}")

    else:
        logger.info(
            "La reserva de sala fue procesada correctamente."
        )

    finally:
        logger.info(
            "Finalizó la prueba de reserva de sala inválida."
        )


def probar_alquiler_equipo_valido():
    """Crea un equipo y calcula correctamente su alquiler."""

    print("\nPRUEBA 5: ALQUILER DE EQUIPO VÁLIDO")

    equipo = AlquilerEquipo(
        codigo="EQU-001",
        nombre="Computador portátil empresarial",
        tarifa_por_dia=80000,
        tipo_equipo="Computador portátil",
        marca="Lenovo",
        estado_equipo="excelente",
    )

    costo = equipo.calcular_costo(
        dias=5,
        descuento=5,
        impuesto=19,
    )

    print(equipo)
    print(f"Costo total: ${costo:,.2f}")


def probar_alquiler_equipo_invalido():
    """Intenta alquilar un equipo durante cero días."""

    print("\nPRUEBA 6: ALQUILER DE EQUIPO INVÁLIDO")

    try:
        equipo = AlquilerEquipo(
            codigo="EQU-002",
            nombre="Proyector multimedia",
            tarifa_por_dia=60000,
            tipo_equipo="Proyector",
            marca="Epson",
            estado_equipo="bueno",
        )

        equipo.calcular_costo(dias=0)

    except SistemaFJError as error:
        logger.error(
            "Error controlado en alquiler de equipo: %s",
            error,
        )
        print(f"Resultado esperado: {error}")

    else:
        logger.info(
            "El alquiler del equipo se procesó correctamente."
        )

    finally:
        logger.info(
            "Finalizó la prueba de alquiler de equipo inválido."
        )


def probar_asesoria_valida():
    """Crea una asesoría y calcula correctamente su costo."""

    print("\nPRUEBA 7: ASESORÍA ESPECIALIZADA VÁLIDA")

    asesoria = AsesoriaEspecializada(
        codigo="ASE-001",
        nombre="Asesoría en arquitectura de software",
        tarifa_por_hora=120000,
        especialidad="Arquitectura de software",
        profesional="Laura Martinez",
        modalidad="virtual",
    )

    costo = asesoria.calcular_costo(
        horas=4,
        descuento=10,
        impuesto=19,
    )

    print(asesoria)
    print(f"Costo total: ${costo:,.2f}")


def probar_asesoria_invalida():
    """Intenta crear una asesoría con modalidad incorrecta."""

    print("\nPRUEBA 8: ASESORÍA ESPECIALIZADA INVÁLIDA")

    try:
        AsesoriaEspecializada(
            codigo="ASE-002",
            nombre="Asesoría en seguridad informática",
            tarifa_por_hora=150000,
            especialidad="Seguridad informática",
            profesional="Carlos Ramirez",
            modalidad="telepática",
        )

    except SistemaFJError as error:
        logger.error(
            "Error controlado en asesoría: %s",
            error,
        )
        print(f"Resultado esperado: {error}")

    else:
        logger.info(
            "La asesoría fue creada correctamente."
        )

    finally:
        logger.info(
            "Finalizó la prueba de asesoría inválida."
        )


def ejecutar_aplicacion():
    """Ejecuta secuencialmente las simulaciones del sistema."""

    logger.info("Inicio de la aplicación Software FJ.")

    try:
        print("=" * 60)
        print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
        print("Gestión de clientes, servicios y reservas")
        print("=" * 60)

        probar_cliente_valido()
        probar_cliente_invalido()
        probar_reserva_sala_valida()
        probar_reserva_sala_invalida()
        probar_alquiler_equipo_valido()
        probar_alquiler_equipo_invalido()
        probar_asesoria_valida()
        probar_asesoria_invalida()

    except SistemaFJError as error:
        logger.error(
            "Error controlado del sistema: %s",
            error,
        )
        print(f"Error controlado: {error}")

    except Exception:
        logger.exception(
            "Ocurrió un error inesperado."
        )
        print(
            "Ocurrió un error inesperado. "
            "Consulte el archivo de logs."
        )

    else:
        logger.info(
            "Las pruebas finalizaron correctamente."
        )

    finally:
        logger.info(
            "Finalizó la ejecución de la aplicación."
        )


if __name__ == "__main__":
    ejecutar_aplicacion()
    