import json

FILE_PATH = "servicios.json"

def guardar_datos(datos):
    with open(FILE_PATH, 'w') as f:
        json.dump(datos, f)

def cargar_datos():
    try:
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
#hh