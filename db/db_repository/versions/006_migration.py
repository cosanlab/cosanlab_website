from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
	# Upgrade operations go here. Don't create your own engine; bind
	# migrate_engine to your metadata
	meta = MetaData(bind=migrate_engine)
	users = Table('users', meta, autoload=True)
	col = Column('1000')
	col.table = users
	col.alter(name='bio',type=String(1000))

def downgrade(migrate_engine):
	# Operations to reverse the above upgrade go here.
	meta = MetaData(bind=migrate_engine)
	users = Table('users', meta, autoload=True)
	col = Column('1000',String(500))
	#col.alter(users, name='bio')



