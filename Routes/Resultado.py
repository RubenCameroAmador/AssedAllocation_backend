from flask import Blueprint, jsonify, request
from Controladores.ControladorResultado import ControladorResultado

cont = ControladorResultado()
resultado = Blueprint('resultado',__name__)


@resultado.route("/resultado", methods=['GET'])
def getAllResults():
    return jsonify(cont.index())

@resultado.route("/resultado/user/<string:userID>/year/<string:year>", methods=['POST'])
def createResult(userID,year):
    data = request.get_json()
    return jsonify(cont.create(data, userID, year))
