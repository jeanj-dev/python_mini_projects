# A poll that asks for user name and age
# Tell when the user will turn 100 based on their current age

from datetime import datetime

TARGET_AGE = 100

def get_valid_name():
    """Get valid name from user input."""

    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Invalid input! Please enter a name.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Invalid input! Names should contain letters and spaces only.")
            continue

        return name
    
        
def get_valid_age():
    """Get valid age from user input."""

    while True:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if age < 0:
            print("Invalid input! Please enter a valid age.")
        else:
            return age
        

def get_yes_no_response(prompt):
    """Get yes or no response from user input."""

    while True:
        response = input(prompt).strip().lower()

        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no.")


def calculate_birth_and_milestone_years(age, birthday_passed, current_year, target_age):
    """Calculate birth and milestone years."""

    if birthday_passed == "yes":
        year_born = current_year - age
    else:
        year_born = current_year - age - 1
    
    year_turning_hundred = year_born + target_age

    return year_born, year_turning_hundred


def build_poll_result(name, year_born, age, year_turning_hundred):
    """Build poll result."""
    person_result = {
        'name': name,
        'year_born': year_born,
        'current_age': age,
        'milestone_year': year_turning_hundred
    }
    return person_result


def display_poll_results(poll_results, target_age):
    """Display poll results."""
    for info in poll_results:
        print(f"\nHi {info['name'].title()}, you are {info['current_age']} years old.")
        print(f"You were born in {info['year_born']}.")

        if info['current_age'] >= target_age:
            print(f"You've already reached {target_age} years old.\n")
        else:
            print(f"You will turn {target_age} years old in {info['milestone_year']}.\n")
            

def run_poll():
    """Run the poll."""
    
    current_year = datetime.now().year

    # Create an empty list to store poll responses
    poll_results = []

    # Set a flag so that polling is active
    poll_active = True 

    while poll_active:
        name = get_valid_name()        
        age = get_valid_age()

        # Find out the year user was born 
        birthday_passed = get_yes_no_response("Has your birthday already occurred this year? (yes/no) ")
        year_born, year_turning_hundred = calculate_birth_and_milestone_years(age, birthday_passed, current_year, TARGET_AGE)
       
        # Store the participant poll result 
        poll_results.append(build_poll_result(name, year_born, age, year_turning_hundred))
    
        # Find out if more people want to take the poll
        repeat = get_yes_no_response("\nDoes anyone else want to try our poll? (yes/no) ")
        if repeat == "no":
            poll_active = False
            
    # Display the polls
    display_poll_results(poll_results, TARGET_AGE)


run_poll()

