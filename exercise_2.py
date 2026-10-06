# Expense Tracker

expenses = []

def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\n----- EXPENSES -----")

        for expense in expenses:
            print("Category:", expense["category"])
            print("Amount:", expense["amount"])
            print("--------------------")


def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense:", total)


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")


        
