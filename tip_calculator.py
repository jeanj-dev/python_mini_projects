# This program calculate tip and total amount
def tip_your_waiter():
    bill_amount = float(input("Enter the bill amount: "))
    tip_percentage = int(input("Enter the tip percentage (e.g., positive integer only): "))
    
    tip_amout = bill_amount * tip_percentage / 100
    total_bill_amount = bill_amount + tip_amout

    print(f"Tip: ${tip_amout:.2f} Total: ${total_bill_amount:.2f}")

tip_your_waiter()