from abc import ABC, abstractmethod
from datetime import datetime

class Transaction(ABC):
    def __init__(self, transaction_id, date, member, item):
        self.__transaction_id = transaction_id
        self.__date = date
        self.__member = member
        self.__item = item

    @property
    def transaction_id(self):
        return self.__transaction_id
    
    @property
    def date(self):
        return self.__date
    
    @property
    def member(self):
        return self.__member
    
    @property
    def item(self):
        return self.__item

    @abstractmethod
    def process_transaction(self):
        pass

    @abstractmethod
    def display_transaction(self):
        pass