# Lists-Basics
friends = ['John','Micheal','Terry', 'Eric','Graham']
print(friends)
print(friends[1],friends[4])
print(friends[2:4])
print(len(friends))
print(friends.count('Eric'))
# Lists-continued
cars = [911,130,328,535,740,308]
print(friends)
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)
print(sum(cars))
friends.append('DanaG')
friends.insert(1,'Dana')
friends.pop('Eric')

# Exercise
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
#sales.extend(sales_w1)
#sales.extend(sales_w2)
sales = sales_w1 + sales_w2
#sales.sort()
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')