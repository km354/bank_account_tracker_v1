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

    def withdraw_money(self):
        amount = input("Enter Amount: ")
        try:
            amount = float(amount)
            if amount > self.bank_balance():
                print("Error. Insufficient funds.")
            else:
                self.trackmoney.remove(amount)
                self.history.append(f' -{amount}')
                print(f"Your withdraw of ${amount} was successful")
        except ValueError:
            print("Error. Please enter a valid number.")

    def deposit_money(self):
        amount = input("Enter amount: ")
        try:
            amount = float(amount)
            self.trackmoney.append(amount)
            self.history.append(f'+ {amount}')
            print(f"Your deposit of ${amount} was successful")
            print(f"Your current balance is ${self.bank_balance()}")
            if amount <= 0:
                print("Error. You must deposit more than $0")
                return
        except ValueError:
            ("Error. Please try again. Numbers only")
            
    def view_transaction_history(self):
        print(self.history)
        
    def view_bank_balance(self):
        print(f"Your bank balance is ${self.bank_balance()}")

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
            bank.deposit_money()
        elif choice == "2" or choice.lower() == "withdraw money":
            bank.withdraw_money()
        elif choice == "3" or choice.lower() == "view account balance":
            bank.view_bank_balance()
        elif choice == "4" or choice.lower() == "view transaction history":
            bank.view_transaction_history()
        elif choice == "5" or choice.lower() == "leave the bank":
            break
        else:
            print("Error. Please try again!")

main()
