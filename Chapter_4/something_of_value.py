prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

for i in prices:
    print i
    print "price: %s" % prices[i]
    print "stock: %s" % stock[i]

total = 0
for key in prices:
    value = prices[key] * stock[key]
    total += value
print "total is {}".format(total)

Hello
Jellow
hielo
hi
