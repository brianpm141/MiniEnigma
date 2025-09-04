from fastapi import FastAPI
import os

app = FastAPI()

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

@app.get("/")
def read_root():
    return {"message": "Hello from MiniEnigma (Simplified)!"}
