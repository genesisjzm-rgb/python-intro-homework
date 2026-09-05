name = ["Genesis", "John", "Alice", "Bob", "Mary", "Jane", "Tom", "Jerry", "Sam", "Lucy"]

find = input("Enter a name to find: ")

counter = 0

for n in name: 
    if n == find:
        print(f" Found {find} at index {counter}.")
    else: 
        counter += 1

if counter == len(name):
    print(f"{find} is not in the list.")