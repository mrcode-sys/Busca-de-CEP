from flask import Flask, render_template, jsonify
from extensions import db
from flask_migrate import Migrate
from routes.cep import cep_bp
from errors.errors import ExternalAPIError, InvalidCEPError
from utils.responses import error_response
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(cep_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(InvalidCEPError)
def handle_inv_cep_error(error):
    return error_response("CEP Inválido", 400)

@app.errorhandler(ExternalAPIError)
def handle_ext_api_error(error):
    return error_response("Falha ao consultar serviço externo", 503)

@app.errorhandler(Exception)
def handle_generic_error(error):
    app.logger.exception(error)
    return error_response("Erro interno", 500)

if __name__ == "__main__":
    app.run(debug=True)