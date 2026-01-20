# This program asks for user input and calculates interest on invested money
def earning_interest():
    principal = float(input("Enter the principal: "))
    interest_rate = float(input("Enter the interest rate (%): "))
    time = int(input("Enter the amount of time in years: "))

    interest_earned = principal * interest_rate * time / 100 
    print(f"Interest earned: ${interest_earned:.2f}") 

earning_interest() 
