# 📚 Library Management System

> A Python OOP project developed as part of the Aitronix AI Course.

---

## 📋 Project Description

A console-based Library Management System that allows librarians to manage books, magazines, members, and transactions. The system supports borrowing, returning, and purchasing items with full validation.

---

## 🧱 OOP Concepts Used

| Concept | How It's Applied |
|---|---|
| **Encapsulation** | Private/protected attributes with `@property` and setters in all model classes |
| **Abstraction** | Abstract base classes using `abc.ABC` and `@abstractmethod` (e.g., `Item`, `Person`, `Transaction`) |
| **Inheritance** | `Person → Member, Librarian` / `Item → Book, Magazine` / `Transaction → BorrowTransaction, PurchaseTransaction` |
| **Polymorphism** | `display_info()` and `process()` overridden in each subclass |
| **Association** | `Library` associates with `Member` and `Item` |
| **Aggregation** | `Library` aggregates a list of `Book` and `Magazine` objects |
| **Composition** | `BorrowTransaction` is composed within `Library` lifecycle |

---

## ✨ Features

- ➕ Add / remove books and magazines
- 👤 Register members
- 📖 Borrow books with limit validation (max 3 per member)
- 🔄 Return books with fine calculation
- 🛒 Purchase items
- 🔍 Search for available books
- 📊 Display full system state

---

## 🗂️ Project Structure

```
Aitronix-AI-Course-Projects/
└── OOP-Library-Management/
    ├── models/
    │   ├── __init__.py
    │   ├── item.py              # Abstract base: Item
    │   ├── book.py              # Book(Item)
    │   ├── magazine.py          # Magazine(Item)
    │   ├── person.py            # Abstract base: Person
    │   ├── member.py            # Member(Person)
    │   ├── librarian.py         # Librarian(Person)
    │   ├── transaction.py       # Abstract base: Transaction
    │   ├── borrow_transaction.py
    │   └── purchase_transaction.py
    ├── library.py               # Core Library class
    └── main.py                  # Entry point
```

---

## ▶️ How to Run

```bash
# Navigate to project folder
cd OOP-Library-Management

# Run the program
python main.py
```

> Requires Python 3.10+

---

## 💻 Implementation

This project is implemented as a **Multi-file Python project**.

---

## 👤 Author

**Mohamed M. Fahmi**  

