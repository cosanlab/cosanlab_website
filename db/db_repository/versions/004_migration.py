from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
papers = Table('papers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('citation', VARCHAR(length=500)),
    Column('link', VARCHAR(length=300)),
    Column('abstract', VARCHAR(length=2000)),
    Column('year', INTEGER),
)

post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('title', VARCHAR(length=120)),
    Column('bio', VARCHAR(length=500)),
    Column('pic', VARCHAR(length=120)),
    Column('email', VARCHAR(length=120)),
    Column('website', VARCHAR(length=120)),
    Column('role', SMALLINT),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['papers'].drop()
    pre_meta.tables['post'].drop()
    pre_meta.tables['user'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['papers'].create()
    pre_meta.tables['post'].create()
    pre_meta.tables['user'].create()
