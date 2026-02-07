from extensions import db
from datetime import datetime

print("MODEL CARREGADO")
class Cep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(8), unique=True, nullable=False)
    localidade = db.Column(db.String(100))
    uf = db.Column(db.String(2))
    regiao = db.Column(db.String(30))
    bairro = db.Column(db.String(100))
    complemento = db.Column(db.String(100))
    logradouro = db.Column(db.String(100))
    ibge = db.Column(db.String(7))
    gia = db.Column(db.String(4))
    ddd = db.Column(db.String(2))
    siafi = db.Column(db.String(4))
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    def to_dict(self):
        return {
            "cep": self.cep,
            "localidade": self.localidade,
            "uf": self.uf,
            "regiao": self.regiao,
            "bairro": self.bairro,
            "complemento": self.complemento,
            "logradouro": self.logradouro,
            "ibge": self.ibge,
            "gia": self.gia,
            "ddd": self.ddd,
            "siafi": self.siafi
        }