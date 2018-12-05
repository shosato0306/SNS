from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import Config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    # config.pyで定義したクラス(=config_nameで指定したクラス)の設定を
    # appにインポート
    app.config.from_object(Config[config_name])
    Config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # attach routes and custom error pages here
    from  .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
