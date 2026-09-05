student = {"name": "Genesis", 
           "Grade": "B", 
           'subjects': ["english", "math", "history"]}

for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = False

print(student)