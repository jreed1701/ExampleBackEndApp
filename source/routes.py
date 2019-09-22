# -*- coding: utf-8 -*-
from source.config import Config
from flask import Blueprint

app = Blueprint('app', Config().app_name)

@app.route('/hello')
def hello():
    print('something happened')
    return 'Hello World'