# -*- coding: utf-8 -*-
import os as _os

from app.example.views import example
from config import app_config, Config
from flask import Flask

print(app_config[_os.environ['ENV']].DATABASE_PATH)

def create_app(config_name):

    app = Flask(Config.APP_NAME, instance_relative_config=True)
    
    app.config.from_object(app_config[config_name])
        
    print('Database path is: %s' % app.config['DATABASE_PATH'])
        
    app.register_blueprint(example)
    
    return app