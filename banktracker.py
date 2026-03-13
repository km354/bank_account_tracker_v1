from datetime import datetime
import json

class BankTracker:
    def __init__(self):
        self.trackmoney = []
        self.history = []

    def bank_balance(self):
        total = 0
        for money in self.trackmoney:
            total += money
        return total

    def withdraw_money(self, amount):
        amount = input("Enter Amount: ")
        if amount.isdigit():
            self.trackmoney.remove(amount)
            self.history.append(f' -{amount}')
            print(f"Your withdraw of ${amount} was successful")
        else:
            print("Error. Make sure there is only numbers")

    def deposit_money(self, amount):
        amount = input("Enter amount: ")
        if amount.isdigit():
            self.trackmoney.append(amount)
            self.history.append(f'+ {amount}')
            print(f"Your deposit of ${amount} was successful")
            print(f"Your current balance is ${self.bank_balance()}")
        else:
            print("Error. Make sure to only have numbers")
            return

    def view_transaction_history(self):
        print(self.history)
        
    def view_bank_balance(self):
        print(self.trackmoney)

def main():
    bank = BankTracker()
    while True:
        print("\n Welcome to Anna State Bank. What would you like to do today?")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. View account balance")
        print("4. View Transaction History")
        print("5. Leave the Bank")

        choice = input("Enter Choice:")
        if choice == "1" or choice.lower() == "deposit money":
            bank.deposit_money(None)
        elif choice == "2" or choice.lower() == "withdraw money":
            bank.withdraw_money(None)
        elif choice == "3" or choice.lower() == "view account balance":
            bank.bank_balance()
        elif choice == "4" or choice.lower() == "view transaction history":
            bank.view_transaction_history()
        elif choice == "5" or choice.lower() == "leave the bank":
            break
        else:
            print("Error. Please try again!")

main()
