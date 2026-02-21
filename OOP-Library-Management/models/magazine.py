from models.item import Item

class Magazine(Item):
    def __init__(self, title, item_id, category, number_of_copies, available_copies, price, issue_number, publisher, publication_date):
        super().__init__(title, item_id, category, number_of_copies, available_copies, price)
        self.__issue_number = issue_number
        self.__publisher = publisher
        self.__publication_date = publication_date

    @property
    def issue_number(self):
        return self.__issue_number
    
    @property
    def publisher(self):
        return self.__publisher
    
    @property
    def publication_date(self):
        return self.__publication_date
    
    def display_info(self):
        print("Magazine Information:")
        print(f"\tTitle: {self.title}")
        print(f"\tID: {self.item_id}")
        print(f"\tPublisher: {self.__publisher}")
        print(f"\tPublication Date: {self.__publication_date}")
        print(f"\tIssue Number: {self.__issue_number}")
        print(f"\tCategory: {self.category}")
        print(f"\tPrice: ${self.price:.2f}")
        print(f"\tTotal Copies: {self.number_of_copies}")
        print(f"\tAvailable Copies: {self.available_copies}\n") 