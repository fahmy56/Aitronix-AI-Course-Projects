from models.item import Item

class Book(Item):

    def __init__(self, title, item_id, category, number_of_copies, available_copies, price, author, isbn, borrowing_price):
        super().__init__(title, item_id, category, number_of_copies, available_copies, price)
        self.__author = author
        self.__isbn = isbn
        self._borrowing_price = borrowing_price

    @property
    def author(self):
        return self.__author
    
    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def borrowing_price(self):
        return self._borrowing_price
    
    @borrowing_price.setter
    def borrowing_price(self, value):
        if value >= 0:
            self._borrowing_price = value

    def display_info(self):
        print("Book Information:")
        print(f"\tTitle: {self.title}")
        print(f"\tID: {self.item_id}")
        print(f"\tAuthor: {self.__author}")
        print(f"\tISBN: {self.__isbn}")
        print(f"\tCategory: {self.category}")
        print(f"\tPrice: ${self.price:.2f}")
        print(f"\tBorrowing Price: ${self._borrowing_price:.2f}")
        print(f"\tTotal Copies: {self.number_of_copies}")
        print(f"\tAvailable Copies: {self.available_copies}\n\n")