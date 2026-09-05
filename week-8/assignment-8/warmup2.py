#Safe Division
#ask user for two numbers and divide the first by second and use try/except ZeroDivisionError to catch the division by  zero, print message, and ask again

while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
        print(f"{numerator} divided by {denominator} = {result}.")
        break  # Exit the loop if division is successful
    except ZeroDivisionError:
        print(" Can't divide by zero - please enter a non-zero denominator.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
