from app import db

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
	email = db.Column(db.String(120), unique=True)
	website = db.Column(db.String(120))
	role = db.Column(db.SmallInteger, default=ROLE_USER)
	cv = db.Column(db.String(120))

	#pwdhash = db.Column(db.String(64)
	#posts = db.relationship('Post', backref = 'user_id', lazy = 'dynamic')
	def __repr__(self):
		return '<User %r>' % (self.nickname)

	#def __init__(self, ):
	#	self.nickname
	#	self.email = email.lower()
	#	self.set_password(password)

	#def is_authenticated(self):
	#	return True

	#def is_active(self):
	#	return True

	#def is_anonymous(self):
	#	return False

	#def get_id(self):
	#	return unicode(self.id)


class Papers(db.Model):
	__tablename__ = 'papers'
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	citation = db.Column(db.String(500), index=True, unique=True)
	link = db.Column(db.String(300), index=True, unique=True)
	abstract = db.Column(db.String(1000), index = True)
	year = db.Column(db.Integer)
	code = db.Column(db.String(300), index=True, unique=True)
	data = db.Column(db.String(300), index=True, unique=True)

	def __repr__(self):
		return '<Papers %r>' % (self.nickname)

#class Post(db.Model):
#	id = db.Column(db.Integer, primary_key = True)
#	body = db.Column(db.String(140))
#	timestamp = db.Column(db.DateTime)
#	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#	def __repr__(self):
#		return '<Post %r>' % (self.body)
