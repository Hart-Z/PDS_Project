import csv

reader = csv.reader("Pittsburgh_review.csv")

for line in reader:
    print(line)
    break