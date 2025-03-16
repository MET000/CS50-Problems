import csv
import sys


a = []

if len(sys.argv) == 3:
    try:

        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]
                student = {"first": first.strip(), "last": last.strip(), "house": house}
                a.append(student)

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in a:
            writer.writerow(
                {
                    "first": student["first"],
                    "last": student["last"],
                    "house": student["house"],
                }
            )

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    sys.exit("Too few command-line arguments")
