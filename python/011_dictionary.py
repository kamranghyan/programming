# Python Dictionaries
# Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Accessing Items
# x = thisdict["model"]
# x = thisdict.get("brand")

# Change Values
# print(thisdict)
# thisdict["year"] = 2018
# print(thisdict)

# Loop Through a Dictionary

# for x in thisdict:
#   print(x[])

# for x in thisdict:
#   print(thisdict[x])

# for x in thisdict.values():
#   print(x)

# Check if Key Exists.
# if "distributor" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
# else :
#   print("Not found") 

# Length

# Adding Items
thisdict["color"] = "pink"

# Removing Items
# print(thisdict)
# thisdict.pop("color")
# print(thisdict)
# print(thisdict)
# thisdict.popitem()
# print(thisdict)

# print(thisdict)
# del thisdict['color']
# print(thisdict)

# thisdict.clear()
# print(thisdict)


# mydict = thisdict.copy()
# print(mydict)

# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily['child2']['name'])