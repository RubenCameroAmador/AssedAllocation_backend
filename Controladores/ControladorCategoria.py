from Modelos.Categoria import Categoria
from Repositorios.RepositorioCategoria import RepositorioCategoria

class ControladorCategoria():

    def __init__(self):
        self.repositorioCategoria = RepositorioCategoria()


    def index(self):
        return self.repositorioCategoria.findAll()


    def create(self, infoCategoria):
        nuevaCategoria = Categoria(infoCategoria)
        return self.repositorioCategoria.save(nuevaCategoria)


    def show(self, id):
        laCategoria = Categoria(self.repositorioCategoria.findById(id))
        return laCategoria.__dict__


    def update(self, id, infoCategoria):
        categoriaActual = Categoria(self.repositorioCategoria.findById(id))
        categoriaActual.nombre = infoCategoria["nombre"]
        return self.repositorioCategoria.save(categoriaActual)

    def delete(self, id):
        return self.repositorioCategoria.delete(id)