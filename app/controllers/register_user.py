from flask import jsonify , request
from app.schemas.register_shemas import CreateUser
from pydantic import ValidationError


def register():
    json_data = request.get_json()

    try:
        data = CreateUser(**json_data)
    except ValidationError as erro:
        return jsonify({"msg":erro.errors}) , 400
    
    return jsonify({"msg":"Usuario criado com sucesso!"}) , 201

