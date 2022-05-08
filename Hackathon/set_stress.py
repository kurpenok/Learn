import random
import csv

fields = []
rows = []

with open("Hackathon.csv", "r") as data:
    reader = csv.reader(data)

    fields = next(reader)

    for row in reader:
        rows.append(row)

fields.append("stress")
for i in range(len(rows)):
    if int(rows[i][3]) >= 0:
        rows[i].append(random.randint(0, 40))
    else:
        rows[i].append(random.randint(40, 80))

with open("Hackathon.csv", "w") as data:
    writer = csv.writer(data)
    writer.writerow(fields)
    writer.writerows(rows)

