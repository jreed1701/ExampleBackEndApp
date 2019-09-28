# -*- coding: utf-8 -*-
import requests

from flask import Blueprint, request, jsonify, url_for
from app.example.models import ExampleModel
from app.common.tools import check_for_object
from app.database import db_session

example = Blueprint('app', __name__)

@example.route('/hello')
def hello():
    print('something happened')
    return 'Hello World'

@example.route('/examples', methods=['GET'])
def get_examples():
    
    page     = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 10000) #TODO Replace update limit
    all_data = request.args.get('all_data', 0, type=int)
    
    reqDict = request.args.copy()
    reqDict.pop('page', 1) # get value and remove key from dict
    reqDict.pop('per_page', 1)
    reqDict.pop('all_data', 1)
    
    ExampleModel.convert_from_strings(reqDict)
    
    if not reqDict:
        data = ExampleModel.to_collection_dict(ExampleModel.query, page, per_page, all_data, 'app.get_examples')
        return jsonify(data)
    else:
        newQuery = ExampleModel.query_filter_by(**reqDict)
        data = ExampleModel.to_collection_dict(newQuery, page, per_page, all_data, 'app.get_examples')
        return jsonify(data)
    
@example.route('/example/<int:id>', methods=['GET'])
def get_example(id):
        return jsonify(check_for_object(ExampleModel, ExampleModel.id == id).to_dict())

"""
@example.route('/example/add/<int:new>', methods=['GET', 'PUT'])
def add_example(new):
    
    if db_session.query(ExampleModel.id).filter_by(id = new) is not None:
        
        ex = ExampleModel()
        
        ex.id = new
        ex.field1 = 'Example String'
        
        db_session.add(ex)
        db_session.commit()
        
        #return url_for('app.get_example', variable=new)
    
        body = 'Success!'
        response = jsonify(body)
        response = requests.status_code = 201
        
        return response
        
    else:
        body = 'That example record already exists'
        
        response = jsonify(body)
        response = requests.status_code = 404
        
        return response
        
"""

