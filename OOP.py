#!/usr/bin/env python
# coding: utf-8

# In[3]:


## Object-oriented programming
## Classess, objects, and instances
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        
car = Vehicle("Toyota", "Camry")
car.display_info()

## Inheritance and polymorphism
class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color
        
    def display_info(self):
        super().display_info()
        print("Color:", self.color)
        
my_car = Car("Honda", "Civic", "Red")
my_car.display_info()


# In[6]:


### Encapsulation and data hiding
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
        
        
    def get_account_number(self):
        return self._account_number
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")
            
account = BankAccount("123456789", 1000)
print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())


# In[7]:


###  A short code for thye same
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
        
    def deposit(self, amount):
        self._balance += amount
        return self._balance
        
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            return "Insufficient funds"
        return self._balance

account = BankAccount("123456789", 1000)
print("Balance after deposit:", account.deposit(500))
print("Balance after withdrawal:", account.withdraw(200))


# In[9]:


## OOP principles and design patters
class Singleton:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)


# In[ ]:




