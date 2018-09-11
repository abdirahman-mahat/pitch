import os

class Config:
    SECRET_KEY='01570936bd6b231dd1e1037bb224cd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://zamzam:Ilovememore100@localhost/pitchperfect_test'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://zamzam:Ilovememore100@localhost/pitchperfect'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}    