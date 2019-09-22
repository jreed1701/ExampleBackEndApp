# -*- coding: utf-8 -*-

from flask import Flask
from source.config import Config

class Launcher():
    
    def __init__(self):
        
        self.app = None
        self.db = None
    
    def create_app(self, config_str='UNSET'):
        
        config = Config()
        
        self.app = Flask(config.app_name, instance_relative_config=True)
        self.app.config.from_object(config.setConfiguration(config_str))
        
        return self.app

        
    def run_app(self, config_str='UNSET'):
        
        self.create_app(config_str)
        
        self.app.run()
        