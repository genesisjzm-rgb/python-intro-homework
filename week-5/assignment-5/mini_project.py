numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def show_menu():
    print('=== Number Cruncher ===')
    print('1. Find the minimum number')
    print('2. Find the maximum number')
    print('3. Search for a number')
    print('4. Sort the list')
    print('5. Quit')
   

running = True
while running:
    show_menu()
    choice = input("\nEnter your choice: ")

    ##user input validation

    if choice == '1':
        min_number = numbers[0]
        for number in numbers:
            if number < min_number:
                min_number = number
        print(f'The minimum number is: {min_number}')

    elif choice == '2':
        max_number = numbers[0]
        for number in numbers:
            if number > max_number:
                max_number = number
        print(f'The maximum number is: {max_number}')

    elif choice == '3':
        search = input("Enter a number to search for: ")
        found = False #this is set to keep track of if its found or not

        #this is to loop through every index of the list to find the number

        for i in range(len(numbers)):
            if numbers[i] == search:
                print(f'Found {search} at index {i}.')
                found = True
                break
        if not found:
            print(f'{search} was not found in the list.')

    ##This is bubble sort without .sort() or sorted()
    elif choice == '4':

        for i in range(len(numbers)):
            for j in range(0, len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        print(f'The sorted list is: {numbers}')
    elif choice == '5':
        print('Goodbye!')
        running = False
    else:
        print('Invalid choice. Please try again.')
