import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'
    MAIL_SERVER = os.environ.get('MAIL_SEVER', 'smtp.gmail.com')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS','true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SNS_MAIL_SUBJECT_PREFIX = '[SNS]'
    SNS_MAIL_SENDER = 'SNS Admin <example@gmail.com>'
    SNS_ADMIN = os.environ.get('SNS_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SNS_POSTS_PER_PAGE = 20
    SNS_FOLLOWERS_PER_PAGE = 50
    SNS_COMMENTS_PER_PAGE = 30


    @staticmethod
    def init_app(app):
        pass

    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///'
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}


