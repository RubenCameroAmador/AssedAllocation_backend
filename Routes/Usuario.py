from flask import Blueprint, jsonify, request
from Controladores.ControladorUsuario import ControladorUsuario

cont = ControladorUsuario()
usuario = Blueprint("usuario",__name__)

@usuario.route("/usuario", methods = ['POST'])
def createUser():
    data = request.get_json()
    return jsonify(cont.create(data))

@usuario.route("/usuario", methods = ['GET'])
def showAllUsers():
    return jsonify(cont.index())

@usuario.route("/usuario/<string:id>", methods = ['GET'])
def showByID(id):
    return jsonify(cont.show(id))


@usuario.route("/usuario/<string:id>", methods = ['DELETE'])
def deleteByID(id):
    return jsonify(cont.delete(id))