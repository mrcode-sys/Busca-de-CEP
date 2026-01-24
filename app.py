from flask import Flask, jsonify, request, render_template
import requests
from routes.cep import cep_bp
app = Flask(__name__)

app.register_blueprint(cep_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)