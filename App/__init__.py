from flask import Flask
from App import settings
from App.ext import init_ext


def create_apps(ENV_NAME):
    app=Flask(__name__)

    # 选择开发环境以及数据库的选择和配置
    app.config.from_object(settings.env.get(ENV_NAME))

    # 第三方库的整合
    init_ext(app=app)

    return app

