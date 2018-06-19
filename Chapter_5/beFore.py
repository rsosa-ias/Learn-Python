names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]

for i in names:
    print i

#

webster = {
    "Aardvark": "A star of a popular children's cartoon show.",
    "Baa": "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# print the key not the value
for i in webster:
    print webster[i]

# if the number is even, print it out
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for n in a:
    if n % 2 == 0:
        print n


# Write a function that counts how many times the string "fizz" appears in a list.
def fizz_count(x):
    count = 0
    for i in x:
        if i == "fizz":
            count = count + 1
    return count


print fizz_count(["fizz", "cat", "fizz"])

# Print items price and stock

prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3}

stock = {"banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15}

for i in prices:
    print i
    print "price: %s" % prices[i]
    print "stock: %s" % stock[i]

#For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
#Finally, outside your loop, print total.
for key in prices:
    total = 0
    total = prices[key] * stock[key]
print total

#TODO:Fix this last funcion to determine how much money you would make if you sold all of your food.