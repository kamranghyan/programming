# Python Data Types

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dictionary
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryvie

x_int = 5
x_float = 20.0
x_string = "Hi! String"
x_boolean = True


# Setting the Specific Data Type
x_str_specify = str("Hello World")
x_int_specify = int(20)
x_float_specify = float(20.0)
x_list_specify = list(("apple", "banana", "cherry"))
x_tuple_specify = tuple(("apple", "banana", "cherry"))
x_dict_specify = dict(name="John", age=36)
x_set_specify = set(("apple", "banana", "cherry"))

# Initlize the Data Type
name = "Hello World"
result = 67
average = 5.5
validate = True

# Compound Data Types
# List -> [] -> [1,2,3]
myList = ["apple", "banana", "cherry"]

# Tuple -> () -> (1,2,3)
myTuple = ("apple", "banana", "cherry")

# Range
# Range(length)    
myRange = range(6)

# Dictionary -> {} ->   {key:value, key:value}
myDictionay = {"name" : "John", "age" : 36}

# Set -> {} -> {"", "", ""}
mySet = {"apple", "banana", "cherry"}

print(type(x_str_specify))