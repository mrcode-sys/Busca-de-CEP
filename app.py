from flask import Flask, render_template
from extensions import db
from config import Config
from routes.cep import cep_bp
from flask_migrate import Migrate
from errors.errors import AppError
from utils.responses import error_response

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(cep_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(AppError)
def handle_app_error(error):
    app.logger.exception(error)
    return error_response(error.code, error.status_code)

if __name__ == "__main__":
    app.run(debug=True)