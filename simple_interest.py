# This program ask user input and calculate interest on money invest
def earning_interest():
    principal = float(input("Enter the principal: "))
    interest_rate = float(input("Enter the interest rate "))
    time = int(input("Enter the amount of time in years: "))

    interest_earned = principal * interest_rate * time / 100 
    print(f"Interest earned: ${interest_earned:.2f}") 

earning_interest() # Call to function