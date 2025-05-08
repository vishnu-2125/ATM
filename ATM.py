# Simple ATM program without functions

accounts = {
    "1234567890": {"pin": "1234", "balance": 5000},
    "9876543210": {"pin": "4321", "balance": 10000}
}

print("=== Welcome to Console ATM ===")
account_number = input("Enter your account number: ")
pin = input("Enter your 4-digit PIN: ")

if account_number in accounts and accounts[account_number]["pin"] == pin:
    print("Login successful!")

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            print(f"Your current balance is: ₹{accounts[account_number]['balance']}")

        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                accounts[account_number]['balance'] += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid deposit amount.")

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            if 0 < amount <= accounts[account_number]['balance']:
                accounts[account_number]['balance'] -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

else:
    print("Authentication failed. Invalid account number or PIN.")
