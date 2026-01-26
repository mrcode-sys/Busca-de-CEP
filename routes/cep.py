from flask import Blueprint, jsonify
from models.cep import Cep
import requests
from extensions import db

cep_bp = Blueprint("cep", __name__, url_prefix="/api/cep")

@cep_bp.route("<val>")
def search_cep(val):
    
    infs = [       
        "cep",
        "localidade",
        "uf",
        "regiao",
        "bairro",
        "complemento",
        "logradouro",
        "ibge",
        "gia",
        "ddd",
        "siafi"
        ]

    val = val.replace("-", "")

    cep_db = Cep.query.filter_by(cep=val).first()

    if cep_db:
        not_inf = False
        for i in infs:
            if getattr(cep_db, i, None) is None:
                not_inf = True
                break

        print("Carregando do Banco de Dados")
        if not_inf == False:
            return jsonify(cep_db.to_dict()), 203
        else:
            print("Ausência de informação no database")
            db.session.delete(cep_db)
            db.session.commit()

    url = f"https://viacep.com.br/ws/{val}/json/"
    resp = requests.get(url)

    if resp.status_code != 200:
        return jsonify({"erro":True}), 502

    data = resp.json()
    if "erro" in data:
        return jsonify({"erro":True}), 400
    
    print("Salvando CEP")
    new = Cep(
        cep = val,
        localidade = data.get("localidade"),
        uf = data.get("uf"),
        regiao = data.get("regiao"),
        bairro = data.get("bairro"),
        complemento = data.get("complemento"),
        logradouro = data.get("logradouro"),
        ibge = data.get("ibge"),
        gia = data.get("gia"),
        ddd = data.get("ddd"),
        siafi = data.get("siafi"),
    )

    db.session.add(new)
    db.session.commit()

    return jsonify(new.to_dict()), 200