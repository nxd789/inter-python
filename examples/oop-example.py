from types import ModuleType
class Car:
    def __init__(self, brand, model, year, color="white"):
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year
        self._condition = "good"
        self.__owner = "Santa"
    def describe(self):
        return f"This is a {self.color} {self.brand} {self.model} from {self.year} in {self._condition} condition owned by {self.__owner}."
my_car = Car("Porsche","Carrera",2024,"blue")
print(my_car.color)
print(my_car.describe())
my_car = Car("Jaguar","XK",2000)
print(my_car.color)
print(my_car.describe())
print(my_car._condition)  #<<-- don't do it!
print(my_car.__owner)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
