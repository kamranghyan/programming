# Boolean Values

#print(10 > 9)  # True
#print(10 == 9) # False 
#print(10 < 9)  # False

# Example 01
a = 200
b = 33
#  33 > 200
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables
#print(bool("Hello"))
#print(bool(15))


# Example 02

x = "Hello"
y = 15

#print(bool(x))
#print(bool(y))

# Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())