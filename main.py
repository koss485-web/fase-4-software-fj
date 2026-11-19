"""
Punto de entrada del Sistema Integral de Gestión Software FJ.
"""

from excepciones import SistemaFJError
from modelos import Cliente
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
        logger.error("Error controlado al crear el cliente: %s", error)
        print(f"Resultado esperado: {error}")

    else:
        logger.info("El cliente de prueba fue creado correctamente.")

    finally:
        logger.info("Finalizó la prueba del cliente inválido.")


def ejecutar_aplicacion():
    """Ejecuta las primeras simulaciones del sistema."""

    logger.info("Inicio de la aplicación Software FJ.")

    try:
        print("=" * 60)
        print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
        print("Gestión de clientes, servicios y reservas")
        print("=" * 60)

        probar_cliente_valido()
        probar_cliente_invalido()

    except SistemaFJError as error:
        logger.error("Error controlado del sistema: %s", error)
        print(f"Error controlado: {error}")

    except Exception:
        logger.exception("Ocurrió un error inesperado.")
        print("Ocurrió un error inesperado. Consulte el archivo de logs.")

    else:
        logger.info("Las pruebas iniciales finalizaron correctamente.")

    finally:
        logger.info("Finalizó la ejecución de la aplicación.")


if __name__ == "__main__":
    ejecutar_aplicacion()