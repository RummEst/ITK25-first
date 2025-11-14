import csv


def is_number(s):
    return s.isdigit()  # only positive integers; adjust if needed


filename = "Create-MyCSV-v.csv"

sum_list = []

with open(filename, "r", encoding="utf-8") as f:
    for line_index, line in enumerate(f):
        line = line.strip()
        if not line:
            continue

        parts = line.split(";")

        # First line: create empty lists
        if line_index == 0:
            sum_list = [[] for _ in parts]

        # Process each column
        for i, item in enumerate(parts):
            item = item.strip()
            if is_number(item):
                sum_list[i].append(int(item))

# Output results
for lst in sum_list:
    count = len(lst)
    total = sum(lst) if lst else 0
    print(count, total)
