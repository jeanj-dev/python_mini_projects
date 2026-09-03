# This program calculates the future value of an investment using compount interest.
def calculate_compound_interest(initial_principal, interest_rate, frequency, years):
    """Calculate compound interest."""
    principal = initial_principal

    for period in range(frequency * years):
            principal = principal * (1 + interest_rate / frequency) 
    return principal

def get_number(prompt):
    """Get a valid number from the user."""
    
    while True:
         try:
               number = float(input(prompt))

               if number <= 0:
                    print("Enter a positive number!")
                    continue
               
               return number
               
         except ValueError:
              print("Wrong input! Numbers only!")

def get_integer(prompt):
     """Get a valid integer from the user."""

     while True:
          try:
               num = int((input(prompt)))
               if num <= 0:
                    print("Enter a positive integer!")
                    continue
               
               return num
          
          except ValueError:
               print("Wrong input! Integer only!")

def get_compound_inputs():
    """Get valid compound interest inputs from the user."""
    initial_principal = get_number("Enter the principal: ")
    interest_rate = get_number("Enter the annual interest rate (e.g., 0.05 for 5%): " )

    years = get_integer("Enter the number of years to invest (positive integer only!): ")
    frequency = get_integer("Enter the number of times the interest is compounded per year: ")

    return initial_principal, interest_rate, frequency, years

def run_compound_calculator():
    initial_principal, interest_rate, frequency, years = get_compound_inputs()

    principal = calculate_compound_interest(initial_principal, interest_rate, frequency, years)
    print(f"The ${initial_principal:.2f} investment will be worth ${principal:.2f} dollars in {years} years.")

run_compound_calculator() # Call to function

