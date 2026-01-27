i = 1

while i < 10:
    print(i, end=" ")
    if i == 6:
        print("Found the six.")
    if i == 7:
        print("Found the seven.")
        print("Six-seven!")
        break
    i += 1

count = 5

print("RACE WILL START IN...")

while count > 0:
    print(count)
    count -= 1

print("START!")