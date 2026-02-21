from models.transaction import Transaction

class PurchaseTransaction(Transaction):
    def __init__(self, transaction_id, date, member, item, quantity):
        super().__init__(transaction_id, date, member, item)
        self.__purchase_date = date
        self.__quantity = quantity
        self.__total_price = 0.0

    @property
    def purchase_date(self):
        return self.__purchase_date
    
    @property
    def quantity(self):
        return self.__quantity
    
    @property
    def total_price(self):
        return self.__total_price

    def calculate_total(self):
        self.__total_price = self.item.price * self.__quantity
        return self.__total_price

    def process_transaction(self):
        if self.item.available_copies >= self.__quantity:
            self.item.available_copies = self.item.available_copies - self.__quantity
            self.calculate_total()
            print(f"'{self.item.title}' purchased by {self.member.name}")
            print(f"Total: ${self.__total_price:.2f}")
            return True
        else:
            print(f"Error: Not enough copies of '{self.item.title}'")
            return False

    def display_transaction(self):
        print("\n" + "="*50)
        print("PURCHASE TRANSACTION")
        print("="*50)
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Member: {self.member.name}")
        print(f"Item: {self.item.title}")
        print(f"Purchase Date: {self.__purchase_date}")
        print(f"Quantity: {self.__quantity}")
        print(f"Unit Price: ${self.item.price:.2f}")
        print(f"Total Price: ${self.__total_price:.2f}")
        print("="*50 + "\n")