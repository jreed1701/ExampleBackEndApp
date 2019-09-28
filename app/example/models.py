# -*- coding: utf-8 -*-
import sqlalchemy as db

from app.common.tools import PaginatedApi, JsonDbSupport
from app.app import Base

class ExampleModel(PaginatedApi, JsonDbSupport, Base):

    __tablename__ = 'example'
    
    id = db.Column(db.Integer, primary_key = True)
    
    field1 = db.Column(db.String(256), nullable=True)
    
    def __repr__(self):
        return '<Example ID{}>'.format(self.id)
    
    def from_dict(self, data, new_entry=False):
        
        for column in self.__table__.columns:
            
            field = column.key
            
            if field == 'id':
                continue
            
            if field in data:
                setattr(self, field, data[field])
                
    def to_dict(self, allData = 0 ):
        
        data = {}
        
        for column in self.__table__.column:
            
            field = column.key
            
            if getattr(self, field) == []:
                continue
            
            data[field] = getattr(self, field)
            
        return data