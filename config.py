class DevelopmentConfig():
    DEBUG = True
    PORT = 5001
    MYSQL_HOST = 'localhost'
    # MYSQL_USER = 'root'
    # MYSQL_DB = 'loginRest'
    MYSQL_USER = 'b6c581180a5036'
    MYSQL_PASSWORD = '6590ad23'
    MYSQL_DB = 'heroku_2f678db4338be62'


config = {
    'development': DevelopmentConfig
}