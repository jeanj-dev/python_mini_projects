# This program asks for user input and calculates interest on invested money
def calculate_simple_interest(principal, interest_rate, time):
    """Calculate simple interest."""
    return principal * interest_rate * time / 100 

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Wrong input! Numbers only!")

def get_interest_inputs():
    """Get valid simple interest inputs from the user."""
    principal = get_number("Enter the principal: ")
    interest_rate = get_number("Enter the interest rate (%): ")
    time = get_number("Enter the amount of time in years: ")
    return principal, interest_rate, time
        
def run_calculator():
    """Run the simple interest calculator."""
    principal, interest_rate, time = get_interest_inputs()
    interest_earned = calculate_simple_interest(principal, interest_rate, time)
    print(f"Interest earned: ${interest_earned:.2f}") 

run_calculator() 
