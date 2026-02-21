from models.person import Person
from models.book import Book

class Member(Person):
    def __init__(self, name, person_id, phone_number, email, membership_date):
        super().__init__(name, person_id, phone_number, email)
        self.__membership_date = membership_date
        self.__borrowed_books = []
        self.__purchased_books = []
        self.__max_borrow_limit = 3

    @property
    def membership_date(self):
        return self.__membership_date
    
    @property
    def borrowed_books(self):
        return self.__borrowed_books
    
    @property
    def purchased_books(self):
        return self.__purchased_books
    
    @property
    def max_borrow_limit(self):
        return self.__max_borrow_limit
    
    def can_borrow(self):
        return len(self.borrowed_books) < self.max_borrow_limit
    
    def borrow_book(self, book):
        if self.can_borrow():
            self.borrowed_books.append(book)
            print(f"'{book.title}' added to your borrowing list successfully!")
        else:
            print(f"You've reached the maximum limit of {self.__max_borrow_limit} books.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"'{book.title}' returned successfully!")
        else:
            print(f"Error: '{book.title}' is not in your borrowed list.")

    def purchase_book(self, book):
        self.purchased_books.append(book)
        print(f"'{book.title}' purchased successfully!")

    def view_borrowed_books(self):
        if len(self.borrowed_books) == 0:
            print("No borrowed books.")
        else:
            print(f"\nBorrowed Books for {self.name}:")
            for book in self.borrowed_books:
                print(f"\t{self.borrowed_books.index(book)+1}. {book.title} by {book.author}")

    def display_info(self):
        print("Member Information:")
        print(f"\tName: {self.name}")
        print(f"\tID: {self.person_id}")
        print(f"\tPhone: {self.phone_number}")
        print(f"\tEmail: {self.email}")
        print(f"\tMembership Date: {self.__membership_date}")
        print(f"\tBorrowed Books: {len(self.__borrowed_books)}/{self.__max_borrow_limit}")
        print(f"\tPurchased Books: {len(self.__purchased_books)}\n")