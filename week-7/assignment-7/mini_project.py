#Expense Report Generator
#use os.path.exists() to check if the file exists. If it does, read the file into list of dictionaries using csv.DictReader. If it does not exist, print "File not found." and exit the program.
#convert the amount field to float for each row
#filter the list to only rows where category is "Food"
#Write report to food_export/txt file in format Food Expenses Report- genrated (todays date)

import os 
import datetime
import csv

# build the path to the file
path = os.path.join('..', 'data', 'expenses.csv')

#check if the file exists
if os.path.exists(path):
    print("expenses.csv found.")
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        expenses = []
        #convery numeric fields to float
        for row in reader:
            row['amount'] = float(row['amount'])
            expenses.append(row)


        #filter the list to only rows where category is "Food"
        food_expenses = [row for row in expenses if row['category'] == 'Food']

        #calculate total
        total_food = sum(item['amount'] for item in food_expenses)

        #Format date and write report
        today = datetime.datetime.now().strftime("%B, %d, %Y")

        with open('food_report.txt', 'w') as report_file:
            report_file.write(f'Food Expenses Report - Generated {today}\n')

            for expense in food_expenses:
                report_file.write(f"{expense['date']}: {expense['amount']}")
            report_file.write(f"\n Total: {total_food:.2f}\n")
else:
    print("expenses.csv not found.")

