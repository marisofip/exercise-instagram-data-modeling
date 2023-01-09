import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

	
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    url = Column(String(250), nullable=False)
    description = Column(String(800), nullable=False)
    user = relationship('User', back_populates='post')
   
class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    description = Column(String(800), nullable=False)
    user = relationship('User', back_populates='comment')
    post = relationship('Post', back_populates='comment')
	
class Like(Base):
    __tablename__ = 'like'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'),nullable=False)
    description = Column(String(800), nullable=False)
    user = relationship('User', back_populates='like')
    post = relationship('Post', back_populates='like')


class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    user_to = relationship('User', back_populates='followers')
    user_from = relationship('User', back_populates='followers')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
