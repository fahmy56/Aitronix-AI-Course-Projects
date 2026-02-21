from models.book import Book
from models.magazine import Magazine
from models.member import Member
from models.librarian import Librarian
from models.borrow_transaction import BorrowTransaction
from models.purchase_transaction import PurchaseTransaction
from library import Library

# Create Library
print("="*50)
print("LIBRARY MANAGEMENT SYSTEM")
print("="*50)

lib = Library("City Library")
print(f"\nWelcome to {lib.name}!\n")

# Create Books
book1 = Book("Python Programming", "B001", "Programming", 10, 10, 50.0, "John Doe", "978-1234567890", 5.0)
book2 = Book("Data Science Basics", "B002", "Science", 5, 5, 45.0, "Jane Smith", "978-0987654321", 4.0)
magazine1 = Magazine("Tech Monthly", "M001", "Technology", 20, 20, 8.99, "Issue 245", "TechPress", "2024-01-15")

# Add to Library
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(magazine1)

# Create Members
member1 = Member("Ahmed Ali", "MEM001", "01012345678", "ahmed@email.com", "2024-01-01")
member2 = Member("Sara Mohamed", "MEM002", "01098765432", "sara@email.com", "2024-01-15")

# Register Members
lib.register_member(member1)
lib.register_member(member2)

# Create Librarian
librarian = Librarian("Khaled Hassan", "LIB001", "01055555555", "khaled@library.com", "EMP001", "Morning", 3000.0, "2020-01-01")

# Display Info
print("\n" + "="*50)
librarian.display_info()
member1.display_info()
book1.display_info()

# Show Available Books
lib.show_available_books()

# Borrow Book
print("\n--- BORROW TRANSACTION ---")
transaction1 = BorrowTransaction("T001", "2024-02-01", member1, book1, "2024-02-01", "2024-02-15")
lib.process_transaction(transaction1)
transaction1.display_transaction()

# Show Available Books After Borrow
lib.show_available_books()

# Return Book (on time)
print("\n--- RETURN BOOK ---")
transaction1.make_returned("2024-02-10", days_late=0)
transaction1.display_transaction()

# Purchase Book
print("\n--- PURCHASE TRANSACTION ---")
transaction2 = PurchaseTransaction("T002", "2024-02-05", member2, book2, 2)
lib.process_transaction(transaction2)
transaction2.display_transaction()

# View Members
lib.view_all_members()

# Search Book
print("\n--- SEARCH BOOK ---")
lib.search_book("Python")

