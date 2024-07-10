from ui import iniciar_aplicacion
from db import crear_tabla_peliculas

def run_app():
    crear_tabla_peliculas()
    iniciar_aplicacion()

if __name__ == "__main__":
    run_app()
