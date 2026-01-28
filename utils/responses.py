from flask import jsonify

def sucess_response(data, status=200):
    return jsonify({
        "sucess": True,
        "data": data
    }), status

def error_response(message, status):
    return jsonify({
        "sucess": False,
        "error": message
    }), status