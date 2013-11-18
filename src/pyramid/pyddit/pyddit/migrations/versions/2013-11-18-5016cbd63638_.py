"""empty message

Revision ID: 5016cbd63638
Revises: None
Create Date: 2013-11-18 04:35:11.553400

"""

# revision identifiers, used by Alembic.
revision = '5016cbd63638'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('hash_url', sa.String(length=255), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    ### end Alembic commands ###
