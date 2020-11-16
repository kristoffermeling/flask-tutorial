from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '31e5cd5d36311385803ff8dae5f2edc6'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER']= 'smtp.googlemail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USERNAME']='kristoffermeling1@gmail.com'                    #os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']= ''                   #os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog import routes