
# 1-This program compute hourly work
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))
total_pay = hours_worked * hourly_rate
print(f"{total_pay:.2f}")

# 2a- This program convert Fahrenheit to Celsius
fahrenheit = float(input("Enter the Fahrenheit temperature: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{celsius:.2f}")

# 2b- This program convert Celsius to Fahrenheit
celsius = float(input("Enter the Celsius temperature: "))
fahrenheit =  celsius * 9 / 5 + 32
print(f"{fahrenheit:.2f}")

# 3- This program calculate interest on money invest or borrow
principal = float(input("Enter the principal: "))
interest_rate = int(input("Enter the interest rate (e.g., positive integer only): "))
time = int(input("Enter the amount of time in years: "))
interest_earned = principal * interest_rate * time / 100
print(f"{interest_earned:.2f}")

# 4- This program calculate the average test score
first_score = int(input("Enter the first test score: "))
second_score = int(input("Enter the second test score: "))
third_score = int(input("Enter the third test score: "))
average = (first_score + second_score + third_score) / 3
print(f"{average:.1f}")

# 5- This program calculate tip and total amount
bill_amount = float(input("Enter the bill amount: "))
tip_percentage = int(input("Enter the tip percentage (e.g., positive integer only): "))
tip = bill_amount * tip_percentage / 100
total_bill = bill_amount + tip
print(f"Tip: ${tip:.2f} Total: ${total_bill:.2f}")

# 6- This program calculate a rectangular room
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area} perimeter: {perimeter}")

# 7- This program converts time hours and remaining minutes
minutes = int(input("Enter the number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")

# 8- This program calculate the total groceries plus taxed purchased
first_item = float(input("Enter price of the first item: "))
second_item = float(input("Enter price of the second item: "))
third_item = float(input("Enter the price of the third item: "))
tax_rate = 0.09
subtotal = first_item + second_item + third_item
taxes = subtotal * tax_rate
total = subtotal + taxes
print(f"subtotal: ${subtotal:.2f} taxes: ${taxes:.2f} total: ${total:.2f}")
