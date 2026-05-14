
# A poll that asks for user name and age
# Tell when the user will turn 100 based on their current age

from datetime import datetime
current_year = datetime.now().year

# Create an empty dictionary
poll_results = {}

TARGET_AGE = 100

# Set a flag so that polling is active
poll_active = True

while poll_active:
    name = input("Enter your name: ").strip()
    if not name:
        print("Invalid input! Please enter a name.")
        continue
    
    # Ensure user enters correct input
    valid_age = False
    
    while not valid_age:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Inform user if they are already 100 years old
        if age < 0:
            print("Invalid input! Please enter a valid age.")
        elif age >= TARGET_AGE:
            print(f"Congratulations, {name.title()}! You've already reached the target age.") 
            valid_age = True     
        else:
            valid_age = True 

    # Find out the year user was born 
    year_born = current_year - age

    # Find what year the user reaches 100
    years_to_reach_hundred = TARGET_AGE - age
    year_turning_hundred = current_year + years_to_reach_hundred
    
    # Store age, birth year, and the year they turn 100 
    poll_results[name] ={
        'year_born': year_born,
        'your_current_age': age,
        'milestone_year': year_turning_hundred
    } 

    # Find out if more people want to take the poll
    repeat = input("\nDoes anyone else want to try our poll? (yes/no) ")
    if repeat.strip().lower() != 'yes':
        poll_active = False

# Display the polls
for name, info in poll_results.items():
    print(f"\nHi {name.title()}, you are {info['your_current_age']} years old.")
    print(f"You were born around {info['year_born']}.")

    if info['your_current_age'] >= TARGET_AGE:
        print(f"You've already reached {TARGET_AGE} years old.\n")
    else:
        print(f"You will turn {TARGET_AGE} years old in {info['milestone_year']}.\n")


