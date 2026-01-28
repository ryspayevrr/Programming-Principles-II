cars = ["Toyota", "Mitsubishi", "Mazda", "Subaru"]
for c in cars:
    print(c, end=" ")

print("\n")
print("Let's spell your name by letters!")
name = str(input())

for char in name:
    print(char, end=" ")
    
print("\n")

for x in cars:
    print(x, end= " ")
    if x == "Mazda":
        break

print("\n")

for y in cars:
    if y == "Mazda":
        continue
    print(y, end=" ")

print("\n")

for k in range(2, 7):
    print(k)