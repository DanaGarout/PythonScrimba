#split and Join
print("split")
msg = 'Welcome to Python 101: Splut and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(list(msg))
print(msg.split())
print

# Exercise
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'


friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)
print('replace', csv.replace(';',',').replace(':',',').split(','))

# Tuples
friends = ['John','Micheal','Terry','Eric','Graham']
print(friends)
# Tuples are lists that you can't change
friends_tuple = ('John','Micheal','Terry','Eric','Graham')
# They are also wrapped in brackets 
print(friends[2:4])
print(friends_tuple[2:4])

# sets - they are blazingly fast unordered lists and they are wrapped in {}
# You can use intersection,union and difference between 2 sets too
# Exercise
friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
print('Eric' in friends and 'John' in friends)
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)
cars_no_dupl =list(set(cars))
print(cars_no_dupl)

# Comments