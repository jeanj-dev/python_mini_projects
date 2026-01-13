# This program ask for user input and compute hourly work and rate
def my_paycheck():
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    
    total_pay = hours_worked * hourly_rate
    print(f"I work ${total_pay:.2f} this week.") # Output

my_paycheck() # call to function