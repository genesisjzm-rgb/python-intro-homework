#Validate Numeric Input
#catch the ValueError with a try/except block

def get_integer_input(prompt):

#ask for input from the user

    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

print(get_integer_input("Please enter an integer: "))





