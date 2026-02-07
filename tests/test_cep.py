from datetime import datetime, timedelta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.cep import Cep

def test_valid_infs_on_cep_api(client):
    resp = client.get("/api/cep/01001000")

    data = resp.get_json()
    assert "logradouro" in data['data']

def test_correct_status_success_api(client):
    resp = client.get("/api/cep/01001000")

    data = resp.get_json()
    assert data['cached'] == False
    assert resp.status_code == 201
    assert data["success"] == True

def test_incorrect_cep(client):
    resp = client.get("/api/cep/00000000")

    data = resp.get_json()

    assert resp.status_code == 400
    assert data["success"] == False

def test_correct_infs_on_cep_cache(client):
    client.get("/api/cep/01001000")
    resp = client.get("/api/cep/01001000")

    data = resp.get_json()

    assert "logradouro" in data['data']

def test_correct_status_success_cache(client):
    client.get("/api/cep/01001000")
    resp = client.get("/api/cep/01001000")

    data = resp.get_json()

    assert resp.status_code == 200
    assert data['cached'] == True
    assert data["success"] == True

def test_cep_error_format(client):
    resp = client.get("/api/cep/010010000")

    data = resp.get_json()

    assert resp.status_code == 400
    assert data["success"] == False

def test_cache_valid(client):

    client.get("/api/cep/01001000")

    from extensions import db
    cep_db = Cep.query.filter_by(cep="01001000").first()

    response = client.get("/api/cep/01001000")
    data = response.get_json()

    cep_db.updated_at = datetime.now()

    db.session.commit()

    assert response.status_code == 200
    assert data["cached"] is True

def test_cache_expired(client):
    expired_time = datetime.now() - timedelta(hours=25)

    cep = Cep(
        cep="01001000",
        localidade="São Paulo",
        uf="SP",
        updated_at=expired_time
    )

    from extensions import db
    db.session.add(cep)
    db.session.commit()

    response = client.get("/api/cep/01001000")
    data = response.get_json()

    assert response.status_code == 201
    assert data["cached"] is False
