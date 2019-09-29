# -*- coding: utf-8 -*-
import sqlalchemy as db

from flask import url_for
from math import ceil
from sqlalchemy.orm import exc
from werkzeug.exceptions import abort

class Pagination(object):
    
    has_next = False
    has_prev = False
    items    = None
    page     = None
    pages    = None
    per_page = None
    prev_num = 0
    query    = None
    total    = None
    
    def paginate(query, page, per_page, unused):
        
        data = Pagination()
        
        print('Query: %s, page: %s, per_page: %s' % (query, page, per_page))
        
        if page == 0:
            page - 1
            
        data.total = query.count()
        data.pages = int(ceil(data.total / float(per_page)))
        
        newQuery = query.limit(per_page).offset((page-1)*per_page)
        data.items = newQuery.all()
        
        if page == 1:
            data.has_prev = False
        else:
            data.has_prev = True
            
        if page >= data.total:
            data.has_next = False
        else:
            data.has_next = True
            
        return data
    
class PaginatedApi(object):
    
    @staticmethod
    def to_collection_dict(query, page, per_page, all_data, endpoint, **kwargs):
        
        resources = Pagination.paginate(query, page, per_page, False)
        
        data = {
            'items' : [item.to_dict(all_data) for item in resources.items],
            '_meta' : {
                'page'        : page,
                'per_page'    : per_page,
                'total_pages' : resources.pages,
                'total_items' : resources.total
            },
            '_links' : {
                'self' : url_for(endpoint, page=page, per_page=page, **kwargs),
                'next' : url_for(endpoint, page=page + 1, per_page=page, **kwargs) if resources.has_next else None,
                'prev' : url_for(endpoint, page=page - 1, per_page=page, **kwargs) if resources.has_next else None
            }
        }
        
        return data
    
class JsonDbSupport(object):
    
    @classmethod
    def convert_from_strings(cls, inDict):
        # go through columsn
        for column in cls.__table__.columns:
            
            # if this column is in the input dict
            if column.key is inDict:
                #if it is in the dict and a float or int, convert from string
                if isinstance(column.type, db.Integer):
                    inDict[column.key] = int(inDict[column.key])
                if isinstance(column.type, db.Float):
                    inDict[column.key] = float(inDict[column.key])
                    
    @classmethod
    def to_empty_dict(cls):
        
        data = {}
        
        for column in cls.__table__.columns:
            
            field = column.key
            
            data[field] = None

        return data

    @classmethod
    def get_valid_columns(cls, column_names):
        return[cls.__table__.columns[name] for name in column_names if name in cls.__table__.columns]
        
        
def check_for_object(model, *criterion):
    try:
        return model.query.filter(*criterion).one()
    except exc.NoResultFound:
        abort(404)
    except exc.MultipleResultsFound:
        abort(404)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        