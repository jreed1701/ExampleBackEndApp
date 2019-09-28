# -*- coding: utf-8 -*-
import os as _os

class Config(object):
        
    APP_NAME = 'GenericBackend'
        
class ProductionConfig(Config):
    
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_ECHO = False
    DATABASE_PATH = 'sqlite:///%s/db/%s.db' % (_os.path.abspath(_os.getcwd()), 'prod')

    
class DevConfig(Config):

    ENV = 'development'
    DEBUG = True        
    SQLALCHEMY_ECHO = True 
    DATABASE_PATH = 'sqlite:///%s/db/%s.db' % (_os.path.abspath(_os.getcwd()), 'dev')
    
    
app_config = {'PROD': ProductionConfig,
              'DEV' : DevConfig}