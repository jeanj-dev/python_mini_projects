# This program calculates the tip and total bill amount
# based on user input
def calculate_tip_and_total(tip_rate, bill_amount):
    """Calculate the tip and bill amount."""
    total_tip = bill_amount * tip_rate / 100
    total_bill = bill_amount + total_tip
    return total_tip, total_bill

def get_amount(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Positive number only!")
                continue

            return amount

        except ValueError:
            print("Wrong input! Numbers only!")

def get_bill_amounts():
    """Get the tip percentage and bill amount from the user."""
    tip_percentage = get_amount("Enter the tip percentage: ")
    bill_amount = get_amount("Enter the bill amount: ")

    return tip_percentage, bill_amount
    
def run_tip_calculator():
    """Run the tip calculator."""
    tip_percentage, bill_amount = get_bill_amounts()
    total_tip, total_bill = calculate_tip_and_total(tip_percentage, bill_amount)
    print(f"Tip: ${total_tip:.2f} Total: ${total_bill:.2f}")

run_tip_calculator()
