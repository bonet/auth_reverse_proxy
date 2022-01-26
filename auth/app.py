from flask import Flask, request, redirect, Response, render_template, jsonify, make_response
from flask_login import login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import requests, random, string
from datetime import datetime as dt

from libs.extensions import db, migrate

from user.models import User
from partner.models import Partner
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

    if request.method == 'POST':
        callback_url=request.form.get('callback_url')
        client_access_token=request.form.get('client_access_token')
        partner_id=request.form.get('partner_id')

        user = User.query.filter(
            User.email==request.form.get('email'),
            User.password==request.form.get('password').encode('ascii')
            ).one_or_none()

        partner = Partner.query.filter(
            Partner.id==partner_id
            ).one_or_none()

        if(user and partner):
            auth_code = ''.join(random.SystemRandom().choice(string.hexdigits) for _ in range(32))
            access_token = ''.join(random.SystemRandom().choice(string.hexdigits) for _ in range(32))
            oauth2_token = OAuth2Token.query.filter(OAuth2Token.user_id == user.id).one_or_none()

            oauth2_token = oauth2_token or OAuth2Token()
            oauth2_token.user_id = user.id
            oauth2_token.partner_id = partner.id
            oauth2_token.auth_code = auth_code
            oauth2_token.access_token = access_token
            oauth2_token.issued_at = dt.utcnow().timestamp()
            oauth2_token.expires_in = 3600

            db.session.add(oauth2_token)
            db.session.commit()

            register_user = 1 if (user.fullname == None or
                user.address == None or
                user.phone == None) else 0

            return redirect(f"/form/v1/allow_form?auth_code={auth_code}&callback_url={callback_url}&client_access_token={client_access_token}&register_user={register_user}")
        else:
            return render_template("login_form.html",
                    callback_url=callback_url,
                    client_access_token=client_access_token,
                    partner_id=partner_id
                )

    else:
        callback_url=request.args.get('callback_url')
        client_access_token=request.args.get('client_access_token')
        partner_id=request.args.get('partner_id')

        return render_template("login_form.html",
                callback_url=callback_url,
                client_access_token=client_access_token,
                partner_id=partner_id
            )


@app.route('/form/v1/allow_form',methods=['GET'])
def allow_form():
    callback_url=request.args.get('callback_url')
    client_access_token=request.args.get('client_access_token')
    auth_code=request.args.get('auth_code')
    register_user=request.args.get('register_user')

    return render_template("allow_form.html",
            auth_code=auth_code,
            callback_url=callback_url,
            client_access_token=client_access_token,
            register_user=register_user
        )


# Ideally this is Partner's callback API, not client-facing API
# Partner server will be whitelisted on our backend server address
@app.route('/api/v1/get_token',methods=['POST'])
def get_token():
    auth_code = request.form.get('auth_code')
    client_id = request.form.get('client_id')
    partner_id = request.form.get('partner_id')
    partner_secret_key = request.form.get('partner_secret_key')
    user_id = request.form.get('user_id')
    register_user = request.form.get('register_user')
    full_name = request.form.get('full_name')
    address = request.form.get('address')
    phone = request.form.get('phone')

    oauth2_token = OAuth2Token.query.filter(OAuth2Token.user_id == user_id,
        OAuth2Token.auth_code == auth_code
        ).one_or_none()

    return make_response(jsonify({
                'access_token': oauth2_token.access_token,
                'expire': (oauth2_token.issued_at + 3600)
            }), 200)
