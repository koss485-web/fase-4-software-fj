"""
Configuración del sistema de registros de Software FJ.

Los eventos y errores se guardan en el archivo logs/sistema.log
y también se muestran en la terminal.
"""

import logging
from pathlib import Path


def configurar_logging():
    """
    Configura y devuelve el logger principal del sistema.

    Returns:
        logging.Logger: Logger configurado para Software FJ.
    """

    # Obtiene la carpeta raíz del proyecto.
    ruta_proyecto = Path(__file__).resolve().parent.parent

    # Crea la carpeta logs si todavía no existe.
    carpeta_logs = ruta_proyecto / "logs"
    carpeta_logs.mkdir(parents=True, exist_ok=True)

    archivo_log = carpeta_logs / "sistema.log"

    logger = logging.getLogger("software_fj")
    logger.setLevel(logging.DEBUG)

    # Evita agregar manejadores duplicados.
    if logger.handlers:
        return logger

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    manejador_archivo = logging.FileHandler(
        archivo_log,
        mode="a",
        encoding="utf-8",
    )
    manejador_archivo.setLevel(logging.DEBUG)
    manejador_archivo.setFormatter(formato)

    manejador_consola = logging.StreamHandler()
    manejador_consola.setLevel(logging.INFO)
    manejador_consola.setFormatter(formato)

    logger.addHandler(manejador_archivo)
    logger.addHandler(manejador_consola)

    return logger