"""def square_generator(n):
    for i in range (n + 1):
        yield i**2
n = int(input())
for square in square_generator(n):  
    print(square)"""

'''def evens():
    n=int(input())
    a=(int(i) for i in range(0, n, 2))
    for i in range(int(n/2)):
        print(next(a), end = ", ")
    print(next(a))'''

"""def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter the value of n: "))
for num in divisible_by_3_and_4(n):
    print(num, end=", ")"""

"""def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2  

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

print("Squares of numbers from", a, "to", b, ":")
for num in squares(a, b):
    print(num, end=", ")"""


"""def decreasing():
    n = int(input())
    a = (i for i in range(n, 0, -1))
    for i in range(n):
        print(next(a))"""