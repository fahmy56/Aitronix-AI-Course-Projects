from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, title, item_id, category, number_of_copies, available_copies, price):
        self.__title = title
        self.__item_id = item_id
        self.__category = category
        self.__number_of_copies = number_of_copies
        self.__available_copies = available_copies
        self.__price = price

    @property
    def title(self):
        return self.__title
    
    @property
    def item_id(self):
        return self.__item_id
    
    @property
    def category(self):
        return self.__category
    
    @property
    def number_of_copies(self):
        return self.__number_of_copies
    
    @property
    def available_copies(self):
        return self.__available_copies
    
    @property
    def price(self):
        return self.__price
    
    @number_of_copies.setter
    def number_of_copies(self, value):
        if value >= 0:
            self.__number_of_copies = value

    @available_copies.setter
    def available_copies(self, value):
        if value >= 0:
            self.__available_copies = value

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value

    def check_availability(self):
        return self.__available_copies > 0
        
    @abstractmethod
    def display_info(self):
        pass