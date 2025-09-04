from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.routers.router import router

app = FastAPI()

# PRODUCCIÓN: orígenes explícitos + regex para previews de Vercel
allowed = [o.strip() for o in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if o.strip()]

if not allowed:
    allowed = [
        "https://bp-mportfolio.vercel.app",   # tu frontend
        "https://mini-enigma.vercel.app",     # mismo host (si llamas desde ahí)
        "http://localhost:3000",
        "http://localhost:8000",
    ]

print(allowed)

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

@app.get("/")
def root():
    return {"message": f"Bienvenido a MiniEnigma Origenes : {allowed}"}
