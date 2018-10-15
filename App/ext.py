from flask_migrate import Migrate
from flask_restful import Api
from flask_session import Session
from App.apis import Hellos
from App.models import db

def init_ext(app):
    # migrate
    migrate = Migrate()
    migrate.init_app(app=app, db=db)

    #session
    app.config['SECRET_KEY']='100'
    app.config['SESSION_TYPE']='redis'
    Session(app=app)

    # 数据模型的初始化
    db.init_app(app=app)

    api = Api()
    #第一个参数是我们要操作的类
    #为什么为把Hello1写在了api中呢？因为增删该查都是在api中执行的
    api.add_resource(Hellos, '/hellos/')
    api.init_app(app=app)