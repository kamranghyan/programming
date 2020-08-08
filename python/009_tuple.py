# Python Tuples
# Tuple

# Access Tuple Items


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Negative Indexing
# Range of Indexes
#               0 - n -1 

# Change Tuple Values
# y = list(thistuple)
# print(y)
# y[1] = "kiwi"

# x = tuple(y)

# Loop Through a Tuple

# for x in thistuple:
#   print(x)

# Check if Item Exists
# if "apple" in thistuple:
#   print("Yes, 'gree' is in the fruits tuple")
# else :
#     print("No, grapes not found")

# Tuple Length


# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2


# The tuple() Constructor
thislist = ["apple", "banana", "cherry"]
print(thislist)
thistuple = tuple(thislist) # note the double round-brackets
print(thistuple)
