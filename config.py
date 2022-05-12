import os

class Config:
    '''
    '''
    # SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST='app/static/photos'



    #email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    '''
    SQLALCHEMY_DATABASE_URI='postgresql://zjiqwacgsmuivn:5b0a9ad83aa723d4e7391d1e667491eb482df7a26cf70af267f09a63459382d2'




class DevConfig(Config):
    '''
    '''

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://robert:Kirugik"79@localhost/pitching'


    DEBUG=True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}
