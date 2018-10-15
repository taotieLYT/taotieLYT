def get_db_uri(DATABASE):
    dialect=DATABASE.get('dialect') or 'mysql'
    mysql=DATABASE.get('mysql') or 'pymysql'
    username=DATABASE.get('username') or 'root'
    password=DATABASE.get('password') or '123456'
    host=DATABASE.get('host') or 'localhost'
    port=DATABASE.get('port') or '3306'
    db=DATABASE.get('db') or 'restful'
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,mysql,username,password,host,port,db)

class Config():
    TEST = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopeConfig(Config):
    DEBUG = True
    DATABASE = {
        'dialect': 'mysql',
        'mysql': 'pymysql',
        'username': 'root',
        'password': '123456',
        'host': 'localhost',
        'port': '3306',
        'db': 'restful',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class TestConfig(Config):
    TEST=True
    DATABASE={
        'dialect':'mysql',
        'mysql':'pymysql',
        'username':'root',
        'password':'123456',
        'host':'localhost',
        'port':'3306',
        'db':'restful',
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(DATABASE)

class ShowConfig(Config):
    DEBUG = True
    DATABASE = {
        'dialect': 'mysql',
        'mysql': 'pymysql',
        'username': 'root',
        'password': '123456',
        'host': 'localhost',
        'port': '3306',
        'db': 'restful',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class ProductConfig(Config):
    DEBUG = True
    DATABASE = {
        'dialect': 'mysql',
        'mysql': 'pymysql',
        'username': 'root',
        'password': '123456',
        'host': 'localhost',
        'port': '3306',
        'db': 'restful',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

env={
    'develop':DevelopeConfig,
    'test':TestConfig,
    'show':ShowConfig,
    'product':ProductConfig,
}