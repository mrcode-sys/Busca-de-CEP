from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route("/api/cep/<val>")
def search_cep(val):
    url = f"https://viacep.com.br/ws/{val}/json/"
    resp = requests.get(url)

    if resp.status_code != 200:
        return jsonify({"erro":True}), 502

    dados = resp.json()
    if "erro" in dados:
        return jsonify({"erro":True}), 400
    
    return jsonify(dados)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)