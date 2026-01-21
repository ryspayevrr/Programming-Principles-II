# Double(" ") or single(' ') quotes both work

# Possible to use them inside the string as long as it doesn't match quotes outside

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multi-line strings (works same with double or single quotes)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are arrays of characters

a = "Hello, World!"
print(a[1]) # prints "e"

print(len(a)) # prints length

# Looping through letters

for x in "banana":
    print(x)


# Checking if a sequence of characters is in the string 

txt = "The best things in life are free!"
print("free" in txt)

# Checking with if statement

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


# Checking with if NOT in the string

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")




# Slicing 

b = "Hello, World!"
print(b[2:5]) # from index 2 to 4 (5 is not included)

# Slicing from the start 

b = "Hello, World!"
print(b[:5])  # from start to 5 (not included)

# Slicing till the end

b = "Hello, World!"
print(b[2:])  # from 2 to the end

# Negative indexing to start from the end

b = "Hello, World!"
print(b[-5:-2])     # -5 is "o" in "World!" and -2 ("d") is not included



# Modifying strings

# Upper and lower methods which return the string in upper/lower case:

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

# strip() method which removes white spaces from the beginning or the end

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!



# Replacing a string with another string

a = "Hello, World!"
print(a.replace("H", "J"))


# Splitting a string by a separator

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# String concatenate

a = "Hello"
b = "World"
c = a + b
print(c)

# If need a space

a = "Hello"
b = "World"
c = a + " " + b
print(c)