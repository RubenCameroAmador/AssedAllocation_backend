from flask import Blueprint, jsonify, request
from Controladores.ControladorResultado import ControladorResultado

cont = ControladorResultado()
resultado = Blueprint('resultado',__name__)


@resultado.route("/resultado", methods = ['GET'])
def getAllResults():
    return jsonify(cont.index())