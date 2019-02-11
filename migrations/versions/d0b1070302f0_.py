"""empty message

Revision ID: d0b1070302f0
Revises: 94b1d3b647ac
Create Date: 2019-02-09 16:51:32.185582

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd0b1070302f0'
down_revision = '94b1d3b647ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('positions',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('position', sa.String(length=100), nullable=True),
    # sa.Column('description', sa.String(length=500), nullable=True),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.create_table('resources',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('type', sa.String(length=300), nullable=True),
    # sa.Column('name', sa.String(length=300), nullable=True),
    # sa.Column('description', sa.String(length=500), nullable=True),
    # sa.Column('link', sa.String(length=300), nullable=False),
    # sa.PrimaryKeyConstraint('id')
    # )
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
    op.drop_table('resources')
    op.drop_table('positions')
    # ### end Alembic commands ###