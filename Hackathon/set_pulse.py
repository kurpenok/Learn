import random
import csv

fields = []
rows = []

with open("Daylio_Abid.csv", "r") as data:
    reader = csv.reader(data)
    
    # For skip name row
    fields = next(reader)

    for row in reader:
        rows.append(row)

for i in range(len(rows)):
    rows[i][1] = random.randint(60, 80)

with open("Hackathon.csv", "w") as data:
    writer = csv.writer(data)
    writer.writerow(fields)
    writer.writerows(rows)

