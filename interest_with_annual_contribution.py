# This program computes the future value of an investment
# with a fixed annual contribution
def annual_contribution():
    yearly_amount = float(input("Enter the amount to invest each year: "))
    yearly_rate = float(input("Enter the yearly_rate (e.g., 0.05 or .05 for 5%): " ))
    num_of_years = int(input("Enter the number of years to invest: "))
    
    total = 0
    # Add annual contribution and apply yearly growth
    for n in range(num_of_years):
        total = total + yearly_amount
        total = total * ( 1 + yearly_rate)

    print(f"The ${yearly_amount:.2f} invested every year will be worth ${total:.2f} dollars in {num_of_years} years.")

annual_contribution()
