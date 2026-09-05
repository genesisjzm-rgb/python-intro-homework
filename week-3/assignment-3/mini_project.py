day = input('Please enter a day of the week: ').strip().lower()
time_of_day = input("Please enter a time of day (morning, afternoon, or evening): ").strip().lower()

if day == "monday":
    if time_of_day == "morning":
        print("Activity: Go for an early morning walk!! ")
    elif time_of_day == "afternoon":
        print('Activity: Make yourself a yummy snack!! ')
    elif time_of_day == "evening":
        print('Activity: Make yourself a yummy and healthy dinner')
    else:
        print('Invalid time of day')
elif day == "saturday":
    if time_of_day == "morning":
        print('Activity: Make yourself a nice cup of coffee to start your day!!')
    elif time_of_day == "afternoon":
        print('Activity: Spend your afternoon in a park or somewhere outdoors')
    elif time_of_day == "evening":
        print('Activity: Go and have nice dinner with a special someone')
    else:
        print('Invalid time of day')
elif day == "sunday":
    if time_of_day == "morning":
        print('Activity: Visit a local farmers market!!')
    elif time_of_day == "afternoon":
        print('Activity: Visit family or friends')
    elif time_of_day == "evening":
        print('Activity: Movie night!!')
    else:
        print('Invalid time of day')
else:
    print('Invalid day of the week. Please choose Monday, Saturday, or Sunday!')

