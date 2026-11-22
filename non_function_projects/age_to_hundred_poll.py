
# A poll that asks for user name and age
# Tell when the user will turn 100 based on their current age

from datetime import datetime
current_year = datetime.now().year

# Create an empty list to store poll responses
poll_results = []

TARGET_AGE = 100

# Set a flag so that polling is active
poll_active = True

while poll_active:
    name = input("Enter your name: ").strip()
    if not name:
        print("Invalid input! Please enter a name.")
        continue
    if not name.replace(" ", "").isalpha():
        print("Invalid input! Names should contain letters and spaces only.")
        continue
    
    # Ensure user enters correct input
    valid_age = False
    
    while not valid_age:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Reject negative ages
        if age < 0:
            print("Invalid input! Please enter a valid age.")
        else:
            valid_age = True 

    # Find out the year user was born 

    while True:
        birthday_passed = input(
            "Has your birthday already occurred this year? (yes/no) "
        ).strip().lower()

        if birthday_passed in ["yes", "y"]:
            year_born = current_year - age
            break
        elif birthday_passed in ["no", "n"]:
            year_born = current_year - age - 1
            break
        else:
            print("Please enter yes or no.")
            
    # Find what year the user reaches 100
    year_turning_hundred = year_born + TARGET_AGE
    
    # Store age, birth year, and the year they turn 100 
    poll_results.append({
        'name': name,
        'year_born': year_born,
        'your_current_age': age,
        'milestone_year': year_turning_hundred
    })
    

    # Find out if more people want to take the poll
    while True:
        repeat = input("\nDoes anyone else want to try our poll? (yes/no) ").strip().lower()
        if repeat in ['yes', 'y']:
            break
        elif repeat in ['no', 'n']:
            poll_active = False
            break
        else:
            print("Please enter yes or no.")

# Display the polls
for info in poll_results:
    print(f"\nHi {info['name'].title()}, you are {info['your_current_age']} years old.")
    print(f"You were born in {info['year_born']}.")

    if info['your_current_age'] >= TARGET_AGE:
        print(f"You've already reached {TARGET_AGE} years old.\n")
    else:
        print(f"You will turn {TARGET_AGE} years old in {info['milestone_year']}.\n")


