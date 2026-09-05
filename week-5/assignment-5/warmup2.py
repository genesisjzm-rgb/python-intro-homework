
while True:

    try:
        user_in = input('Please enter a number: ')
        if user_in.isdigit():
            number = int(user_in)
            break 
        else:
            print("That's not a positive integer. Try again.")
    
    except ValueError:

        print("That's not a positive integer. Try again.")

print(f'Got it: {number}')