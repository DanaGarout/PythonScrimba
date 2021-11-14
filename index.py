
# Printstatements
from typing import AsyncGenerator


print("Welcome to Python")
print("Welcome to python2")
print("Create hammer")
print("Use Hammer")

# Variables
failed_subjects="2"
name='John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
print(name + '  will need to redo ' + failed_subjects + '  courses.')
name="Eric"
print(name + '  is doing well in geography.')

# Datatypes & Tpyecasting
print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))

# DataTupes exercise

#Create appropriate Variables for Item name, the price 
#and how many you have in stock
item_name = 'widget'
price = 23.5
inventory = 100
is_in_inventory = True
print(item_name, price, inventory)

# Arithmetic Operations
print("Basic Arithmetic")
a=10
b=3
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)


# Strings-Basics/Slicing
msg='welcome to Python 101:strings'
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(len(msg))
print(msg.count('o'))

# slicing
print(msg[0])
print(msg[-2])
print(msg[2:15])
# Exercise
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
print(msg1[::-1].title())
# Strings-2 Find/replace,string formatting
print(msg.find('Python'))
print(msg.replace('Python','C'))
print('Python' in msg)
print('Python' not in msg)

# User input
print("User Input")
name = input('What is your name?:')
age = input('What is your age?:')
print('Hello '+ name + '! You are '+ age + ' years old.')

num1 = input('Enter a digit:')
num2 = input('Another digit:')
answer = float(num1) + float(num2)
print(answer)

# Exercise
name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')












