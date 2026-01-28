from models.cep import Cep
import requests
import re
from extensions import db
from errors.errors import InvalidCEPError, ExternalAPIError

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
            "siafi"
        ]
        self.not_infs = []
    def search(self):
        data = self.database_search()

        if not data:
            data = self.api_search()

        return data

    def database_search(self):

        if self.cep_db:
            self.not_in_inf()

            print("Carregando do Banco de Dados")
            if not self.not_infs:
                return self.cep_db.to_dict()

            else:
                print("Ausência de informação no database")

    def api_search(self):
        url = f"https://viacep.com.br/ws/{self.val}/json/"

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
        
        if self.not_infs:
            self.updt_db(data)
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
        )

        db.session.add(new)
        db.session.commit()

        return new.to_dict()

    def updt_db(self, data):
        for i in self.not_infs:
            setattr(self.cep_db, i, data.get(i))

        db.session.commit()

        return self.cep_db.to_dict()

    def not_in_inf(self):
        self.not_infs.clear()
        for i in self.infs:
            if getattr(self.cep_db, i, None) is None:
                self.not_infs.append(i)