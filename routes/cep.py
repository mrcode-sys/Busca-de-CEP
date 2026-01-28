from flask import Blueprint, jsonify
from models.cep import Cep
from utils.responses import sucess_response
import requests
from extensions import db
from services.cep_service import Search_cep

cep_bp = Blueprint("cep", __name__, url_prefix="/api/cep")

@cep_bp.route("<val>")
def request_cep(val):

    sc = Search_cep(val)
    data = sc.search()
    print(data)
    return sucess_response(data, 200)