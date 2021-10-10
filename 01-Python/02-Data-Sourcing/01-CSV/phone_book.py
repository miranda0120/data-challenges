import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, skipinitialspace=True)
    line_count = 0

    for row in csv_reader:
        if line_count > 1:
            print(f"{row[1]}: {row[2]}")
        line_count += 1
# optional:
    csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
    for row in csv_reader:
        print(f"{row['last_name']}: {row['phone_number']}")
