# -*- coding: utf-8 -*-

import sys as _sys

class Config():

    def __init__(self):
        
        self.available_modes = {'PROD': ProductionConfig,
                                'DEV' : DevConfig}
        
        self.app_name = 'GenericBackend'
        
    def setConfiguration(self, mode):
        if mode == 'PROD':
            return self.available_modes['PROD']
        elif mode == 'DEV':
            return self.available_modes['DEV']
        else:
            print('Mode: %s is invalid. Set mode to PROD or DEV')
            _sys.exit(0)
        
class ProductionConfig(Config):
    
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_ECHO = False

    
class DevConfig(Config):

    ENV = 'development'
    DEBUG = True        
    SQLALCHEMY_ECHO = True 