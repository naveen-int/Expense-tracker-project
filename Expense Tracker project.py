
import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def print_heading(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)

def add_expense():
    print_heading("➕ Add New Expense")
    category = input("Enter category (Food, Travel, etc.): ").strip()

    while True:
        try:
            amount = float(input("Enter amount (₹): "))
            break
        except ValueError:
            print("❗ Please enter a valid number.")

    description = input("Enter description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("\n✅ Expense saved successfully!")

def view_expenses():
    print_heading("📄 All Expense Records")
    if not os.path.exists(FILENAME):
        print("No expense records found.")
        return

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        rows = list(reader)

    if not rows:
        print("No expenses to display.")
        return

    print(f"{'Date':<20} {'Category':<15} {'Amount':<10} Description")
    print("-" * 60)

    for row in rows:
        print(f"{row[0]:<20} {row[1]:<15} ₹{row[2]:<10} {row[3]}")

def total_expenses():
    print_heading("💰 Total Expense Summary")
    total = 0.0

    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                total += float(row[2])
        print(f"\n📊 Total Spent: ₹{total:.2f}")
    except FileNotFoundError:
        print("No expenses found.")

def delete_history():
    print_heading("⚠️ Delete All Expenses")
    confirm = input("Are you sure you want to delete all records? (yes/no): ").strip().lower()
    
    if confirm == "yes":
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
        print("🗑️ All expenses cleared!")
    else:
        print("❌ Deletion cancelled.")

def show_menu():
    while True:
        print_heading("📌 Expense Tracker Menu")
        print("1. ➕ Add Expense")
        print("2. 📄 View All Expenses")
        print("3. 💰 View Total Expenses")
        print("4. 🗑 Delete All Expense History")
        print("5. ❎ Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            delete_history()
        elif choice == "5":
            print("\n👋 Thank you for using the Expense Tracker!")
            print("🧑‍💻 Developed by Naveen S\n")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    init_file()
    show_menu()
