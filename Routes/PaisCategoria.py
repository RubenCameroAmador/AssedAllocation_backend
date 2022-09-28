from flask import Blueprint, jsonify, request
from Controladores.ControladorPaisesCategoria import ControladorPaisesCategorias

cont = ControladorPaisesCategorias()
paisCategoria = Blueprint('paisCategoria', __name__)

@paisCategoria.route("/paiscategoria/pais/<string:pais_id>/categoria/<string:categoria_id>", methods = ['POST'])
def createPaisCategoria(pais_id, categoria_id):
    return jsonify(cont.create(pais_id, categoria_id))


@paisCategoria.route("/paiscategoria", methods = ['GET'])
def showAllPaisesCategorias():
    return jsonify(cont.index())


@paisCategoria.route("/paiscategoria/<string:id>", methods = ['GET'])
def showByID(id):
    return jsonify(cont.show(id))

