from errors.errors import InvalidCEPError, ExternalAPIError
from utils.cache_verification import cache_is_valid
from datetime import datetime
from flask import current_app
from models.cep import Cep
from extensions import db
import requests
import re

class Search_cep():
    def __init__(self, val):

        self.val = re.sub(r"\D", "", val)
        
        if len(val) != 8:
            raise InvalidCEPError()
        
        self.cep_db = Cep.query.filter_by(cep=self.val).first()

        self.infs = [       
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
            "siafi",
            "updated_at",
        ]
        self.not_infs = []
        self.cache_valid = ""

    def search(self):
        status = 200
        cached = True
        data = self.database_search()

        if not data:
            data = self.api_search()
            status = 201
            cached = False

        return data, status, cached

    def database_search(self):
        if self.cep_db:
            self.cache_valid = cache_is_valid(self.cep_db.updated_at, current_app.config["CEP_CACHE_TTL_HOURS"])            
            print(self.cache_valid)
            self.not_in_inf()

            if not self.not_infs and self.cache_valid:
                return self.cep_db.to_dict()

            elif not self.cache_valid:
                print("Dados do CEP expirados")

            else:
                print("Ausência de informação no database")
            
            return None

    def api_search(self):
        url = f"https://viacep.com.br/ws/{self.val}/json/"
        print(url)

        try:
            resp = requests.get(url, timeout=7)
            
        except requests.RequestException:
            raise ExternalAPIError()

        print(url)
        print(resp.status_code)

        if resp.status_code != 200:
            raise ExternalAPIError()

        data = resp.json()
        if "erro" in data:
            raise InvalidCEPError()
        
        print(data)

        if self.not_infs:
            self.updt_db(data)

        elif not self.cache_valid and self.cep_db:
            self.updt_all_db(data)
        else:
            self.save_cep(data)
        return data

    def save_cep(self, data):
        print("Salvando CEP")

        new = Cep(
            cep = self.val,
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
            updated_at = datetime.now()
        )

        db.session.add(new)
        db.session.commit()

        return new.to_dict()

    def updt_db(self, data):
        for i in self.not_infs:
            setattr(self.cep_db, i, data.get(i))

        self.cep_db.updated_at = datetime.now()

        db.session.commit()

        return self.cep_db.to_dict()

    def updt_all_db(self, data):
        print(data)
        for field in self.infs:

            if field == "updated_at":
                continue
            print(data)
            setattr(self.cep_db, field, data.get(field))

        self.cep_db.updated_at = datetime.now()

        db.session.commit()

        return self.cep_db.to_dict()

    def not_in_inf(self):
        self.not_infs.clear()
        for i in self.infs:
            if getattr(self.cep_db, i, None) is None:
                self.not_infs.append(i)