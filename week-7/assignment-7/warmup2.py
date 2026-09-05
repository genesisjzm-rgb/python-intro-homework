#Read a CSV with DictReader and Print Line by Line

import csv

with open('python-intro-homework/week-7/data/students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['score'])