## Configuration files 
import os

class Config:
    password = os.environ.get('SQL_PASSWORD')
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorraine:gift1234@localhost/muscify'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
=======
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:GenZ|0420@localhost/muscify'
    SECRET_KEY = os.environ.get('SECRET_KEY')
>>>>>>> 3cbe3e1109f8c04a547d85be025f6f851b5189d4
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    pass

class ProdConfig(Config):
<<<<<<< HEAD
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://", 1)
=======
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://", 1)
>>>>>>> 3cbe3e1109f8c04a547d85be025f6f851b5189d4
    pass

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
<<<<<<< HEAD
    # password = os.environ.get('SQL_PASSWORD')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:GenZ|0420@localhost/blog_test'
=======
    password = os.environ.get('SQL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:GenZ|0420@localhost/muscify_test'
>>>>>>> 3cbe3e1109f8c04a547d85be025f6f851b5189d4
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
