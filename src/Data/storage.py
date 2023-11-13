from .models import User, Channel, Group
from abc import abstractmethod, ABCMeta

class Storage(metaclass=ABCMeta):
    @abstractmethod
    def getChannel(self, chat_id: int) -> Channel:
        pass

    @abstractmethod
    def saveChannel(self, chat_id: int, name: str) -> None:
        pass

    @abstractmethod
    def getGroup(self, chat_id: int) -> Group:
        pass

    @abstractmethod
    def saveGroup(self, chat_id: int, name: str) -> None:
        pass
    
    @abstractmethod
    def getUser(self, user_id: int) -> User:
        pass

    @abstractmethod
    def saveUser(self, user_id: int, username: str) -> None:
        pass

    @abstractmethod
    def updateUserPhone(self, user_id: int, phone_number: str) -> bool:
        pass
