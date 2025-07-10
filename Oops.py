class Oops:
    def __init__(self):
        print("Oops class called")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

p1=Product("Pencil", 100, 10)
p2=Product("NoteBook", 100, 10)

print("The product1 is a",p1.name)
print("The product1 price is",p1.price)
print("The product1 quantity is",p1.quantity)

print("\nThe product2 is a",p2.name)
print("The product2 price is",p2.price)
print("The product2 quantity is",p2.quantity)


# Encaplulation
class Account:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.__balance = 0
    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance += balance
a1=Account("Raj",852)
print()
a1.setBalance(100000)
print(a1.getBalance())
# Example
class Marks:
    def __init__(self):
        self.__maths=0
    def setMaths(self,maths):
        self.__maths=maths
    def getMaths(self):
        return self.__maths
# obj
m1=Marks()
m1.setMaths(100)
print(m1.getMaths())


# inheritance
class User:
    def login(self):
        print("Login called")
class BusinessUser(User):
    def run_add(self):
        print("Run add called")
b1=BusinessUser()
b1.login()
b1.run_add()
# Example
class Employee:
    def work(self):
        print("Employee works")
class Manager(Employee):
    def manage(self):
        print("Manager manages")
m1=Manager()
m1.work()
m1.manage()


# Polymorhism
class Vehicle:
    def navigate(self):
        print("navigate")
class Car(Vehicle):
    def navigate(self):
        print("navigate via Car")
class Bicycle(Vehicle):
    def navigate(self):
        print("navigate via Bicycle")
for v in [Car(),Bicycle()]:
    v.navigate()
# Example
class Dog:
    def make_sound(self):
        print("Dog barks")
class Cat(Dog):
    def make_sound(self):
        print("Cat meows")
c1= Cat()
c1.make_sound()
# overloading
class Demo:
    def show(self,a=None,b=None,c=None):
        if a and b and c:
            print("3 args")
        elif (a and b) or (a and c):
            print("2 args")
        elif a or b or c:
            print("1 args")
        else:
            print("0 args")
a=Demo()
a.show(1,2,3)
a.show(1,2)
a.show(1)
a.show()

# Abstrction
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def online(self):
        pass
class Upi(PaymentMethod):
    def pay(self):
        print("Payment is in Upi")
    def online(self):
        print("Payment is in Upi")
u1 = Upi()
u1.pay()
u1.online()
# Example
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class WashingMachine(Appliance):
    def turn_on(self):
        print("Turning on Washing Machine")
class Fridge(Appliance):
    def turn_on(self):
        print("Turning on Fridge")
w1=WashingMachine()
w1.turn_on()
f1=Fridge()
f1.turn_on()

