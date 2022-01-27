# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SERVER_NAME = env.str("URL_HOST")
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
FLASK_APP = env.str("FLASK_APP")
API_HOST = env.str("API_HOST")
SQLALCHEMY_TRACK_MODIFICATIONS = True
