#Using the os module
#print current directory, Check whether ../data/expenses.csv exists using os.path.exists(). Print "expenses.csv found." or "expenses.csv not found." accordingly.
#Use os.path.join() to build the path "../data/expenses.csv" from unittest import result

import os 

print(os.getcwd())

# build the path to the file
path = os.path.join('..', 'data', 'expenses.csv')

#check if the file exists
if os.path.exists(path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

print(path)