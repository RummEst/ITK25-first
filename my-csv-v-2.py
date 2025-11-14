

filename = "Create-MyCSV-v.csv"
total = 0
number = 0
counter = 0

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

f = open(filename, "r")
cols = len(f.readline().strip().split(";"))
f.close()
print(cols)

column = int(input(f"Enter the number of columns 1-{cols}: "))

if column < 1 or column > cols:
    print("Column out of range")
    exit()

with open(filename, "r") as f:
    content = f.readlines()
    column -= 1
    for line in content:
        parts = line.strip().split(";")
        if is_number(parts[column]):
            total += int(parts[column])
            counter += 1

    print(f"Veeru summa: {total}")
    print(f"Numbreid kokku:: {counter}")