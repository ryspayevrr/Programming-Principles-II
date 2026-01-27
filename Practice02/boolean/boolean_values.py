print(123 > 121)
print(33 == 33)
print(20 < 99)

a = 213
b = 45

if a < b:
    print("b is greater than a")
else:
    print("a is greater than b")


print(bool("Almaty"))
print(bool(138))
print(bool(0))
print(bool(["kurt", "beshbarmak"]))
print(bool(None))
print(bool({}))

def func():
    return True

if func():
    print("YES!")
else:
    print("NO!")


x = 36.6
print(isinstance(x, str))