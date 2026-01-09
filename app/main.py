from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.routers.router import router
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# PRODUCCIÓN: orígenes explícitos + regex para previews de Vercel
allowed = [o.strip() for o in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if o.strip()]

if not allowed:
    allowed = [
        "*"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed,
    allow_origin_regex=r"https://.*\.vercel\.app$",  # permite previews *.vercel.app
    allow_credentials=False,  # déjalo en False si no usas cookies/autenticación
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=600,
)

app.include_router(router)

base_path = Path(__file__).parent

static_path = base_path / "static"

if static_path.exists():
    app.mount("/static", StaticFiles(directory=static_path), name="static")
else:
    print(f"ADVERTENCIA: No se encontró la carpeta static en: {static_path}")


@app.get("/")
def root():
    return {"message": f"Bienvenido a MiniEnigma Origenes : {allowed}"}

