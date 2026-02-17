# 1
 
def squares(N):
    i = 1

    while i <= N:
        yield i ** 2
        i += 1

n = int(input("Enter a number: "))

for j in squares(n):
    print(j)




# 2

def evenNumbers(n):

    i = 0

    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

n = int(input("Enter a number: "))

last_even = n if n % 2 == 0 else n - 1

for _ in evenNumbers(n):
    if _ == last_even:
        print(_, end="")
    else:
        print(_, end=", ")





# 3

def divisible_by_3_and_4(n):
    for i in range (n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())

print(*divisible_by_3_and_4(n), sep=", ")




# 4

def squares2(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for j in squares2(a, b):
    print(j, end=" ")





# 5

def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter n: "))

for num in countdown(n):
    print(num)
