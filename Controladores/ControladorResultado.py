from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()

    def index(self):
        return self.repositorioResultado.findAll()