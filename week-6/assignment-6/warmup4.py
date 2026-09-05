def is_valid_score(score):
    if score < 0 or score > 100:
        return False
    else:
        return True

user_score = int(input("Enter a score between 0 and 100: "))
if is_valid_score(user_score):
     print("Valid score.")
else:
     print("Invalid score - must be between 0 and 100.")