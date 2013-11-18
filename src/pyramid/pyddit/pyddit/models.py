from sqlalchemy import (
    Column,
    Index,
    Integer,
    String
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    hash_url = Column(String(255))
    url = Column(String(250), nullable=False)
    votes = Column(Integer, default=0)

Index('Post.hash_url_index', Post.hash_url, unique=True, mysql_length=255)
