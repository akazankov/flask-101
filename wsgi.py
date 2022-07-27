# wsgi.py
# pylint: disable=missing-docstring

from math import prod
from flask import Flask
from flask import jsonify, abort, request
app = Flask(__name__)


PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    return jsonify(list(PRODUCTS.values()))

# @app.route('/api/v1/products/<int:product_id>', methods = ['GET', 'DELETE'])
# def db_interaction(product_id):
#     if request.method == 'GET':
#         if product_id in PRODUCTS.keys():
#             return jsonify(PRODUCTS.get(product_id))
#         else:
#             abort(404)
#     elif request.method == 'DELETE':
#         if product_id in PRODUCTS.keys():
#             PRODUCTS.pop(product_id)
#             abort(204)
#         else:
#             abort(404)

@app.get('/api/v1/products/<int:product_id>')
def db_get(product_id):
    if product_id in PRODUCTS.keys():
        return jsonify(PRODUCTS.get(product_id))
    else:
        abort(404)

@app.delete('/api/v1/products/<int:product_id>')
def db_delete(product_id):
    if product_id in PRODUCTS.keys():
        PRODUCTS.pop(product_id)
        abort(204)
    else:
        abort(404)