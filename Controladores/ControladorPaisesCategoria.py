from Repositorios.RepositorioPaisesCategoria import RepositorioPaisesCategorias
from Modelos.PaisCategoria import PaisCategoria

from Repositorios.RepositorioPais import RepositorioPais
from Repositorios.RepositorioCategoria import RepositorioCategoria
from Modelos.Pais import Pais
from Modelos.Categoria import Categoria

class ControladorPaisesCategorias():

    def __init__(self):
        self.repositorioPaisesCategorias = RepositorioPaisesCategorias()
        self.repositorioPais = RepositorioPais()
        self.repositorioCategoria = RepositorioCategoria()

    def index(self):
        return self.repositorioPaisesCategorias.findAll()

    def create(self, id_pais, id_categoria):
        elPais = Pais(self.repositorioPais.findById(id_pais))
        laCategoria = Categoria(self.repositorioCategoria.findById(id_categoria))
        nuevoMix = PaisCategoria({})
        nuevoMix.pais = elPais
        nuevoMix.categoria = laCategoria
        return self.repositorioPaisesCategorias.save(nuevoMix)

    def show(self, id):
        elPaisCategoria = PaisCategoria(self.repositorioCategoria.findById(id))
        return elPaisCategoria.__dict__