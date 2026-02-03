from flask import jsonify
err_messages = {
    "Invalid_CEP_Error": "CEP inválido",
    "External_API_Error": "Falha ao consultar API externa",
    "Internal_Error": "Erro interno",
}
def code_message(code):
    return err_messages.get(code, "Erro desconhecido")

def success_response(data, status=200, cached=False):

    return jsonify({
        "success": True,
        "data": data,
        "cached": cached
    }), status

def error_response(code, status):
    message = code_message(code)
    return jsonify({
        "success": False,
        "error":{
            "code": code,
            "message": message
        }
    }), status