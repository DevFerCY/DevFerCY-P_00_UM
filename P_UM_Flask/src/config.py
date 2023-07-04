
# clase para las configuaraciones de Desarrollo
class Config:
    SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_Host = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'agenda_db_01'

config = { 'development': DevelopmentConfig }