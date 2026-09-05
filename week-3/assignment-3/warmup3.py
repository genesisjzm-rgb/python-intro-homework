# 'not True' is False and since one side is False False and False gives False
print(not True and False)

# 'True or False' only needs one to ne True so it gives True
print(True or False and False)

# 5 is greater than 3 so thats True and adding not flips True to False so its False.
print(not (5 > 3))

# 10 equals 10 is true, but 4 not equal to 4 is False. Both arent True 'and' gives False
print(10 == 10 and 4 != 4)

# 'not False' is True, and 'not True' is False. It gives True
print(not False or not True)