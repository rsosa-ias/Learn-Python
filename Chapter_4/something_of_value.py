prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 1,
    "orange": 32,
    "pear": 15,
}

for i in prices:
    print i
    print "price: %s" % prices[i]
    print "stock: %s" % stock[i]

for k in prices:
    total = 0
    total = prices[k] * stock[k]
print "total is {}".format(total)

