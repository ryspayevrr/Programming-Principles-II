import math

# 1

degree = float(input("Enter degrees: "))

radian = math.radians(degree)

print("Radians: ", radian)



print("\n")

# 2 

print("Calculating Area of Trapezoid")

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2

print("Area:", area)


print("\n")

# 3

print("Calculating Area of Regular Polygon")

n = int(input("Enter number of sides: "))
s = float(input("Enter the length of a side: "))

area = int((n * s**2) / (4 * math.tan(math.pi / n)))
print("The area of the polygon is:", area)



print("\n")




# 4

print("Calculating Area of Parallelogram")

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print("Expected Output:", area)

