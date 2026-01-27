n = 5
while n > 0:
    print(n**2, end=" ")
    n -= 1


print("\n")

i = 0
print("Even elements: ", end=" ")
while i < 10:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1