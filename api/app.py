from flask import Flask, request, redirect, Response, render_template, jsonify, make_response

import requests, random, string
from datetime import datetime as dt

app = Flask(__name__)
app.config.from_object("config.settings")

with app.app_context():
    @app.route('/')
    def index():
        return 'Flask API Server is running!'

    # Products
    @app.route('/api/v1/lists',methods=['GET'])
    def product_list():
        data_dict =  {
                        'products': [ {
                            'id':       1,
                            'title':    "product 1",
                            'picture_tumb': "https://picsum.photos/id/1/200/300",
                            'price':    "$40"
                        },
                        {
                            'id':       2,
                            'title':    "product 2",
                            'picture_tumb': "https://picsum.photos/id/2/200/300",
                            'price':    "$23"
                        }
                        ]
                    }
        return make_response(jsonify({
                'status': 'success',
                'data': data_dict
            }), 200)

    @app.route('/api/v1/detail/<product_id>',methods=['GET'])
    def product_detail(product_id):
        data_dict = {
                        'id':       product_id,
                        'title':    "product " + product_id,
                        'picture_tumb': "https://picsum.photos/id/"+product_id+"/200/300",
                        'price':    "$40"
                    }
        return make_response(jsonify({
                'status': 'success',
                'data': data_dict
            }), 200)



    # Orders
    @app.route('/api/v1/add_to_cart',methods=['POST'])
    def add_to_cart():
        return make_response(jsonify({
                'status': 'success',
                'message': 'Successfully add a product to cart'
            }), 200)

    @app.route('/api/v1/cart/detail/<user_id>',methods=['GET'])
    def cart_detail(user_id):
        data_dict =  {
                        'products': [ {
                            'id':       1,
                            'title':    "product 1",
                            'picture_tumb': "https://picsum.photos/id/1/200/300",
                            'price':    "$40",
                            'qty':      1
                        },
                        {
                            'id':       2,
                            'title':    "product 2",
                            'picture_tumb': "https://picsum.photos/id/2/200/300",
                            'price':    "$23",
                            'qty':      5
                        }
                        ]
                    }
        return make_response(jsonify({
                'status': 'success',
                'data': data_dict
            }), 200)

    @app.route('/api/v1/checkout',methods=['POST'])
    def checkout():
        return make_response(jsonify({
                'status': 'success',
                'message': 'Successfully add a product to cart'
            }), 200)


    @app.route('/<path:path>')
    def catch_all(path):
        return make_response(jsonify({
                'status': 'error'
            }), 404)
