# This program computes the future value of an investment
# with a fixed annual contribution
def future_value_investment(yearly_amount, yearly_rate, num_of_years):
    """Calculate the annual contribution and the yearly growth."""
    total = 0
    for n in range(num_of_years):
        total = total + yearly_amount
        total = total * (1 + yearly_rate / 100)

    return total

def get_positive_number(prompt):
    """Get a positive number from the user."""
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                print("Positive number only!")
                continue

            return num

        except ValueError:
            print("Wrong input! Numbers only!")

def get_positive_integer(prompt):
    """Get a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Positive number only!")
                continue

            return value

        except ValueError:
            print("Wrong input! Numbers only!")

def get_right_inputs():
    """Get valid investment inputs from the user."""
    yearly_amount = get_positive_number("Enter the amount to invest each year: ")
    yearly_rate = get_positive_integer("Enter the yearly interest rate (5 for 5%): " )
    num_of_years = get_positive_integer("Enter the number of years to invest: ")

    return yearly_amount, yearly_rate, num_of_years

def run_investment_calculator():
    """Run the investment calculator."""
    yearly_amount, yearly_rate, num_of_years = get_right_inputs()
    total = future_value_investment(yearly_amount, yearly_rate, num_of_years)
    print(f"The ${yearly_amount:.2f} invested every year will be worth ${total:.2f} dollars in {num_of_years} years.")

run_investment_calculator()