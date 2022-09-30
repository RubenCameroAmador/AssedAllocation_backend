from flask import Blueprint, jsonify, request
from Controladores.ControladorResultado import ControladorResultado

cont = ControladorResultado()
resultado = Blueprint('resultado',__name__)


@resultado.route("/resultado", methods = ['GET'])
def getAllResults():
    return jsonify(cont.index())

@resultado.route("/resultado", methods=['POST'])
def createResult():
    data = request.get_json()
    return jsonify(cont.create(data))

@resultado.route("/resultadoValicacion", methods=['POST'])
def resValidate():
    data = request.get_json()
    return jsonify(cont.validacionResultado(data))