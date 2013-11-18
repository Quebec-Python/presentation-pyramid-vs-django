"""Adding fake posts

Revision ID: 2533675381c7
Revises: 5016cbd63638
Create Date: 2013-11-18 04:36:11.715178

"""

# revision identifiers, used by Alembic.
revision = '2533675381c7'
down_revision = '5016cbd63638'

from alembic import op
import sqlalchemy as sa

from pyramid.paster import get_appsettings, setup_logging
import transaction
from pyddit.models import (DBSession, Post, Base)
from pyddit.helpers import create_hashed_url

config_uri = "/opt/pyramid/pyddit/development.ini"

title1 = "All hail Twitter bootstrap 3.0"
title2 = "All hail Zurb Foundation"

def upgrade():
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = sa.engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    with transaction.manager:

        p1 = Post(
            title=title1,
            hash_url= create_hashed_url(title1),
            url="http://getbootstrap.com/",
            votes=100
        )
        DBSession.add(p1)

        p2 = Post(
            title=title2,
            hash_url= create_hashed_url(title2),
            url="http://foundation.zurb.com/",
            votes=101
        )
        DBSession.add(p2)

def downgrade():
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = sa.engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        post1 = Post.get(title=title1)
        DBSession.delete(post1)
        post2 = Post.get(title=title2)
        DBSession.delete(post2)
