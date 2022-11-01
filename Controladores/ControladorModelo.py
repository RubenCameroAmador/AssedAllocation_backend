import numpy as np

"""
Matrices de tamaño: 4*7
Columnas: Negocios
Filas: Paises
"""
class ControladorModelo():
    def __init__(self):
        self.m_riesgo_rentabilidad = np.array([[1.0,1.0,1.0,1.0],
                                               [1.0,1.0,1.0,1.0],
                                               [1.0,1.0,1.0,1.0],
                                               [1.0,1.0,1.0,1.0],
                                               [1.0,1.0,1.0,1.0],
                                               [1.0,1.0,1.0,1.0],
                                               [1.0,1.0,1.0,1.0],
                                               [1.0,1.0,1.0,1.0],
                                               [1.0,1.0,1.0,1.0]]).reshape(9,4)
        self.negocio_list = ["Transmisión","Almacenamiento","SED","Vias"]
        self.pais_list = ["colombia", "peru","chile","brasil", "bolivia", "panama", "EEUU", "mexico", "argentina"]
        self.resultados_list = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.cant_monedas = 100

    def calculo(self, data):
        self.fillMatrix(data)
        matrix_resultado = np.array(self.resultados_list).reshape(9,4)
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
        #"colombia", "peru", "chile", "brasil", "bolivia", "panama", "EEUU", "mexico", "argentina"
        paises_monedas = [0,0,0,0,0,0,0,0,0] #suma total de cada país por moneda
        negocio_moneda = [0,0,0,0] #suma país de cada negocio por moneda
        variacionPais = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]  #% por país
        variacionNegocio = [0.5,0.5,0.5,0.5]
        porcentaje_monedas = [[0.5,0.5,0.5,0.5],
                              [0.5,0.5,0.5,0.5],
                              [0.5,0.5,0.5,0.5],
                              [0.5,0.3,0.5,0.5],
                              [0.5,0.5,0.5,0.5],
                              [0.5,0.5,0.5,0.5],
                              [0.5,0.5,0.5,0.5],
                              [0.5,0.5,0.5,0.5],
                              [0.5,0.5,0.5,0.5]]

        for items in data:
            category = items["categoria"]
            for item in items:
                if item != "categoria":
                    money_porcentaje = porcentaje_monedas[self.pais_list.index(item)][self.negocio_list.index(category)]
                    if items[item] > self.cant_monedas * money_porcentaje:  #Valida país por país
                        return {
                            "sucess": False,
                            "msg": f"El pais {item} en el negocio {category} excede el potencial capturable de {money_porcentaje * 100}% de monedas"
                        }
                    else:
                        paises_monedas[self.pais_list.index(item)] = paises_monedas[self.pais_list.index(item)] + items[item]
                        negocio_moneda[self.negocio_list.index(category)] = negocio_moneda[self.negocio_list.index(category)] + items[item]
        sum_total = sum(paises_monedas)
        if sum_total < 0 or sum_total > 100:   #Valida que no se asignen más de 100 monedas o menos
            return {
                "sucess": False,
                "msg": "El total de monedas asignadas, excede el total permitido"
            }
        else:
            for index in range(0, len(paises_monedas)):   #Validación por total paises
                if paises_monedas[index] >= self.cant_monedas * variacionPais[index]:
                    return {
                        "sucess": False,
                        "msg": f"El total de monedas en el pais {self.pais_list[index]} excede el {int(variacionPais[index] * 100)}% permitido"
                    }
            for index in range(0, len(negocio_moneda)):   #validación por total negocio
                if negocio_moneda[index] >= self.cant_monedas * variacionNegocio[index]:
                    return {
                        "sucess": False,
                        "msg": f"El total de monedas en el negocio {self.negocio_list[index]} excede el {int(variacionNegocio[index] * 100)}% permitido"
                        }
            return {
                "sucess": True,
                "msg": "Modelo valido, se han superado todas las restricciones"
                }




    def showArray(self):
        print(self.resultados_list)