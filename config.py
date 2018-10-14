import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abdirahman:1234@localhost/pitch'
class prodConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':prodConfig
}