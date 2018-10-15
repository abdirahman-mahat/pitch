import os

class Config:
<<<<<<< HEAD
    SECRET_KEY='1234'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
    SECRET_kEY='1234'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abdirahman:1234@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
<<<<<<< HEAD
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abdirahman:1234@localhost/pitch_test'

=======
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class prodConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abdirahman:1234@localhost/pitch_test'


>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abdirahman:1234@localhost/pitch'
    DEBUG = True

config_options = {
<<<<<<< HEAD
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
=======
   
'development': DevConfig,
'production': prodConfig,
'test': TestConfig
}
>>>>>>> af6b453f4f3974552e1f96fecffab63a657ef23b
