# This program computes the future value of an investment
# with a fixed annual contribution

while True:
    try:
        yearly_amount = float(input("Enter the amount to invest each year: "))
        if yearly_amount <= 0:
            print("Positive numbers only!")
            continue

        break

    except ValueError:
        print("Wrong input! Numbers only!")

valid_yearly_rate = False

while not valid_yearly_rate:
    try:
        yearly_rate = float(input("Enter the yearly_rate (5 for 5%): " ))
        if yearly_rate < 0:
            print("Positive numbers only!")
        else:
            valid_yearly_rate = True

    except ValueError:
        print("Wrong input! Numbers only!")

while True:
    try:
        num_of_years = int(input("Enter the number of years to invest: "))
        if num_of_years <= 0:
            print("Positive integers only!")
            continue

        break
    
    except ValueError:
        print("Wrong input! Numbers only!")
    
total = 0
# Add annual contribution and apply yearly growth
for n in range(num_of_years):
    total = total + yearly_amount
    total = total * ( 1 + yearly_rate / 100)

print(f"The ${yearly_amount:.2f} invested every year will be worth ${total:.2f} dollars in {num_of_years} years.")

