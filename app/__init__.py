import os
from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell, Manager
from flask_migrate import Migrate
import imp

basedir = '/Users/lukechang/Github/cosanlab_web'
# basedir = '/home/lukcha5/cosanlab'
keypath = imp.load_source('keys', os.path.join(basedir,'keys.py'))
keys = keypath.Keys()

app = Flask(__name__)
app.secret_key = keys.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = keys.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = Manager(app)

migrate = Migrate(app, db)

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

@app.context_processor
def utility_processor3():
	def get_paper_by_tag(tag):
		dat = models.Tags.query.filter_by(name = tag)
		return dat
	return dict(get_paper_by_tag=get_paper_by_tag)
