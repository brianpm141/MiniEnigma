import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.router import router


#creacion de instancia principal
app = FastAPI(
    title="MiniEnigma",
    description="Api de encriptacion de mensajeria",
    version="0.1.0",
)

# Configuracion de CORS para desarrollo y produccion en Vercel
# Obtener los orígenes permitidos de una variable de entorno
allowed_origins_str = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
origins = [
    origin.strip() for origin in allowed_origins_str if origin.strip()
]

# Si no se especifican orígenes, permitir localhost para desarrollo
if not origins:
    origins = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "null",
    ]

print(f"CORS Allowed Origins: {origins}") # Added for debugging

# Añade el middleware de CORS a la aplicacion
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#Coneccion del router
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de MiniEnigma"}
