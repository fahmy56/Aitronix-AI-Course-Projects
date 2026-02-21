class Library:
    def __init__(self, name):
        self.__name = name
        self.__book_list = []
        self.__member_list = []
        self.__transaction_list = []

    @property
    def name(self):
        return self.__name

    def add_book(self, book):
        self.__book_list.append(book)
        print(f"'{book.title}' added to library.")

    def remove_book(self, book_id):
        for book in self.__book_list:
            if book.item_id == book_id:
                self.__book_list.remove(book)
                print(f"'{book.title}' removed.")
                return
        print(f"Book not found.")

    def register_member(self, member):
        self.__member_list.append(member)
        print(f"'{member.name}' registered.")

    def remove_member(self, member_id):
        for member in self.__member_list:
            if member.person_id == member_id:
                self.__member_list.remove(member)
                print(f"'{member.name}' removed.")
                return
        print(f"Member not found.")

    def show_available_books(self):
        print("\nAvailable Books:")
        for book in self.__book_list:
            if book.available_copies > 0:
                print(f"- {book.title} ({book.available_copies} available)")

    def search_book(self, title):
        for book in self.__book_list:
            if title.lower() in book.title.lower():
                print(f"Found: {book.title}")
                return book
        print("Book not found.")
        return None

    def process_transaction(self, transaction):
        if transaction.process_transaction():
            self.__transaction_list.append(transaction)

    def view_all_members(self):
        print("\nMembers:")
        for member in self.__member_list:
            print(f"- {member.name}")