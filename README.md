# Sistema Integral de Gestión Software FJ

Proyecto académico desarrollado en Python para gestionar clientes, servicios y reservas mediante Programación Orientada a Objetos.

La aplicación permite registrar clientes, calcular el costo de diferentes servicios, procesar reservas, confirmar operaciones, cancelar reservas y controlar errores sin interrumpir la ejecución del programa.

## Información académica

- **Actividad:** Fase 4 - Componente práctico - Prácticas simuladas
- **Curso:** Programación
- **Estudiante:** Juan Sebastián Rojas Badillo
- **Empresa simulada:** Software FJ
- **Lenguaje:** Python 3
- **Repositorio:** https://github.com/koss485-web/fase-4-software-fj

## Objetivo

Desarrollar una aplicación orientada a objetos que permita gestionar clientes, servicios y reservas, aplicando:

- Abstracción.
- Herencia.
- Encapsulación.
- Polimorfismo.
- Excepciones personalizadas.
- Encadenamiento de excepciones.
- Registro de eventos y errores.
- Validaciones de datos.
- Operaciones válidas e inválidas.

## Funcionalidades principales

El sistema permite:

1. Registrar y validar clientes.
2. Reservar salas por horas.
3. Alquilar equipos por días.
4. Contratar asesorías especializadas por horas.
5. Aplicar descuentos opcionales.
6. Aplicar impuestos opcionales.
7. Procesar reservas.
8. Confirmar reservas.
9. Cancelar reservas.
10. Controlar operaciones repetidas o no permitidas.
11. Registrar eventos y errores en un archivo de log.
12. Continuar la ejecución después de errores controlados.

## Estructura del proyecto

```text
fase-4-software-fj/
│
├── main.py
├── README.md
├── .gitignore
│
├── excepciones/
│   ├── __init__.py
│   └── excepciones.py
│
├── modelos/
│   ├── __init__.py
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   └── reserva.py
│
├── servicios/
│   ├── __init__.py
│   ├── reserva_sala.py
│   ├── alquiler_equipo.py
│   └── asesoria_especializada.py
│
├── utilidades/
│   ├── __init__.py
│   └── configuracion_logging.py
│
├── pruebas/
│   ├── __init__.py
│   └── simulaciones.py
│
├── logs/
│   └── sistema.log
│
└── docs/
```

## Modelo de clases

```text
Entidad
├── Cliente
├── Servicio
│   ├── ReservaSala
│   ├── AlquilerEquipo
│   └── AsesoriaEspecializada
└── Reserva
```

### Entidad

Clase abstracta general que contiene el identificador y obliga a las clases derivadas a implementar el método `mostrar_informacion()`.

### Cliente

Gestiona los datos personales del cliente mediante atributos encapsulados y propiedades.

Valida:

- Nombre.
- Documento.
- Correo electrónico.
- Teléfono.

### Servicio

Clase abstracta que contiene la información y los comportamientos comunes de los servicios.

Define los métodos:

- `calcular_costo()`
- `describir_servicio()`
- `validar_parametros()`
- `verificar_disponibilidad()`
- `aplicar_ajustes()`

### ReservaSala

Calcula el costo de una sala según:

- Tarifa por hora.
- Cantidad de horas.
- Descuento.
- Impuesto.
- Capacidad.
- Tipo de sala.

### AlquilerEquipo

Calcula el costo de un equipo según:

- Tarifa por día.
- Cantidad de días.
- Descuento.
- Impuesto.
- Tipo de equipo.
- Marca.
- Estado del equipo.

### AsesoriaEspecializada

Calcula el costo de una asesoría según:

- Tarifa por hora.
- Horas contratadas.
- Descuento.
- Impuesto.
- Especialidad.
- Profesional.
- Modalidad.

### Reserva

Relaciona un cliente con un servicio y controla:

- Procesamiento.
- Cálculo polimórfico del costo.
- Confirmación.
- Cancelación.
- Liberación del servicio.
- Estado de la reserva.

## Principios de Programación Orientada a Objetos

### Abstracción

Las clases `Entidad` y `Servicio` utilizan `ABC` y `abstractmethod`, por lo que no pueden instanciarse directamente.

### Herencia

Las clases `Cliente`, `Servicio` y `Reserva` heredan de `Entidad`.

Los servicios `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada` heredan de `Servicio`.

### Encapsulación

La clase `Cliente` protege sus datos mediante atributos privados como:

```python
self.__nombre
self.__documento
self.__correo
self.__telefono
```

Su acceso y actualización se realizan mediante propiedades.

### Polimorfismo

Cada servicio implementa su propia versión de `calcular_costo()`.

La clase `Reserva` puede ejecutar el cálculo sin conocer el tipo concreto de servicio:

```python
self.__servicio.calcular_costo(
    self.__duracion,
    descuento=self.__descuento,
    impuesto=self.__impuesto,
)
```

## Manejo de excepciones

El proyecto incluye una jerarquía de excepciones personalizadas:

```text
SistemaFJError
├── ClienteInvalidoError
│   ├── DocumentoInvalidoError
│   └── CorreoInvalidoError
├── ServicioInvalidoError
├── ServicioNoDisponibleError
├── DuracionInvalidaError
├── ReservaInvalidaError
├── OperacionNoPermitidaError
└── CalculoCostoError
    ├── DescuentoInvalidoError
    └── ImpuestoInvalidoError
```

También se aplican:

- `try`
- `except`
- `else`
- `finally`
- Encadenamiento mediante `raise ... from ...`
- Captura de errores específicos.
- Captura general de respaldo.

## Sistema de logs

La aplicación utiliza el módulo `logging` de Python.

Los eventos se muestran en la terminal y se almacenan en:

```text
logs/sistema.log
```

Ejemplo de registro:

```text
2026-11-18 22:59:46 | INFO | software_fj | Reserva confirmada: codigo=RES-001
```

El archivo de log no se publica en GitHub porque se genera automáticamente durante cada ejecución.

## Simulaciones ejecutadas

El programa realiza diez pruebas secuenciales:

| Número | Simulación | Resultado esperado |
|---:|---|---|
| 1 | Cliente válido | Registro correcto |
| 2 | Correo incorrecto | Excepción controlada |
| 3 | Reserva de sala válida | Costo de $160.650 |
| 4 | Sala con duración negativa | Excepción controlada |
| 5 | Alquiler de equipo válido | Costo de $452.200 |
| 6 | Alquiler de cero días | Excepción controlada |
| 7 | Asesoría especializada válida | Costo de $514.080 |
| 8 | Modalidad de asesoría inválida | Excepción controlada |
| 9 | Procesamiento y confirmación | Reserva confirmada por $158.270 |
| 10 | Cancelación repetida | Operación no permitida controlada |

Los errores esperados no detienen la aplicación.

## Requisitos

- Python 3.10 o superior.
- Git, únicamente para clonar y gestionar el repositorio.
- No se requieren librerías externas.

El proyecto utiliza exclusivamente módulos de la biblioteca estándar de Python.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/koss485-web/fase-4-software-fj.git
```

Entrar en la carpeta:

```bash
cd fase-4-software-fj
```

## Ejecución

Ejecutar desde la carpeta principal:

```bash
python main.py
```

En algunos sistemas puede utilizarse:

```bash
python3 main.py
```

## Resultados esperados

La aplicación debe mostrar las diez simulaciones y finalizar con mensajes similares a:

```text
Las diez pruebas finalizaron correctamente.
Finalizó la ejecución de la aplicación.
```

No debe aparecer ningún `Traceback` sin controlar.

## Tecnologías utilizadas

- Python 3.
- Visual Studio Code.
- Git.
- GitHub.
- Programación Orientada a Objetos.
- Módulo `abc`.
- Módulo `logging`.
- Expresiones regulares mediante `re`.
- Manejo de rutas mediante `pathlib`.

## Autor

**Juan Sebastián Rojas Badillo**

Proyecto desarrollado como evidencia académica de la Fase 4 del curso de Programación.