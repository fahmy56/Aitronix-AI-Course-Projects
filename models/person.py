from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, person_id, phone_number, email):
        self.__name = name
        self.__person_id = person_id
        self.__phone_number = phone_number
        self.__email = email
    
    @property
    def name(self):
        return self.__name
    
    @property
    def person_id(self):
        return self.__person_id
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @property
    def email(self):
        return self.__email
    
    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @email.setter
    def email(self, value):
        self.__email = value

    @abstractmethod
    def display_info(self):
        pass