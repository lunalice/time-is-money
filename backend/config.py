import os
from os.path import join, dirname
from dotenv import load_dotenv
from IPython import embed

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 280, 'pool_timeout': 100, 'pool_pre_ping': True}
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'host': os.getenv('DB_HOST', 'localhost'),
        'db': os.getenv('DB_NAME', 'db'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig
