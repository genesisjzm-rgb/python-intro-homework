# Warmup 1
# Read a Text File and Print Line by Line


with open('python-intro-homework/week-7/data/notes.txt', 'r') as file:
    for line in file:
        print(line.strip())