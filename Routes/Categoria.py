from flask import Blueprint, jsonify, request
from Controladores.ControladorCategoria import ControladorCategoria

cont = ControladorCategoria()

categoria = Blueprint("categoria",__name__)

@categoria.route("/categoria", methods = ['POST'])
def create():
    data = request.get_json()
    return jsonify(cont.create(data))

@categoria.route("/categoria", methods = ['GET'])
def showAll():
    return jsonify(cont.index())

@categoria.route("/categoria/<string:id>", methods = ['GET'])
def showByID(id):
    return jsonify(cont.show(id))