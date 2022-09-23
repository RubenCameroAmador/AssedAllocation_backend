from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo as pymongo
import certifi


from Routes.Pais import pais

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(pais)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])