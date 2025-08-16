from db import insert_expense
from expense_report import yearly_expenses, monthly_expenses, category_summary

def print_banner():
    print("=" * 40)
    print("   🧾 Personal Expenses Tracker 🧾")
    print("=" * 40)

def print_menu():
    print("\nWhat would you like to do?")
    print(" 1️⃣  Add Expense")
    print(" 2️⃣  View Yearly Expenses Report")
    print(" 3️⃣  View Monthly Expenses Report")
    print(" 4️⃣  View Category Summary")
    print(" 5️⃣  Exit")

def main():
    while True:
        print_banner()
        print_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Add Expense ---")
            insert_expense()
        elif choice == "2":
            print("\n--- Yearly Expenses Report ---")
            yearly_expenses()
        elif choice == "3":
            print("\n--- Monthly Expenses Report ---")
            monthly_expenses()
        elif choice == "4":
            print("\n--- Category Summary ---")
            category_summary()
        elif choice == "5":
            print("\nThank you for using Personal Expenses Tracker!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()