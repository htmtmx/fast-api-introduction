from fastapi import FastAPI

app = FastAPI()


# @ app.get("Nombre de nuestro endpoint") define la ruta que tomara nuestra app
@app.get('/')
def message():
    return "Hola parcero"

# Comando para levantar la aplicacion
    """
        uvicorn main:app
        
        Flags
        --reload -> Recargara el servidor en cuanto detecte cambios
        --port XXXX -> Definimos el puerto en el que queremos que se ejecute la aplicacion
        --host 0.0.0.0 -> Ejecutarla mediante red para que otros dispositivos conectado en la misma red puedan acceder
    """