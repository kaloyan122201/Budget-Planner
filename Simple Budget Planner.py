import tkinter
from tkinter import *
#Asking for user's information
def asking_info():
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()
    user = first_name + " " + last_name
    starting_income = float(input(f"Okay {user} what is your monthly income: "))
    currency = input("Enter currency: ")
    return user,income,currency
#Printing the menu
def show_menu():
    options = ["Add Income", "Add Expense", "View Current Balance", "Show All Income", "Show All Expenses", "Exit"]
    counter = 1
    print()
    for option in options:
        print(f"{counter}: {option}", end=" ")
        counter += 1
    print()
#Adding additional income to dictionary so i can print it if the user wants to see all his/her income sources
def adding_incomes(dictionary_income,balance,symbol):
    print("Enter additional income in format: category-amount")
    print("Press [Enter] to go back.")
    while True:
        try:
            command = input()
            if command == "":
                break
            expenses_parts = command.split("-")
            source, amount = expenses_parts[0], float(expenses_parts[1])
            source = source.title()
            if source not in dictionary_income.keys():
                dictionary_income[source] = 0
            dictionary_income[source] = amount
            if amount <= 0:
                print("Income must be a positive number. Try again.")
                continue
            if amount > 1_000_000:
                confirm = input("That’s quite high! Are you sure? (y/n): ")
                if confirm.lower() != 'y':
                    continue

            balance += amount
            print(f"Income added. New balance: {balance:.2f}{symbol}")
            break
        except ValueError:
            print("Invalid number. Please enter a numeric value.")

    return dictionary_income,balance

#Adding additional expenses to dictionary so i can print it if the user wants to see all his/her expense sources
def adding_expenses(dict_expenses,balance:float,currency):
    print("Enter expenses in format: category-amount")
    print("Press [Enter] to go back.")
    while True:
        command = input()
        if command == "":
            break
        expenses_parts = command.split("-")
        source, amount = expenses_parts[0], float(expenses_parts[1])
        source = source.title()

        if balance - amount<0:
            print("You cannot afford to pay for this expense.")
            print(f"Current Balance: {balance:.2f}{currency}")
            break
        elif balance-amount ==0:
            balance-=amount
            print(f"You spent your last money from your bank account!")
        else:
            balance-=amount
        if source not in dict_expenses.keys():
            dict_expenses[source] = 0
        dict_expenses[source] = amount
        print(f"Current Balance: {balance:.2f}{currency}")

    return dict_expenses,balance
#take the dictionary with expenses and print each one on a new line
def view_expenses(current_expenses,final_symbol):
    total = 0
    for expense,amount in current_expenses.items():
        print(f"•{expense}  -{amount:.2f}{final_symbol}")
        total+=amount
    print("____________________")
    print(f"Total: {total:.2f}")
#take the dictionary with income sources and print each one on a new line
def view_incomes(dictionary_income,symbol):
    total = 0
    for balance,amount in dictionary_income.items():
        print(f"•{balance}  +{amount:.2f}{symbol}")
        total+=amount
    print("____________________")
    print(f"Total: {total:.2f}")

#printing options
def choosing_option(expenses,income,symbol,dictionary_income):
    while True:
        show_menu()
        try:
            choice = int(input("\nEnter a number: "))
        except ValueError:
            print("Enter a number between 1 and 6")
            continue
        if choice == 1:
            dictionary_income,income =adding_incomes(dictionary_income,income,symbol)
        elif choice == 2:

            current_expenses, current_income = adding_expenses(expenses,income,symbol)
            income = current_income
        elif choice == 3:
            print(f"Current balance: {income:.2f}{symbol}")
        elif choice == 4:
            view_incomes(dictionary_income,symbol)
        elif choice == 5:
            view_expenses(expenses,symbol)
        elif choice == 6:
            break


#6. Simple Budget Planner

print("Welcome to your personal budget planner.")
full_name,income,currency = asking_info()
dict_incomes={}
expenses = {}
print(f"{full_name} you have {income:.2f}{currency}")
choosing_option(expenses,income,currency,dict_incomes)
print("Thank you for using your Budget Planner!\n Have a good day.")





