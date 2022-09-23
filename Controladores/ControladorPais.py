from Modelos.Pais import Pais

class ControladorPais():
    def __init__(self):
        print("Se ha creado un país")

    def index(self):
        print("listar todos los paises")
        unPais={
            "id": 1,
            "pais": "Colombia",
            "latitud": "4° 35'56''",
            "Longitud": "74°04'51''"
        }
        return [unPais]

    def create(self, infoPais):
        print("crear los paises")
        elPais = Pais(infoPais)
        return elPais.__dict__
