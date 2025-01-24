print("Hello, World!")

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")

#x = 5
#y = "Hello, World!"        

#This is a comment.
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
x = 5
y = 10
print(x + y)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = 5
print(type(x))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  b = "Hello, World!"
print(b[-5:-2])

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello"
b = "World"
c = a + " " + b
print(c)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
