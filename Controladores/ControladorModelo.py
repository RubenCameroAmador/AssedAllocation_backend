import numpy as np

"""
Matrices de tamaño: 4*7
Columnas: Negocios
Filas: Paises
"""

class ControladorModelo():
    def __init__(self):
        self.m_riesgo_rentabilidad = np.array([[0.1,0.1,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1]]).reshape(7,4)
        self.negocio_list = ["Transmisión","Almacenamiento","SED","Vias"]
        self.pais_list = ["colombia", "peru","chile","brasil", "bolivia", "panama", "EEUU"]
        self.resultados_list = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.cant_monedas = 100

    def calculo(self, data):
        self.fillMatrix(data)
        matrix_resultado = np.array(self.resultados_list).reshape(7,4)
        res_restricciones = self.restricciones(data)
        if res_restricciones["sucess"]:
            suma = 0
            for i in range(0, np.shape(matrix_resultado)[0]):
                for j in range(0, np.shape(matrix_resultado)[1]):
                    suma = matrix_resultado[i][j] * self.m_riesgo_rentabilidad[i][j] + suma
            return {
                "sucess": True,
                "resultado": suma,
                "msg": res_restricciones["msg"]
            }
        else:
            return {
                "sucess": False,
                "msg": res_restricciones["msg"]
            }


    def fillMatrix(self, data):
        for items in data:
            category = items["categoria"]
            for item in items:
                if item != "categoria":
                    self.resultados_list[self.pais_list.index(item)][self.negocio_list.index(category)] = items[item]
        #self.showArray()

    def restricciones(self, data):
        #"colombia", "peru", "chile", "brasil", "bolivia", "panama", "EEUU"
        paises_monedas = [0,0,0,0,0,0,0] #suma total de cada país por moneda
        variacionPais = [0.5,0.5,0.5,0.5,0.5,0.5,0.5]  #% por país
        for items in data:
            category = items["categoria"]
            for item in items:
                if item != "categoria":
                    if items[item] > self.cant_monedas*0.5:
                        return {
                            "sucess": False,
                            "msg": f"El pais {item} en el negocio {category} excede el 50% de monedas"
                        }
                    else:
                        paises_monedas[self.pais_list.index(item)] = paises_monedas[self.pais_list.index(item)]+items[item]
        sum_total = sum(paises_monedas)
        if sum_total < 0 or sum_total > 100:
            return {
                "sucess": False,
                "msg": "El total de monedas asignadas, excede el total permitido"
            }
        else:
            for index in range(0, len(paises_monedas)):
                if paises_monedas[index] >= self.cant_monedas*variacionPais[index]:
                    return {
                        "sucess": False,
                        "msg": f"El total de monedas en el pais {self.pais_list[index]} excede el {int(variacionPais[index]*100)}% permitido"
                    }
                else:
                    return {
                        "sucess": True,
                        "msg": "Modelo valido, se han superado todas las restricciones"
                    }




    def showArray(self):
        print(self.resultados_list)