# For One and All
my_list = [1, 9, 3, 8, 5, 7]

for number in my_list:
    # Your code here
    print 2 * number


start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for x in start_list:
    x = x ** 2
    square_list.append(x)
square_list.sort()

print square_list

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']


menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Pasta matona'] = 4.50
menu['Carnita asada'] = 6.50
menu['Pescadito fresco'] = 2.50

print "There are " + str(len(menu)) + " items on the menu."
print menu