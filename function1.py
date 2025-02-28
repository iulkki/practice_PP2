'''def convert_to_ounces():
    x = float(input("Input your grams:"))
    y = x * 28.3495231
    print ("ounces", y)

convert_to_ounces()'''

'''def convert_to_celsium():
    x = float(input("your Fahrenheit: "))
    y = (5 / 9) * (x - 32)
    print ("In celsium: ", y)

convert_to_celsium() '''

"""def solve(numheads, numlegs):
    for x in range (1, 100):
        if 70 - 2 * x + 4 * x == 94:
            y = 35 - x
            print(x, y)

solve(35, 94) """

'''def filter_prime(l):
    new_list = []  
    for x in l:
        if not any(x % y == 0 for y in range(2, x)):  
            new_list.append(x) 
    print(new_list)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_prime(list1)'''

'''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    primes = []
    for n in numbers:
        if is_prime(n):
            primes.append(n)
    return primes

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(n) for n in numbers]
print("Prime numbers:", filter_prime(numbers))'''

"""import itertools

def permutations(string):
    perms = [''.join(perm) for perm in itertools.permutations(string)]
    print(*perms, sep=' ')

permutations("abc")"""

'''def reverseSentence(s):
    s = s.split(" ")
    l = list(s)
    l.reverse()
    for i in l:
        print(i, end = ' ')

string = input("Enter a sentence: ")
reverseSentence(string)'''

"""def True_OR_Not(l):
    for i in range(len(l) - 1): 
        if l[i] == 3 and l[i+1] == 3:
            return True
    return False  
list1 = input("Enter numbers separated by spaces: ").split()
list1 = [int(n) for n in list1]

print(True_OR_Not(list1))"""

"""def findCombination(nums):
    res = ""  

    for i in nums:  
        if i == 0 or i == 7:  
            res = res + str(i)  

    if "007" in res:  
        return True  
    else:
        return False  """

"""def volume(r):
    return (4/3) * 3.14 * r**3"""

"""def unique_elements(lst):
    unique_list = []  

    for item in lst:  
        if item not in unique_list:  
            unique_list.append(item) 
    
    return unique_list  

nums = [1, 2, 2, 3, 4, 4, 5, 1]
print(unique_elements(nums))  """

"""def palindrome(string):
    s = string[::-1]
    if(s == string):
        return True
    return False"""

"""def histogram(my_list): 
    for i in my_list:
        for j in range(i):
            print("*", end = "")
        print()

list = [8, 8, 8]    
histogram(list)"""

"""import random

def guessGame():
    guessNumber = random.randint(1, 20)
    tries = 0
    num = 0
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    while(num != guessNumber):
        num = int(input("Take a guess "))
        tries += 1
        if(num < guessNumber):
            print("Your guess is too low.")
        elif(num > guessNumber):
            print("Your guess is too big.")

    print(f"Good job, {name}! You guessed my number in {tries} guesses!")

guessGame()"""






















    




    


