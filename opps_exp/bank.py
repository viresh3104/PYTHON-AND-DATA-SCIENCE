
class BankAccount:
    def __init__(self):
        self.accounts = {}  # Dictionary to store account information

    def create_account(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        account_number = input("Enter desired account number: ")

        # Check if account number already exists
        if account_number in self.accounts:
            print("Account number already taken. Please choose a different account number.")
        else:
            balance = float(input("Enter initial deposit amount: "))
            self.accounts[account_number] = {'name': name, 'age': age, 'balance': balance}
            print("Account created successfully!")

    def display_account_details(self, account_number):
        if account_number in self.accounts:
            account_info = self.accounts[account_number]
            print("\nAccount Details:")
            print(f"Name: {account_info['name']}")
            print(f"Age: {account_info['age']}")
            print(f"Account Number: {account_number}")
            print(f"Balance: ${account_info['balance']:.2f}")
        else:
            print("Account not found.")

    def deposit_money(self, account_number):
        if account_number in self.accounts:
            amount = float(input("Enter amount to deposit: $"))
            self.accounts[account_number]['balance'] += amount
            print(f"Amount deposited successfully. Updated balance: ${self.accounts[account_number]['balance']:.2f}")
        else:
            print("Account not found.")

    def withdraw_money(self, account_number):
        if account_number in self.accounts:
            amount = float(input("Enter amount to withdraw: $"))
            if amount > self.accounts[account_number]['balance']:
                print("Insufficient funds!")
            else:
                self.accounts[account_number]['balance'] -= amount
                print(f"Amount withdrawn successfully. Updated balance: ${self.accounts[account_number]['balance']:.2f}")
        else:
            print("Account not found.")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully!")
        else:
            print("Account not found.")


def main():
    account_system = BankAccount()

    while True:
        print("\n1. Create Account")
        print("2. Already Have an Account")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_system.create_account()
        elif choice == 2:
            account_number = input("Enter your account number: ")

            sub_choice = 0
            print("\n1. Display Account Details")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Delete Account")
            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                account_system.display_account_details(account_number)
            elif sub_choice == 2:
                account_system.deposit_money(account_number)
            elif sub_choice == 3:
                account_system.withdraw_money(account_number)
            elif sub_choice == 4:
                account_system.delete_account(account_number)
            else:
                print("Invalid choice!")

        choice = input("\nDo you want to perform another operation? (yes/no): ")
        if choice.lower() != 'yes':
            break

    print("Thank you for using the banking system program!")


if __name__ == "__main__":
    main()
