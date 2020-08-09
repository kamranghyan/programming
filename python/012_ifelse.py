# Python Conditions

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200
# if b > a: # True
#   print("b is greater than a")

# Elif -> else if

a = 35
b = 34
# if b > a: # False
#   print("b is greater than a")
# elif a == b: # False
#   print("a and b are equal")
# else :
#     print("a is greater than b")


# Short Hand If
# if a > b: print("a is greater than b")

# Short Hand If ... Else

# print("A") if a > b else print("B")

# Ternary Operators
# print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500

# if a > b and c > a: # True
#   print("Both conditions are True")

#   if a > b or a > c:
#   print("At least one of the conditions is True")

x = 21

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
