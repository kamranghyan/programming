# Python Sets
# Sets
thisset = {"apple", "banana", "cherry"}
# print(thisset)

# Access Items
# for x in thisset:
#   print(x)

# print("grape" in thisset)


# Add Items

# thisset.add("orange")

# print(thisset)
thisset.update(["orange", "mango", "grapes"])

# print(thisset)

# length

# print(len(thisset))


# Remove Item


# thisset.remove("banana")
# print(thisset)


# thisset.discard("banana")
# print(thisset)

# Join Two Sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)