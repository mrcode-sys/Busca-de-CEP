def test_cep_valido(client):
    resp = client.get("/api/cep/01001000")
    assert resp.status_code == 201

    data = resp.get_json()
    assert "logradouro" in data['data']

def test_cep_invalido(client):
    resp = client.get("/api/cep/00000000")
    assert resp.status_code == 400

def test_cep_cache(client):
    client.get("/api/cep/01001000")
    resp = client.get("/api/cep/01001000")

    assert resp.status_code == 200

def test_cep_error_format(client):
    resp = client.get("/api/cep/010010000")

    assert resp.status_code == 400