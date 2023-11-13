from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from Data.storage import Storage
from Data.models import User, Channel, Group
from Data.database import initialize_database

from utils.logger import logger

logger = logger("sqlite")

class LiteStorage(Storage):
    def __init__(self):
        self._database = initialize_database()
        self._session = sessionmaker(self._database)
    
    def getChannel(self, chat_id) -> Channel:
        with self._session() as session:
            return session.execute(select(Channel).where(id == chat_id)).first()
        
    def saveChannel(self, chat_id, name: str) -> None:
        with self._session() as session:
            session.add(Channel( id= chat_id, name = name))
            try:
                session.commit()
            except IntegrityError as error:
                session.rollback()
                logger.error(error)

    def getGroup(self, chat_id) -> Group:
        with self._session() as session:
            return session.execute(select(Group).where(id == chat_id)).first()
        
    def saveGroup(self, chat_id, name: str) -> None:
        with self._session() as session:
            session.add(Group( id= chat_id, name = name))
            try:
                session.commit()
            except IntegrityError as error:
                session.rollback()
                logger.error(error)

    def getUser(self, user_id: int) -> User:
        with self._session() as session:
            return session.get(User, user_id)
        
    def saveUser(self, user_id: int, username: str) -> None:
        with self._session() as session:
            session.add(User(id = user_id, username = username))
            try:
                session.commit()
            except IntegrityError as error:
                session.rollback()
                logger.error(error)
                raise error # Handle error logic outside scope
    
    def updateUserPhone(self, user_id: int, phone_number: str) -> bool:
        with self._session() as session:
            user = session.get(User, user_id)
            user.phone_number = phone_number
            try:
                session.commit()
                return True
            except IntegrityError as error:
                session.rollback()
                logger.error(error)

            return False
