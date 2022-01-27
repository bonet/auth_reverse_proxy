from flask import Flask, request, redirect, Response, render_template, jsonify, \
    current_app, make_response

import requests, random, string
from datetime import datetime as dt
import json

from libs.extensions import db

from oauth2_token.models import OAuth2Token

app = Flask(__name__)
app.config.from_object("config.settings")
db.init_app(app)


@app.route('/')
def index():
    OAuth2Token.find_by_access_token(db.session, '', '')
    return 'Flask Reverse Proxy is running!'


@app.route('/<path:path>',methods=['GET','POST','DELETE'])
def proxy(path):
    global SITE_NAME
    user_id = request.headers.get('UID')
    access_token = None
    auth_header = request.headers.get('Authorization')

    if auth_header:
        auth_header_arr = auth_header.split()
        access_token = auth_header_arr[-1]

    if user_id and access_token:
        initial_headers = {
                'UID': request.headers.get('UID'),
                'Content-Type': request.headers.get('Content-Type'),
                'Authorization': auth_header
            }

        api_url = 'http://' + current_app.config['API_HOST'] + '/' + path

        token = OAuth2Token.find_by_access_token(db.session, access_token, user_id)
        if request.method=='GET':
            resp = requests.get(api_url, headers=initial_headers)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response
        elif request.method=='POST':
            resp = requests.post(api_url,json=request.get_json(), headers=initial_headers)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response
        elif request.method=='DELETE':
            resp = requests.delete(api_url).content
            response = Response(resp.content, resp.status_code, headers)
            return response
    else:
        return make_response(jsonify({
                'Status': 'Error'
            }), 401)
