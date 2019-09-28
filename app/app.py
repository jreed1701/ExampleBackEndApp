# -*- coding: utf-8 -*-
import os as _os
import sqlalchemy as db

from config import app_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(app_config[_os.environ['ENV']].DATABASE_PATH, convert_unicode = True)
    
db_session = scoped_session(sessionmaker(autocommit = False,
                                         autoflush = False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

