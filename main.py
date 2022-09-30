from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json
from waitress import serve
from Routes.Pais import pais
from Routes.Categoria import categoria
from Routes.Usuario import usuario
from Routes.PaisCategoria import paisCategoria
from Routes.Resultado import resultado
from Routes.Modelo import modelo

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(pais)
app.register_blueprint(categoria)
app.register_blueprint(usuario)
app.register_blueprint(paisCategoria)
app.register_blueprint(resultado)
app.register_blueprint(modelo)

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])