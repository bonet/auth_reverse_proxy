from flask import Flask, request, redirect, Response, render_template, jsonify, make_response

import requests, random, string
from datetime import datetime as dt

app = Flask(__name__)
app.config.from_object("config.settings")


@app.route('/')
def index():
    return 'Flask is running!'
