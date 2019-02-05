class DevelopmentConfig():
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8080
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/PhillyPhoodies'
    SECRET_TOKEN = 'SECRET TOKEN'

