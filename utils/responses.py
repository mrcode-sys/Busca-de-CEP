from flask import jsonify
def code_message(code):
    if code == "Invalid_CEP_Error":
        message = "CEP Inválido"

    elif code == "External_API_Error":
        message = "Falha na API externa"

    elif code == "Internal_Error":
        message = "Erro interno"

    else:
        message = "Erro desconhecido"
        
    return message

def sucess_response(data, status=200):
    cached = True
    if status == 201:
        cached = False

    return jsonify({
        "sucess": True,
        "data": data,
        "cached": cached
    }), status

def error_response(code, status):
    message = code_message(code)
    return jsonify({
        "sucess": False,
        "error":{
            "code": code,
            "message": message
        }
    }), status