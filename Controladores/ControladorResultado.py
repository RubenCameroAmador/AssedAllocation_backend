from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado

from Repositorios.RepositorioPaisesCategoria import RepositorioPaisesCategorias
from Modelos.PaisCategoria import PaisCategoria

from Controladores.ControladorModelo import ControladorModelo

from datetime import datetime


class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioPaisCategoria = RepositorioPaisesCategorias()
        self.controladorModelo = ControladorModelo()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, data):
        userID = "lo pido como parámetro"
        año_actividad = 2026  # sería el año de la actividad por si hay que definir
        fechayHora = self.getTime()
        data.append({
            "año": año_actividad,
            "user": userID,
            "time": fechayHora
        })
        calculo = self.controladorModelo.calculo(data)
        if calculo["sucess"]:
            return data
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

    def validacionResultado(self, data):
        monedas_max = 100   #Monedas max del ejercicio
        suma = 0
        for items in data:
            suma_category = 0
            for item in items:
                if item != "categoria":
                    suma = suma + items[item]
                    suma_category = suma_category + items[item]
            if suma_category > monedas_max * 0.25:
                return {
                    "sucess": False,
                    "msg": "El total de monedas excede el limite permitido",
                    "negocio": f"{items['categoria']}"
                }
        if suma > monedas_max:
            return {
                "sucess": False,
                "msg": "El total de items excede las monedas"
            }
        elif suma == monedas_max:  #Valida que el número de monedas enviadas sea igual al total
            return {
                "sucess": True
            }
        else:
            return {
                "sucess": False,
                "msg": "No fue asignado el total de las monedas"
            }

