"""empty message

Revision ID: 7a4526a1eb30
Revises: 352cb746332a
Create Date: 2019-02-10 18:47:14.300006

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7a4526a1eb30'
down_revision = '352cb746332a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_foreign_key(None, 'tagmap', 'papers', ['paper_id'], ['id'])
    # op.alter_column('users', 'email',
    #            existing_type=mysql.VARCHAR(length=120),
    #            nullable=False)
    # ### end Alembic commands ###
    pass

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    op.drop_constraint(None, 'tagmap', type_='foreignkey')
    # ### end Alembic commands ###
