from flask import Blueprint
from models.cep import Cep
from utils.responses import success_response
import requests
from extensions import db
from services.cep_service import Search_cep

cep_bp = Blueprint("cep", __name__, url_prefix="/api/cep")

@cep_bp.route("<val>")
def request_cep(val):

    sc = Search_cep(val)
    data, status, cached = sc.search()
    return success_response(data, status, cached)