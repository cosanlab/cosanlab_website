from app import db
# from sqlalchemy.orm import relationship

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), unique=True)
	name = db.Column(db.String(64))
	title = db.Column(db.String(64))
	bio = db.Column(db.String(1000))
	pic = db.Column(db.String(120))
	email = db.Column(db.String(120), unique=True, nullable=False)
	website = db.Column(db.String(120), nullable=False)
	role = db.Column(db.SmallInteger, default=ROLE_USER)
	cv = db.Column(db.String(120), nullable=False)

	def __repr__(self):
		return self.nickname

class Tags(db.Model):
	__tablename__ = 'tags'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	def __repr__(self):
		return self.name

tagmap = db.Table('tagmap',
	db.Column('paper_id', db.Integer, db.ForeignKey('papers.id'), primary_key=True),
	db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

class Papers(db.Model):
	__tablename__ = 'papers'
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	citation = db.Column(db.String(300))
	link = db.Column(db.String(300))
	abstract = db.Column(db.String(500), nullable=False)
	year = db.Column(db.Integer)
	code = db.Column(db.String(300), nullable=False)
	data = db.Column(db.String(300), nullable=False)
	tags = db.relationship('Tags', secondary=tagmap, lazy='subquery',
		backref=db.backref('paper', order_by='Papers.year.desc()', lazy=True))

	def __repr__(self):
		return self.nickname

class Positions(db.Model):
	__tablename__ = 'positions'
	id = db.Column(db.Integer, primary_key=True)
	position = db.Column(db.String(300))
	description = db.Column(db.String(500))
	def __repr__(self):
		return self.position

class Resources(db.Model):
	__tablename__ = 'resources'
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(300))
	name = db.Column(db.String(300))
	description = db.Column(db.String(1500))
	link = db.Column(db.String(300), nullable=False)
	def __repr__(self):
		return self.name

class Teaching(db.Model):
	__tablename__ = 'teaching'
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(300))
	name = db.Column(db.String(300))
	description = db.Column(db.String(1500))
	syllabus = db.Column(db.String(300), nullable=False)
	code = db.Column(db.String(300), nullable=False)
	link = db.Column(db.String(300), nullable=False)
	def __repr__(self):
		return self.name

class Research(db.Model):
	__tablename__ = 'research'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(300))
	description = db.Column(db.String(1500))
	def __repr__(self):
		return (self.name)
