from flask import Flask, render_template, flash, redirect, url_for,session
from flask import request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class Config(object):
    # .......
    # 格式为mysql+pymysql://数据库用户名:密码@数据库地址:端口号/数据库的名字?数据库格式
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/paper_web?charset=utf8'
    # 如果你不打算使用mysql，使用这个连接sqlite也可以
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = '我是密码'
db = SQLAlchemy(app)
