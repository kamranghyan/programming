# Python Lists
#  Python Collections (Arrays)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# LIST

# mylist = []
           # 0        1          2
thislist = ["apple", "banana", "cherry"]

# Access Items
# Negative Indexing
# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Range of Negative Indexes

# Change Item Value
#thislist[1] = "Grapes"
# print(thislist[1])

# Loop Through a List
# for x in thislist:
#   print(x)

#Check if Item Exists
# if "grapes" in thislist:
#   print("Yes, 'apple' is in the fruits list")
# else :
#     print("Not found!")

# Length

# Add Items
# print(len(thislist))
# thislist.append("grapes")
# print(len(thislist))
# print(thislist)

# Insert Item
# print(thislist)
# thislist.insert(1, "grapes")
# print(thislist)

# Remove Item

# thislist.remove("banana")

# thislist.pop()

# del thislist[0]

# Copy a List
# mylist = thislist.copy()

# mylist = list(thislist)
# a + 2 error data type different
# 2 + 2 same data type
# aa + bb = aabb same data type

list1 = ["a", "b" , "c"] # list
list2 = [1, 2, 3] # list
mylist = list1 + list2
#   0
# ["a", "b" , "c", 1, 2, 3 ]
# for x in list2:
#   list1.append(x)


# list() Constructor

thistuple = ("apple", "banana", "cherry")
print(type(thistuple))
print(thistuple)
thislist = list(thistuple)
print(type(thislist))
print(thislist)
