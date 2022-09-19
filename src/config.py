class DevelopmentConfig():
    DEBUG = True
    PORT = 5001
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_DB = 'loginRest'

config = {
    'development': DevelopmentConfig
}