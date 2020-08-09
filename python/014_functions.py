# Creating a Function
# In Python a function is defined using the def keyword:

# function -> def

# defination -> def myfunction
# declaration -> : print(x)
# calling -> myfunction()

# defincation
# def my_function():
#   print("Hello from a function")

# calling
# my_function()

# Arguments
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")

# Number of Arguments
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Kamran", "G")

# Arbitrary Arguments, *args
# *kids = ["emil", "Tobias", "Linus"]
# def my_function(*kids):
#   print("The youngest child is " + kids[0])

# my_function("Emil", "Tobias", "Linus")

# Keyword Arguments

# def my_function(child3, child2, child1):
#   print("The child3 is " + child3)
#   print("The child2 is " + child2)
#   print("The child1 is " + child1)

# my_function("Emil", "Tobias", "Linus")
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
    
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")