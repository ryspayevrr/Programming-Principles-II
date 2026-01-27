import math

j = 0

print("Find the missing number in the sequence!")

while j < 6:
    j += 1
    if j == 4:
        continue
    print(j, end=" ")

print("\n")

prime_number = 17
i = 1

while i < 100:
    if prime_number % i == 0:
        print("Number is prime!")
    i += 1