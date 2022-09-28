from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado

from Repositorios.RepositorioPaisesCategoria import RepositorioPaisesCategorias
from Modelos.PaisCategoria import PaisCategoria

from datetime import datetime

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioPaisCategoria = RepositorioPaisesCategorias()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, data):
        userID = "lo pido como parámetro"
        año_actividad = 2026
        id_PaisCategoria = self.getPaisCategoria(data['pais'], data['categoria'])
        fechayHora = self.getTime()
        json = {"user": userID, "ejercicio": año_actividad, "envio": fechayHora, "id_paisCategoria": id_PaisCategoria}
        return json


    #Métodos
    def getTime(self):
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    #Recibe una categoria y un pais y devuelve un id_paiscategoria
    def getPaisCategoria(self, country, category):
        paisCategorias = self.repositorioPaisCategoria.findAll()
        for paisCategoria in paisCategorias:
            if(paisCategoria["categoria"]["nombre"]==category and paisCategoria["pais"]["nombre"]==country):
                return paisCategoria["_id"]
        return None