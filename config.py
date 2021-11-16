import os 

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://levy:123456@localhost/blog_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://levy:123456@localhost/blog'
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}