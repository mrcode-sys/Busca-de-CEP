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
