import csv
filename = "Persons.csv"
total = 0

phrase = input("Enter the phrase you want to search: ").lower()


if len(phrase) > 1:
    with open(filename, "r", encoding="utf-8") as f:
        contents = csv.reader(f, delimiter=";")
        for row in contents:
            if phrase in row[0].lower() or phrase in row[1].lower():
                print(";".join(row))
                total += 1

        print(f"Found {total} phrases")
else:
    print("phrase too short.")