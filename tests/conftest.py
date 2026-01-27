import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app as f_app
from extensions import db

@pytest.fixture
def app():
    f_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with f_app.app_context():
        db.create_all()
        yield f_app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()