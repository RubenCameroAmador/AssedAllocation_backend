from flask import Blueprint, jsonify, request
from Controladores.ControladorPais import ControladorPais

cont = ControladorPais()

pais = Blueprint('pais',__name__)

@pais.route("/pais", methods= ['GET'])
def getPais():
    return jsonify(cont.index())

@pais.route("/pais/<string:id>", methods=['GET'])
def getPaisByID(id):
    return jsonify(cont.show(id))

@pais.route("/pais", methods = ['POST'])
def createPais():
    data = request.get_json()
    return jsonify(cont.create(data))