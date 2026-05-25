from flask import jsonify , request
from app.schemas.register_shemas import User_register_Schemas
from pydantic import ValidationError



def before_request():
    if request.method == 'POST' or request.method == 'PUT':
        if not request.is_json:
            return jsonify({"msg":"Formato de dados nao suportado!"}) ,400

def register():
    json_data = request.get_json(silent= True)

    if not json_data:
        return jsonify({"msg":"O corpo da requisicao nao pode ser vazio!"}) , 400
    return jsonify({"dados":json_data}) , 200
