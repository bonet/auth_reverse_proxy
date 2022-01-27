# -*- coding: utf-8 -*-
import pytest, logging

from libs.database import db as _db
from flask import Flask
from user.models import User

print("HELLO OELD")
@pytest.fixture
def app():
    """Create application for the tests."""
    _app = Flask(__name__)
    _app.config.from_object("tests.settings")
    _app.logger.setLevel(logging.CRITICAL)
    _db.init_app(_app)


    print("HELLO")
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def db(app):
    """Create database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()



@pytest.fixture
def initial_user(db):
    return User.create(email='jdoe@example.com', password='hello123'.encode('ascii'))
