from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    Boolean,
    ForeignKey
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


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(250), nullable=False)
    vote = relationship("Vote", uselist=False)

Index('User.username_index', Users.username, unique=True, mysql_length=255)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    text = Column(Text)
    hash_url = Column(String(255))
    url = Column(String(250))
    is_link = Column(Boolean)
    votes = relationship("Vote")

Index('Post.hash_url_index', Posts.hash_url, unique=True, mysql_length=255)

class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    vote = Column(Integer)
