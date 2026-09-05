
# 1. What the error message said:
 #  NameError: name 'naame' is not defined. Did you mean: 'name'?

#2. What caused it:
 #  I misspelled the variable name as 'naame' inside the print statement 
  # and forgot to include input() on line 1, so Python didn't know what 'naame' was.

#3. How I fixed it:
 #  I added input() to line 1 to capture the user's input and corrected 
  # the spelling of the variable to 'name' in the print statement.'''

# Fixed, working code:

name = input("What is your name? ")
print(f"Your name is {name}.")
