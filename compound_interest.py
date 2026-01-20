# This program calculate the future value of an investment using compount interest
def compound_interest():
    initial_principal = float(input("Enter the principal: "))
    interest_rate = float(input("Enter the annual interest rate (e.g., 0.05 for 5%): " ))

    frequency = int(input("Enter the number of times the interest is compounded per year: "))
    num_of_years = int(input("Enter the number of years to invest (positive integer only!): "))
    
    principal = initial_principal

    for period in range(frequency * num_of_years):
        principal = principal * (1 + interest_rate / frequency) 
    print(f"The ${initial_principal:.2f} investment will be worth ${principal:.2f} dollars in {num_of_years} years.")

compound_interest() # Call to function

