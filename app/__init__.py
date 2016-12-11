import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import imp

basedir = '/home/lukcha5/cosanlab'
keypath = imp.load_source('keys', os.path.join(basedir,'keys','keys.py'))
keys = keypath.Keys()

app = Flask(__name__)
app.secret_key = keys.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = keys.SQLALCHEMY_DATABASE_URI
# app.config.from_object('config')
db = SQLAlchemy(app)


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
