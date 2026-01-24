from flask import Blueprint, jsonify, request, render_template
import requests

cep_bp = Blueprint("cep", __name__, url_prefix="/api/cep")

@cep_bp.route("<val>")
def search_cep(val):
    url = f"https://viacep.com.br/ws/{val}/json/"
    resp = requests.get(url)

    if resp.status_code != 200:
        return jsonify({"erro":True}), 502

    dados = resp.json()
    if "erro" in dados:
        return jsonify({"erro":True}), 400
    
    return jsonify(dados)