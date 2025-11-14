import csv

filename = "Create-MyCSV-v.csv"
column, total, counter = 0


while True:
    column = input("Enter the column number (1-10): ")
    if column.isdigit():
        column = int(column)
        if 1 <= column <= 10:
            break  # valid input → exit loop
    print("Invalid input. Please enter a number between 1 and 10.")


with open(filename) as f:
    contents = f.readlines()
    column = column - 1
    for line in contents:
        line = line.strip()
        parts = line.split(";")
        if parts[column].isdigit():
            total += int(parts[column])
            counter += 1

    print("The total number of rows is: ", total)
    print("The total number of columns is: ", counter)

