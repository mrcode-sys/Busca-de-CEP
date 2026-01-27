from flask import Blueprint, jsonify
from models.cep import Cep
import requests
from extensions import db
from services.cep_service import Search_cep

cep_bp = Blueprint("cep", __name__, url_prefix="/api/cep")

@cep_bp.route("<val>")
def request_cep(val):
    try:
        sc = Search_cep(val)
        data = sc.search()
        return jsonify(data), 200
    except ValueError:
        return jsonify({"erro":True}), 400
    except RuntimeError:
        return jsonify({"erro":True}), 502