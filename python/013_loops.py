# Python While Loops
# Python Loops

# The while Loop

# i = 1
# while i < 100:
#   print(i)
#   i += 1 # i++, i = i + 1


# The break Statement
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

#   The continue Statement
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# The else Statement
# i = 1
# while i < 6: # False
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# Python For Loops
# fruits = ["apple", "banana", "cherry", "grapes"]
# for x in fruits:
#   print(x)

# Looping Through a String
# [b , a , n , a, n, a]
# for x in "banana":
#   print(x)

fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# continue statement
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# range function
# for x in range(10):
#   print(x)

# else in for loop
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  print(x)
  for y in fruits:
    print(y)