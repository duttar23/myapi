from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

#Init api
api = Flask(__name__)

@api.route('/', methods=['GET'])
def get():
    return jsonify({ 'msg': 'Hello World' })

# Run Server
if __name__ == '__main__':
    api.run(debug=True)