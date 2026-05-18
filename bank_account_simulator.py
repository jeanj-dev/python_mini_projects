# Create a bank account holder simulator

# Set flag variable to control the user logging activity
user_logging = False
correct_pin = 1234
tries = 3

# Create initial values menu
# create an empty list to store transaction history
current_balance = 0
transaction_history = []

# Greet the customers and inform them of their account balance
print("Welcome to Village Bank!")

# Ensure user doesn't enter empty strings
while True:
    account_holder = input("Please, enter your name: ").strip()
    if account_holder != "":
        break

    print("Name cannot be empty.")
   
print(f"Hello {account_holder.title()}!")

# Ensure user enter correct pin
# Ensure account is locked after three tries
while tries > 0:
    try:
        pin_number = int(input("Enter your pin number: "))
    except ValueError:
        print("Invalid input! Numbers only.\n")
        continue  

    # only display menu when user enters correct pin
    if pin_number == correct_pin:
        print(f"Access Granted! {account_holder.title()}")
        print("\nHere are your account menu options:")
        user_logging = True
        break
    else: 
        tries -= 1
        if tries == 0:
            print("Too many incorrect attempts. Account Locked.\n")
            user_logging = False
        else:
            print(f"Incorrect! {tries} attempt{'s' if tries != 1 else ''} remaining")

    
               
account_menu = {1:"Deposit", 2:"Withdraw", 3:"Check balance", 4:"View transaction history", 5:"Exit"}

while user_logging:
    # Only display menu when user enters the correct pin
    # Prompt user to choose their account menu options
    
    for key, value in account_menu.items():
        print(f"{key} = {value}")
    print()

    # Ensure users enter only number
    try:
        choice = int(input("Enter a number in the menu option (1, 2, 3, 4 or 5): ")) 
    except ValueError:
        print("Invalid input! Please enter a number only.\n")
        continue
    
    if choice not in account_menu:
        print("Invalid choice! Please enter a valid choice in the account menu options.\n")
        
    else:
        
        # Ensure users enter only numbers
        if choice == 1:
            try:
                deposit = float(input("Please enter your deposit amount: "))
            except ValueError:
                print("Invalid input! Numbers only.\n")
                continue

            if deposit <= 0:
                print("Deposit amount must be greater than $0.\n")
            else:
                current_balance += deposit
                transaction_history.append(f"Deposit: ${deposit:.2f} | Balance: ${current_balance:.2f}")
                print(f"Deposit: ${deposit:.2f} | Balance: ${current_balance:.2f}\n")              
                                
        elif choice == 2:
            try:
                withdrawal = float(input("Please enter your withdrawal amount: "))
            except ValueError:
                print("Invalid input! Numbers only.\n")
                continue

            if withdrawal <= 0:
                print("Withdrawal amount must be greater than $0.\n")
            elif withdrawal > current_balance:
                print(f"Insufficient funds! -- Balance: ${current_balance:.2f}\n")
            else:
                current_balance -= withdrawal
                transaction_history.append(f"Withdraw: ${withdrawal:.2f} | Balance: ${current_balance:.2f}")
                print(f"Withdraw: ${withdrawal:.2f} | Balance: ${current_balance:.2f}\n")
                                  
        elif choice == 3:
            print(f"Your current balance is ${current_balance:.2f}\n")

        elif choice == 4:
            if len(transaction_history) == 0:
                print("No transaction history.\n")
            else:
                print("\nTransaction history:")
                for transaction in transaction_history:
                    print(transaction)
                print()
            
        elif choice == 5:
            print("Goodbye!\n")
            print(f"Your final balance is ${current_balance:.2f}")
            print(f"You have made {len(transaction_history)} transactions.\n")
            user_logging = False

# Show the amount and type of transactions made
# Show final transactions history
if transaction_history:
    print("Final transaction history: ")
    for transaction in transaction_history:
        print(transaction)
        



