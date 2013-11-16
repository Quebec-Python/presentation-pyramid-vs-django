"""add test users

Revision ID: 50696bd2ccef
Revises: 36a843f466c0
Create Date: 2013-11-16 05:02:37.821575

"""

# revision identifiers, used by Alembic.
revision = '50696bd2ccef'
down_revision = '36a843f466c0'

from alembic import op
import sqlalchemy as sa

from pyramid.paster import get_appsettings, setup_logging

import transaction
from pyddit.models import (DBSession, User, Base)

config_uri = "/opt/pyramid/pyddit/development.ini"

def upgrade():
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = sa.engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        user = User(username='vagrant1', email="vagrant1@gmail.com", password="vagrant1")
        DBSession.add(user)
        user_2 = User(username='vagrant2', email="vagrant2@gmail.com", password="vagrant2")
        DBSession.add(user_2)

def downgrade():
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = sa.engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    vagrant1 = User.get(username="vagrant1")
    DBSession.delete(vagrant1)
    vagrant2 = User.get(username="vagrant2")
    DBSession.delete(vagrant2)
    pass
