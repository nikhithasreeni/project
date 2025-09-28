import json
import os

DATA_FILE = "accounts.json"

# ------------------- Account Class ------------------- #
class Account:
    def __init__(self, acc_number, name, balance=0.0):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def to_dict(self):
        return {
            "acc_number": self.acc_number,
            "name": self.name,
            "balance": self.balance
        }

# ------------------- Helper Functions ------------------- #
def load_accounts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_accounts(accounts):
    with open(DATA_FILE, 'w') as file:
        json.dump(accounts, file, indent=4)

def find_account(acc_number, accounts):
    for acc in accounts:
        if acc["acc_number"] == acc_number:
            return acc
    return None

# ------------------- Main Operations ------------------- #
def create_account():
    acc_number = input("Enter new account number: ")
    name = input("Enter account holder's name: ")

    accounts = load_accounts()
    if find_account(acc_number, accounts):
        print("Account already exists with that number.")
        return

    new_account = Account(acc_number, name)
    accounts.append(new_account.to_dict())
    save_accounts(accounts)
    print("Account created successfully!")

def deposit_money():
    acc_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))

    accounts = load_accounts()
    acc = find_account(acc_number, accounts)
    if acc:
        account_obj = Account(acc["acc_number"], acc["name"], acc["balance"])
        account_obj.deposit(amount)
        # Update in the list
        acc["balance"] = account_obj.balance
        save_accounts(accounts)
    else:
        print("Account not found.")

def withdraw_money():
    acc_number = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))

    accounts = load_accounts()
    acc = find_account(acc_number, accounts)
    if acc:
        account_obj = Account(acc["acc_number"], acc["name"], acc["balance"])
        account_obj.withdraw(amount)
        # Update in the list
        acc["balance"] = account_obj.balance
        save_accounts(accounts)
    else:
        print("Account not found.")

def view_account():
    acc_number = input("Enter account number: ")

    accounts = load_accounts()
    acc = find_account(acc_number, accounts)
    if acc:
        print("\n--- Account Details ---")
        print(f"Account Number: {acc['acc_number']}")
        print(f"Account Holder: {acc['name']}")
        print(f"Balance: ₹{acc['balance']}")
    else:
        print("Account not found.")

# ------------------- Main Menu Loop ------------------- #
def main():
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Details")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            view_account()
        elif choice == '5':
            print("Thank you for using the Bank Management System!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

# Run the program
if __name__ == "__main__":
    main()
