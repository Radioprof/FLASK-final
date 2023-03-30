from flask import Flask
from flask_migrate import Migrate

from blog.api import init_api
# from flask_wtf import CSRFProtect

from blog.views.article import articles_app
from blog.views.auth import auth_app, login_manager
from blog.views.authors import authors_app
from blog.views.users import users_app
from blog.views.admin import admin_app, admin

from blog.models.database import db
# import os


app = Flask(__name__)


# cfg_name = os.environ.get('TestingConfig')
# app.config.from_object(f"blog.configs.{cfg_name}")


app.register_blueprint(users_app)
app.register_blueprint(articles_app)
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(authors_app)
app.register_blueprint(admin_app)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\UCHEBA\\PYTHON PROJECT\\FLASK_PROJECT\\instance\\blog.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sergey:QoJ3CDZJWP8wAsZcSQ4VZLIyIrM7e0JR@dpg-cgi90e7dvk4vd51khm80-a/db_kiyl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '(cb!h&a)y8j*i-x62*d#t@3u2t!%6^5c8=n9l3339y)7gq&+o)'
app.config['WTF_CSRF_ENABLE'] = True
app.config['FLASK_ADMIN_SWATCH'] = 'LUX'
app.config['OPENAPI_URL_PREFIX'] = '/api/docs'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
app.config['OPENAPI_SWAGGER_UI_VERSION'] = '3.22.0'


db.init_app(app)

migrate = Migrate(app, db, compare_type=True)

login_manager.init_app(app)
# csrf = CSRFProtect(app)

admin.init_app(app)

api = init_api(app)
