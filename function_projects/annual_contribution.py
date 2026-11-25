# This program computes the future value of an investment
# with a fixed annual contribution

def calculate_future_value(number_of_years, yearly_amount, yearly_rate):
    """Calculate future value."""
    total = 0

    for num in range(number_of_years):
        total += yearly_amount
        total *= (1 + yearly_rate / 100)

    return total


def get_yearly_contribution():
    """Get yearly contribution."""

    while True:
        try:
            yearly_amount = float(input("Enter the amount to invest each year: "))
            
            if yearly_amount <= 0:
                print("Positive numbers only!")
                continue

            return yearly_amount

        except ValueError:
            print("Wrong input! Numbers only!")


def get_annual_rate():
    """Get annual rate."""
    valid_yearly_rate = False

    while not valid_yearly_rate:
        try:
            yearly_rate = float(input("Enter the yearly_rate (5 for 5%): " ))
            
            if yearly_rate < 0:
                print("Non-negative numbers only!")
            else:
                valid_yearly_rate = True

        except ValueError:
            print("Wrong input! Numbers only!")

    return yearly_rate


def get_num_of_years():
    """Get number of years."""
    
    while True:
        try:
            num_of_years = int(input("Enter the number of years to invest: "))
            
            if num_of_years <= 0:
                print("Positive integers only!")
                continue

            return num_of_years
    
        except ValueError:
            print("Wrong input! Numbers only!")


def run_annual_contribution():
    """Run annual contribution investment."""

    yearly_amount = get_yearly_contribution()
    yearly_rate = get_annual_rate()   
    number_of_years = get_num_of_years()

    total_growth = calculate_future_value(number_of_years, yearly_amount, yearly_rate)
    print(f"The ${yearly_amount:.2f} invested every year will be worth ${total_growth:.2f} dollars in {number_of_years} years.")


run_annual_contribution()
