# MiniEnigma

MiniEnigma es una herramienta de encriptación y desencriptación de texto inspirada en el funcionamiento de la famosa máquina Enigma. Este proyecto proporciona una API sencilla para proteger mensajes mediante una clave secreta.

**URL Base:** https://mini-enigma.vercel.app/

## 1. Uso de la API

La API cuenta con dos endpoints principales para procesar textos.

### Endpoints

- **POST** `/minienigma/encrypt`: Encripta un mensaje.
- **POST** `/minienigma/decrypt`: Desencripta un mensaje previamente encriptado.

### Formato de Solicitud (JSON)

Ambos endpoints esperan un cuerpo JSON con la siguiente estructura:

```json
{
  "message": "Tu mensaje aquí (1-180 caracteres)",
  "password": "tu_clave_secreta_aqui (15-64 caracteres)"
}
```

- `message`: El texto que deseas encriptar o desencriptar.
- `password`: Una clave secreta necesaria para el proceso de cifrado/descifrado (entre 15 y 64 caracteres).

### Respuestas

La API devuelve un objeto JSON con el resultado de la operación.

**Respuesta Exitosa (200 OK):**

```json
{
  "result": "Texto procesado (encriptado o desencriptado)"
}
```

**Posibles Errores:**

- **400 Bad Request**: Contraseña inválida o mensaje corrupto.
- **500 Internal Server Error**: Error interno de procesamiento.

## 2. Tecnologías

Este proyecto ha sido construido utilizando las siguientes tecnologías:

- **[Python](https://www.python.org/)**: Lenguaje de programación principal.
- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno y rápido para construir APIs.
- **[Uvicorn](https://www.uvicorn.org/)**: Servidor ASGI para ejecutar la aplicación.
- **[Pydantic](https://docs.pydantic.dev/)**: Validación de datos y gestión de configuraciones.
- **[Vercel](https://vercel.com/)**: Plataforma de despliegue y hosting.

## 3. Estructura del Proyecto

La estructura de carpetas del proyecto es la siguiente:

- `app/`: Contiene el código fuente principal de la aplicación.
  - `main.py`: Punto de entrada de la aplicación FastAPI y configuración de CORS.
  - `routers/`: Definición de las rutas y endpoints de la API (`router.py`).
  - `models/`: Modelos de datos Pydantic para validación de entradas y salidas (`message.py`).
  - `enigmain/`: Lógica core de encriptación y desencriptación.
  - `static/`: Archivos estáticos.
- `api/`: Scripts de configuración para el despliegue en Vercel (Entrypoint).
- `requirements.txt`: Lista de dependencias del proyecto.
- `vercel.json`: Archivo de configuración para el despliegue en Vercel.
