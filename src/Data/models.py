from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer(), primary_key=True, autoincrement=False)
    username = Column('username', String)
    phone_number = Column('phone_number', String, nullable=True)

    def __repr__(self):
        return '<Users: %r>' % (self.title)
    
class Channel(Base):
    __tablename__ = 'channels'

    id = Column('id', Integer(), primary_key=True, autoincrement=False)
    name = Column('name', String)

    def __repr__(self):
        return '<Channel: %r>' % (self.name)

class Group(Base):
    __tablename__ = 'groups'

    id = Column('id', Integer(), primary_key=True, autoincrement=False)
    name = Column('name', String)

    def __repr__(self):
        return '<Group: %r>' % (self.name)
