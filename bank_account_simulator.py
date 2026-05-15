# Create a bank account holder simulator

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
   
print(f"Hello {account_holder.title()}, your current balance is ${current_balance:.2f}\n")
    

account_menu = {1:"Deposit", 2:"Withdraw", 3:"Check balance", 4:"View transaction history", 5:"Exit"}

# Set flag variable to control the user logging activity
user_logging = True

while user_logging:

    # Prompt user to choose their account menu options
    print("Here are your account menu options:")
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
        if account_menu[choice] == "Deposit":
            try:
                deposit = float(input("Please enter your deposit amount: "))
            except ValueError:
                print("Invalid input! Numbers only.\n")
                continue

            if deposit <= 0:
                print("Deposit amount must be greater than $0.\n")
            else:
                current_balance += deposit
                transaction_history.append(f"Deposit: ${deposit:.2f}")
                print(f"{account_holder.title()}, your current balance is ${current_balance:.2f}\n")              
                                
        elif account_menu[choice] == "Withdraw":
            try:
                withdrawal = float(input("Please enter your withdrawal amount: "))
            except ValueError:
                print("Invalid input! Numbers only.\n")
                continue

            if withdrawal <= 0:
                print("Withdrawal amount must be greater than $0.\n")
            elif withdrawal > current_balance:
                print("Insufficient funds!\n")
            else:
                current_balance -= withdrawal
                print(f"{account_holder.title()}, your current balance is ${current_balance:.2f}\n")
                transaction_history.append(f"Withdraw: ${withdrawal:.2f}")
                                                   
        elif account_menu[choice] == "Check balance":
            print(f"Your current balance is ${current_balance:.2f}\n")

        elif account_menu[choice] == "View transaction history":
            if len(transaction_history) == 0:
                print("No transactions history.\n")
            else:
                print("\nTransaction history:")
                for transaction in transaction_history:
                    print(transaction)
                print()
            
        elif account_menu[choice] == "Exit":
            print("Goodbye!\n")

            user_logging = False

# Show the amount and type of transactions made
print(f"Your final balance is ${current_balance:.2f}")
print(f"You have made {len(transaction_history)} transactions.\n")

# Show final transactions history
if transaction_history:
    print("Final transaction history: ")
    for transaction in transaction_history:
        print(transaction)



