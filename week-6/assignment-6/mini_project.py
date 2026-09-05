numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

#Findind minimum number
def find_minimum(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

#Finding maximum number
def find_maximum(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

#Searching for a number
def search_number(numbers, target):

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

#Bubble sort 

def bubble_sort(numbers):

#make copy of the list to avoid modifying the original list
    sorted_numbers = numbers.copy()

    for i in range(len(sorted_numbers)):
        for j in range(0, len(sorted_numbers) - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]
    print(f'The sorted list is: {sorted_numbers}')

    return bubble_sort

#Prints the menu options
def show_menu():
    print('=== Number Cruncher ===')
    print('1. Find the minimum number')
    print('2. Find the maximum number')
    print('3. Search for a number')
    print('4. Sort the list')
    print('5. Quit')

    return show_menu

#Main program loop that calls for show_menu() and takes user input to call the appropriate function

if __name__ == "__main__":
    running = True
    while running:
        show_menu()
        choice = input("\nEnter your choice: ")

        ##user input validation

        if choice == '1':
            min_number = find_minimum(numbers)
            print(f'The minimum number is: {min_number}')

        elif choice == '2':
            max_number = find_maximum(numbers)
            print(f'The maximum number is: {max_number}')

        elif choice == '3':
            target = int(input("Enter a number to search for: "))
            index = search_number(numbers, target)

            if index != -1:
                print(f'Found {target} at index {index}.')
            else:
                print(f'{target} was not found in the list.')

        elif choice == '4':
            bubble_sort(numbers)

        elif choice == '5':
            print('Goodbye!')
            running = False
        else:
            print('Invalid choice. Please try again.')


        