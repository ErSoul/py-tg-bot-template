import os
from sqlalchemy import Engine, Integer, String, Table, Column, create_engine, MetaData

def initialize_database() -> Engine:
    engine = create_engine(os.getenv("DATABASE"), echo=False)
    metadata = MetaData() # extracting the metadata

    Table('users', metadata,
            Column('id', Integer(), primary_key=True, autoincrement=False),
            Column('username', String),
            Column('phone_number', String, nullable=True)
        )
    
    Table('channels', metadata,
            Column('id', Integer(), primary_key=True, autoincrement=False),
            Column('name', String),
        )
    
    Table('groups', metadata,
            Column('id', Integer(), primary_key=True, autoincrement=False),
            Column('name', String),
        )

    metadata.create_all(engine)
    return engine
