"""class String:
    def getString(self):
        self.userInput = input()
    def printString(self):   
        print(self.userInput.upper())

string = String()
string.getString()
string.printString()"""

"""class Shape:
    def __init__(self):
        pass  

    def area(self):
        return 0  


class Square(Shape):
    def __init__(self, length):
        self.length = length  
    
    def area(self):
        return self.length * self.length  


x = int(input("Enter length : "))  
s = Square(x)  
print("Square area:", s.area())  

shape = Shape()
print("area of Shape:", shape.area())"""

"""import math  

class Point:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  

    def show(self):  
        print("The point has coordinates:", self.x, self.y)  

    def move(self, new_x, new_y):  
        self.x = new_x  
        self.y = new_y  

    def dist(self, other_point):  
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)  


p1 = Point(0, 0)  
p2 = Point(3, 4)  

p1.show()  
p2.show()  

print("Distance between points:", p1.dist(p2))  

p1.move(1, 1)  
p1.show()  """

"""class Account:
    def __init__(self, owner, balance):  
        self.owner = owner  
        self.balance = balance  

    def deposit(self, amount):  
        self.balance += amount  
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")  

    def withdraw(self, amount):  
        if amount > self.balance:  
            print(f"{self.owner}, insufficient funds! Balance: {self.balance}")  
        else:  
            self.balance -= amount  
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")  


acc = Account("John", 100)  

acc.deposit(50)    
acc.withdraw(30)   
acc.withdraw(200)  
acc.withdraw(100)"""

"""class Filter_prime():
    def isPrime(self, num):
        if (num < 2):
            return False
        else:
            for i in range(2, num):
                if(num % i == 0):
                    return False
        return True   

    def filter_primes(self, listofnums):
        return filter(lambda x : self.isPrime(x), listofnums)

prime_filter = Filter_prime()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(prime_filter.filter_primes(nums))
print(prime_numbers)"""

