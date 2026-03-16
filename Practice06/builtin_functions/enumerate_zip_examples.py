names = ["Aisha", "Yeraly", "Gaziz"]
scores = [85, 90, 88]


for i, (n, s) in enumerate(zip(names, scores)):
    print(i, n, s)








# Demonstrate type checking and conversions


value = "25"

print("Original value:", value)
print("Type:", type(value))

number = int(value)

print("Converted value:", number)
print("Type after conversion:", type(number))