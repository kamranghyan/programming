##################################################
# Variables, loops, if/else
##################################################

# A variable is like a box you store a value in for later use.
# We call this "assigning" the value to the variable.

# VARIABLES

# data structure
# int, float, double, sring, null, boolean 
# tuple, list, dictionary, array


# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

x = 5;
y = 10

# first name
fname = "Kamran"
lname = "Ghyan"


#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John


# Assign Value to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# Output Variables

x = "Hasroon B"
#print("My name is " + x)

x = 5
y = "John"
# print(x + y)

# Global Variables
x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()


## The global Keyword

def myfunc():
  global txt
  txt = "fantastic"

myfunc()

print("Python is " + txt)
