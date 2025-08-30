from fastapi import FastAPI
from .routers.router import router


#creacion de instancia principal
app = FastAPI(
    title="MiniEnigma",
    description="Api de encriptacion de mensajeria",
    version="0.1.0",
)


#Coneccion del router
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de MiniEnigma"}
