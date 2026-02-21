from models.transaction import Transaction

class BorrowTransaction(Transaction):
    def __init__(self, transaction_id, date, member, item, borrow_date, due_date):
        super().__init__(transaction_id, date, member, item)
        self.__borrow_date = borrow_date
        self.__due_date = due_date
        self.__return_date = None
        self.__fine = 0.0
        self.__is_returned = False

    @property
    def borrow_date(self):
        return self.__borrow_date
    
    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def return_date(self):
        return self.__return_date
    
    @property
    def fine(self):
        return self.__fine
    
    @property
    def is_returned(self):
        return self.__is_returned
    
    @return_date.setter
    def return_date(self, value):
        self.__return_date = value

    @fine.setter
    def fine(self, value):
        if value >= 0:
            self.__fine = value

    @is_returned.setter
    def is_returned(self, value):
        self.__is_returned = value

    def calculate_fine(self, days_late):
        if days_late > 0:
            self.__fine = days_late * 2
        else:
            self.__fine = 0
        return self.__fine
    
    def make_returned(self, return_date, days_late=0):
        self.__return_date = return_date
        self.__is_returned = True
        self.calculate_fine(days_late)

        if self.__fine > 0:
            print(f"Book returned late, Fine: ${self.__fine:0.2f}")
        else:
            print(f"Book returned on time.")

    def process_transaction(self):
        if self.item.available_copies > 0:
            self.item.available_copies = self.item.available_copies - 1
            print(f"'{self.item.title}' borrowed by {self.member.name}")
            return True
        else:
            print(f"'{self.item.title}' not available")
            return False
        
    def display_transaction(self):
        print("\n" + "="*50)
        print("BORROW TRANSACTION")
        print("\n" + "="*50)
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Member: {self.member.name}")
        print(f"Item: {self.item.title}")
        print(f"Borrow Date: {self.__borrow_date}")
        print(f"Due Date: {self.__due_date}")

        if self.__is_returned:
            print(f"Return Date: {self.__return_date}")
            print(f"Fine: ${self.__fine:.2f}")
        else:
            print(f"Status: Not Returned Yet")
        print("="*50 + "\n")