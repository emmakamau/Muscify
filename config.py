## Configuration files 
import os

class Config:
    password = os.environ.get('SQL_PASSWORD')

    SQLALCHEMY_DATABASE_URI = ''
    SECRET_KEY = os.environ.get('SECRET_KEY')

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    pass

class ProdConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://", 1)
    pass

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = ''
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
