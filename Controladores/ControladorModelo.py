import numpy as np

"""
Matrices de tamaño: 4*7
Columnas: Negocios
Filas: Paises
"""

class ControladorModelo():
    def __init__(self):
        self.m_riesgo_rentabilidad = np.array([[1.5,1.4,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1],
                                               [0.3,0.6,0.1,0.1]])
        self.negocio_list = ["Transmisión","Almacenamiento","SED","Vias"]
        self.pais_list = ["colombia", "peru","chile","brasil", "bolivia", "panama", "EEUU"]
        self.resultados_list = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def calculo(self, data):
        self.fillMatrix(data)
        matrix_resultado = np.array(self.resultados_list)
        print(self.m_riesgo_rentabilidad*matrix_resultado)
        return {
            "status": "todo oka",
        }

    def fillMatrix(self, data):
        for items in data:
            category = items["categoria"]
            for item in items:
                if item != "categoria":
                    self.resultados_list[self.pais_list.index(item)][self.negocio_list.index(category)] = items[item]
        #self.showArray()


    def showArray(self):
        print(self.resultados_list)

