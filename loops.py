from random import randint

names = ["Mari", "Juana", "Bob", "Märten"]

# print listis olevad nime yhe kaupa
for name in names:
    print(name)

print("\n---------------------------\n")

# sama yl teine lahendus
for x in range(len(names)):
    print(f"{x+1}. {names[x]} {randint(1, 122)}")

print("\n--------------------------\n")

for x in range(10+1):
    print(x, end=" ")

print("\n\n--------------------------\n")

for x in range(1, 5+1):
    print(x, end=" ")

print("\n\n--------------------------\n")

for x in range(0, 10, 2):
    print(x, end=" ")
print()
for x in range(1, 10, 2):
    print(x, end=" ")

print("\n\n--------------------------\n")

# While-loop
x = 0
while x < len(names):
    print(f"{x + 1}. {names[x]} {randint(1, 122)}")
    x += 1

print("\n\n--------------------------\n")

#ÜLESANNE:
x = 0
while x < len(names):
    print(f"{x + 1}. {names[x]}")
    x += 1

print("\n\n--------------------------\n")

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")