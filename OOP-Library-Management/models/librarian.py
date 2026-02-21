from models.person import Person

class Librarian(Person):
    def __init__(self, name, person_id, phone_number, email, employee_id, shift, salary, hire_date):
        super().__init__(name, person_id, phone_number, email)
        self.__employee_id = employee_id
        self.__shift = shift
        self.__salary = salary
        self.__hire_date = hire_date

    @property
    def employee_id(self):
        return self.__employee_id
    
    @property
    def shift(self):
        return self.__shift
    
    @property
    def salary(self):
        return self.__salary
    
    @property
    def hire_date(self):
        return self.__hire_date
    
    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value

    def login(self, username, password):
        print(f"Librarian {self.name} logged in successfully!")
        return True
    
    def display_info(self):
        print("Librarian Information:")
        print(f"\tName: {self.name}")
        print(f"\tID: {self.person_id}")
        print(f"\tEmployee ID: {self.employee_id}")
        print(f"\tPhone: {self.phone_number}")
        print(f"\tEmail: {self.email}")
        print(f"\tShift: {self.shift}")
        print(f"\tSalary: ${self.salary:.2f}")
        print(f"\tHire Date: {self.hire_date}\n")