import csv

fields = []
rows = []

with open("Hackathon.csv", "r") as data:
    reader = csv.reader(data)

    fields = next(reader)

    for row in reader:
        rows.append(row)

number_mood = {
    "Amazing": 2,
    "Good": 1,
    "Normal": 0,
    "Bad": -1,
    "Awful": -2
}

fields.append("number_mood")
for i in range(len(rows)):
    rows[i].append(number_mood[rows[i][2]])

with open("Hackathon.csv", "w") as data:
    writer = csv.writer(data)
    writer.writerow(fields)
    writer.writerows(rows)

