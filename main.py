"""
Punto de entrada del Sistema Integral de Gestión Software FJ.
"""

from utilidades.configuracion_logging import configurar_logging


logger = configurar_logging()


def ejecutar_aplicacion():
    """Inicia la aplicación y controla posibles errores."""

    logger.info("Inicio de la aplicación Software FJ.")

    try:
        print("=" * 60)
        print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
        print("Gestión de clientes, servicios y reservas")
        print("=" * 60)

    except Exception as error:
        logger.exception(
            "Ocurrió un error inesperado durante el inicio."
        )
        print(f"Error controlado: {error}")

    else:
        logger.info("La aplicación se inició correctamente.")

    finally:
        logger.info("Finalizó el proceso de inicio.")


if __name__ == "__main__":
    ejecutar_aplicacion()