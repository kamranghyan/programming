# print("Hello")
# print('Hello')

#Assign String to a Variable

x = "Hello World!"

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
this is test
ut labore et dolore magna aliqua."""

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

# Strings are Arrays
a = "Hello, World!"

# Slicing
b = "Hello, World!"

#print(b[-13:-5])

# Negative Indexing

#print(b[-13:-5])

# String Length
# print(len(b))


# String Methods
a = " Hello, World!, The "

# print(a.strip()) # returns "Hello, World!"

# print(a.lower())

# print(a.upper())

# print(a.replace("H", "J"))

# print(a.split(",")) # returns ['Hello', ' World!']

# Check String

txt = "The rain in Spain stays mainly in the plain"
x = "the" in txt
# print(x)

# String Concatenation
a = "Hello, "
b = "World"
c = a + b

# Format string
age = str(36)
txt = "My name is John, I am " + age

age = 30
txt = "My name is John, and I am {}, height {}"
# print(txt.format(age, 5.8))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
#print(myorder.format(quantity, itemno, price))


itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
#print(myorder.format(quantity, itemno, price))

# Escape Character

txt = "We are the so-called \"Vikings\" from the north."

print(txt)