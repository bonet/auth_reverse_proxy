from flask import Flask, request, redirect, Response, render_template, jsonify, make_response

import requests, random, string
from datetime import datetime as dt

from libs.extensions import db

app = Flask(__name__)
app.config.from_object("config.settings")
db.init_app(app)


@app.route('/')
def index():
    return 'Flask is running!'


