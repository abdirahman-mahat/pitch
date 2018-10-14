import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://abdirahman:1234@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("abdirahmanmahat3@gmail.com")
    MAIL_PASSWORD = os.environ.get("abdirahmanun11")
class prodConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':prodConfig
}