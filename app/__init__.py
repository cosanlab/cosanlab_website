import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Shell, Manager
import imp

# from flask import Flask, render_template_string, redirect
# from sqlalchemy import create_engine, MetaData
from flask.ext.login import UserMixin, LoginManager, login_user, logout_user
from flask.ext.blogging import SQLAStorage, BloggingEngine

basedir = '/Users/lukechang/Github/cosanlab_web'
# basedir = '/home/lukcha5/cosanlab'
keypath = imp.load_source('keys', os.path.join(basedir,'keys.py'))
keys = keypath.Keys()

app = Flask(__name__)
app.secret_key = keys.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = keys.SQLALCHEMY_DATABASE_URI
# app.config["BLOGGING_URL_PREFIX"] = "/blog"
# app.config["BLOGGING_DISQUS_SITENAME"] = "test"
# app.config["BLOGGING_SITEURL"] = "http://localhost:8000"
# app.config.from_object('config')
db = SQLAlchemy(app)
manager = Manager(app)

from app import views, models

@app.context_processor
def utility_processor():
	def get_paper_by_year(year):
		dat = models.Papers.query.filter_by(year = year)
		return dat
	return dict(get_paper_by_year=get_paper_by_year)
@app.context_processor
def utility_processor2():
	def get_person_by_title(title):
		dat = models.User.query.filter_by(title = title)
		return dat
	return dict(get_person_by_title=get_person_by_title)
