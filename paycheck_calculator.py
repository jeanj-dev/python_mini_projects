# This program asks for user input and computes weekly pay
def calculate_weekly_pay(hours_worked, hourly_rate):
    """Calculate weekly pay."""
    return hours_worked * hourly_rate

def get_positive_number(prompt):
    """Get a valid positive number from the user.""" 
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                print("Positive number only!")
                continue

            return number
    
        except ValueError:
            print("Wrong input! Please enter a number!")
        
def get_hours_inputs():
    """Get paycheck inputs from the user."""
    hours_worked = get_positive_number("Enter hours worked: ")
    hourly_rate = get_positive_number("Enter hourly rate: ")
    return hours_worked, hourly_rate

def run_paycheck_calculator():
    """Run the paycheck calculator."""
    hours_worked, hourly_rate = get_hours_inputs()
    weekly_pay = calculate_weekly_pay(hours_worked, hourly_rate)
    print(f"I earned ${weekly_pay:.2f} this week.") # Output

run_paycheck_calculator()
