suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]
print first
# Third and fourth items (index two and three)
middle = suitcase[2:4]
print middle
# The last two items (index four and five)
last = suitcase[4:6]
print last

animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]
print cat
# The fourth through sixth characters
dog = animals[3:6]
print dog
# From the seventh character to the end
frog = animals[6:10]
print frog

animals2 = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals2.index("duck")# Use index() to find "duck"

# Your code here!
animals2.insert(duck_index, "cobra")

print animals2 # Observe what prints after the insert operation

# For One and All
my_list = [1, 9, 3, 8, 5, 7]

for number in my_list:
    # Your code here
    print 2 * number
