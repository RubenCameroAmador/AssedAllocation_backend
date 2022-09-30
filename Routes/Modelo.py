from flask import Blueprint, request, jsonify
from Controladores.ControladorModelo import ControladorModelo

cont = ControladorModelo()
modelo = Blueprint("modelo", __name__)

"""
@modelo.route("/modelo", methods = ['GET'])
def mostrarMatriz():
    return jsonify(cont.showArray())
"""

@modelo.route("/modelo", methods = ['POST'])
def calculo():
    data = request.get_json()
    return jsonify(cont.calculo(data))