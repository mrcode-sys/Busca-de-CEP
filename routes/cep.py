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
    not_infs = []

    val = val.replace("-", "")

    cep_db = Cep.query.filter_by(cep=val).first()

    if cep_db:
        not_inf = False
        for i in infs:
            if getattr(cep_db, i, None) is None:
                not_infs.append(i)
                not_inf = True

        print("Carregando do Banco de Dados")
        if not_inf == False:
            return jsonify(cep_db.to_dict()), 200
        else:
            print("Ausência de informação no database")

    url = f"https://viacep.com.br/ws/{val}/json/"
    resp = requests.get(url)

    if resp.status_code != 200:
        return jsonify({"erro":True}), 502

    data = resp.json()
    if "erro" in data:
        return jsonify({"erro":True}), 400
    
    if not_infs and cep_db:
        for i in not_infs:
            setattr(cep_db, i, data.get(i))

        db.session.commit()

        return jsonify(cep_db.to_dict()), 200

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