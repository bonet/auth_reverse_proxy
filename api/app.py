from flask import Flask, request, redirect, Response, render_template, jsonify, make_response

import requests, random, string
from datetime import datetime as dt

app = Flask(__name__)
app.config.from_object("config.settings")

with app.app_context():
    @app.route('/')
    def index():
        return 'Flask API Server is running!'

    @app.route('/api/v1/lists')
    def product_list():
        return 'this is api list'

    @app.route('/api/v1/detail/<product_id>')
    def product_detail(product_id):
        return f'this is api detail{product_id}'


    @app.route('/<path:path>')
    def catch_all(path):
        return 'this is catch_all'
