from Repositorios.RepositorioPais import RepositorioPais
from Modelos.Pais import Pais

class ControladorPais():
    def __init__(self):
        self.repositorioPais = RepositorioPais()

    def index(self):
        return self.repositorioPais.findAll()

    def create(self, infoPais):
        nuevoPais = Pais(infoPais)
        if(self.uniqueName(infoPais["nombre"])==False):
            return self.repositorioPais.save(nuevoPais)
        else:
            message = {
                "status": "not created",
                "message": "El nombre del país, ya existe"
            }
            return message

    def show(self, id):
        elPais = Pais(self.repositorioPais.findById(id))
        return elPais.__dict__

    def update(self, id, infoPais):
        paisActual = Pais(self.repositorioPais.findById(id))
        paisActual.nombre = infoPais["nombre"]
        paisActual.latitud = infoPais["latitud"]
        paisActual.longitud = infoPais["longitud"]
        return self.repositorioPais.save(paisActual)

    def delete(self, id):
        return self.repositorioPais.delete(id)

    def uniqueName(self, nombre):
        paises = self.repositorioPais.findAll()
        for pais in paises:
            if(nombre == pais["nombre"]):
                return True
        return False