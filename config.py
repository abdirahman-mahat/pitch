import os

class Config:
    SECRET_kEY='1234'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abdirahman:1234@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class prodConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abdirahman:1234@localhost/pitch_test'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abdirahman:1234@localhost/pitch'
    DEBUG = True

config_options = {
   
'development': DevConfig,
'production': prodConfig,
'test': TestConfig
}