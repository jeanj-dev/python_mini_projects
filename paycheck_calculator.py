# This program asks for user input and computes weekly pay
def my_paycheck():
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    
    weekly_pay = hours_worked * hourly_rate
    print(f"I work ${weekly_pay:.2f} this week.") # Output

my_paycheck() 
