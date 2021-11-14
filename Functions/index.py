# 

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# color = input('Enter favorite color: ')
# greeting(name, int(age), color)
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 




# Functions - Named Notation
# if you want to switch arguments while calling the functions, you need to name the arguments frist

# Return statements
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return f"{amount}, {tax}, {total_amount}"
    
price = value_added_tax(100)    
print(price, type(price))

# Comparisons and Boolean
a = 7
b= 3
print(a == b)
print(a != b)
print(a > b)
print(a < b)



# Conditionals: If, Else, Elif
is_raining = False
is_cold = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella or jacket or both")
else:
    print("Umbrella is optional")