from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo as pymongo
import certifi
from Routes.Pais import pais
from Routes.Categoria import categoria

app = Flask(__name__)
cors = CORS(app)

#ca = certifi.where()

#client = pymongo.MongoClient("mongodb+srv://adminISA:Conexiones2030@cluster0.r95sfx2.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
#db = client.test

#print(db)
#baseDatos = client["AssedAllocationBD"]
#print(baseDatos.list_collection_names())


app.register_blueprint(pais)
app.register_blueprint(categoria)

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