from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado

from Modelos.Usuario import Usuario
from Repositorios.RepositorioUsuario import RepositorioUsuario

from Controladores.ControladorModelo import ControladorModelo
from datetime import datetime


class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioUsuario = RepositorioUsuario()
        self.controladorModelo = ControladorModelo()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, data, userID, activityTime):
        elresultado = Resultado({})
        elresultado.resultado = data
        eluser = Usuario(self.repositorioUsuario.findById(userID))
        elresultado.user = eluser
        elresultado.time = self.getTime()
        elresultado.añoActividad = activityTime
        calculo = self.controladorModelo.calculo(data)
        if calculo["sucess"]:
            try:  #Empanada trifasica
                return self.repositorioResultado.save(elresultado)
            except:
                return {
                    "msg": "Resultado guardado correctamente"
                }
        else:
            return {
                "msg": calculo["msg"]
            }
    # Métodos
    def getTime(self):
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    # Recibe una categoria y un pais y devuelve un id_paiscategoria
    def getPaisCategoria(self, country, category):  # Análizar si este método no causa problemas en el rendimiento
        paisCategorias = self.repositorioPaisCategoria.findAll()
        for paisCategoria in paisCategorias:
            if paisCategoria["categoria"]["nombre"].upper() == category.upper() and paisCategoria["pais"]["nombre"].upper() == country.upper():
                return paisCategoria["_id"]
        return None