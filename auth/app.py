from flask import Flask, request, redirect, Response, render_template
from flask_login import login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import requests, random

from libs.extensions import db, migrate

from user.models import User
from oauth2_token.models import OAuth2Token

app = Flask(__name__)
app.config.from_object("config.settings")
db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/api/v1/auth',methods=['GET', 'POST'])
def login():
    callback_url=request.args.get('callback_url')
    client_access_token=request.args.get('client_access_token')

    if request.method == 'POST':
        user = User.query.filter(
            User.email==request.args.get('email'),
            User.password==request.args.get('password').encode('ascii')
            ).one_or_none()

        auth_code = ''.join(random.SystemRandom().choice(string.hexdigits) for _ in range(32))
        oauth2_token = OAuth2Token.query.filter(OAuth2Token.user_id == user.id).one_or_none()
        if oauth2_token:
            oauth2_token.auth_code = auth_code
        else:
            oauth2_token = OAuth2Token(
                    user_id = user.id,
                    auth_code = auth_code
                )

        db.session.add(oauth2_token)

        register_user = (user.fullname == None ||
            user.address == None ||
            user.phonw == None) ? 1 : 0

        if(user):
            return redirect("/form/v1/allow_form",
                    auth_code=auth_code,
                    callback_url=callback_url,
                    client_access_token=client_access_token
                )
        else:
            return render_template("login_form.html",
                    callback_url=callback_url,
                    client_access_token=client_access_token
                )

    else:
        return render_template("login_form.html",
                callback_url=callback_url,
                client_access_token=client_access_token
            )


@app.route('/form/v1/allow_form',methods=['GET'])
def allow_form():
    callback_url=request.args.get('callback_url')
    client_access_token=request.args.get('client_access_token')

    return render_template("allow_form.html",
            callback_url=callback_url,
            client_access_token=client_access_token,
            register_user=register_user
        )


@app.route('/api/v1/get_token',methods=['POST'])
def get_token():
    auth_code = request.args.get('auth_code')
    oauth2_token = OAuth2Token.query.filter(OAuth2Token.user_id == user.id).one_or_none()
