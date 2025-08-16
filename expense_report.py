import matplotlib.pyplot as plt
import pandas as pd
from db import *
import calendar

def get_expense_df():
  #making pandas
  expense_data = fetch_expenses()
  data = {
    "id": [],
    "date": [],
    "money": [],
    "category": []
  }
  for expense in expense_data:
    data["id"].append(expense[0])
    data["date"].append(expense[1])
    data["money"].append(expense[2])
    data["category"].append(expense[3])

  df = pd.DataFrame(data)
  return(df)

def yearly_expenses():
  df = get_expense_df()
  df['date'] = pd.to_datetime(df['date'])
  df_year = df[df['date'].dt.year == 2025]
  yearly_spend = df_year["money"].sum()
  print(f"\nThe yearly spend is : ₹{yearly_spend}\n")
  print("Monthly break down is :")
  
  month_expenses = [] 
  month_names_for_pie = []

  for month in range(1, 13):
    df_month = df[df['date'].dt.month == month]
    if df_month.empty:
      continue
        
    month_name = df_month['date'].dt.strftime('%B').iloc[0]
    monthly_sum = df_month["money"].sum()
    print(f"Expenses for {month_name} is ₹{monthly_sum}")

    month_expenses.append(monthly_sum)
    month_names_for_pie.append(month_name)
  
  plt.pie(month_expenses, labels=month_names_for_pie, autopct='%1.1f%%', colors = ['lightcoral', 'lightblue', 'lightgreen', 'wheat', 
                                                                                  'plum', 'powderblue', 'thistle', 'paleturquoise', 
                                                                                  'moccasin', 'pink', 'palegreen', 'lavender'])
  plt.title("2025 Monthly Spending Breakdown", fontsize=17)
  plt.text(0, -1.3, f"Total Money Spend is ₹{yearly_spend}", ha='center', fontsize=13)
  plt.tight_layout()
  plt.show()



def monthly_expenses():
  df = get_expense_df()
  df['date'] = pd.to_datetime(df['date'])

  month_name = input("Enter month name (e.g., July): ").capitalize()
  month_num = list(calendar.month_name).index(month_name)

  # Filter data for that month
  df_month = df[df['date'].dt.month == month_num]
  if df_month.empty:
    print(f"No expenses found for {month_name}.")
    return
  
  print(f"\n=== Expenses for {month_name} ===")
  print(df_month.to_string(index=False))

  monthly_sum = df_month["money"].sum()
  print(f"\nTotal spending in {month_name}: ₹{monthly_sum}")

  category_summary = df_month.groupby("category")["money"].sum()
  print("\nCategory-wise spending:")
  print(category_summary)


  df_month = df_month.sort_values("date")
  plt.figure(figsize=(10,6))
  plt.plot(df_month["date"], df_month["money"], marker="o", linestyle="-", color="blue")

  plt.title(f"Expenses in {month_name}", fontsize=16)
  plt.xlabel("Date", fontsize=12)
  plt.ylabel("Money Spent (₹)", fontsize=12)
  plt.grid(True, linestyle="--", alpha=0.6)
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

def category_summary():
  df = get_expense_df()
  df['date'] = pd.to_datetime(df['date'])

  choice = input("Do you want yearly or monthly summary? (yearly/monthly): ").lower()

  if choice == "yearly":
    print("\n=== Yearly Category Summary ===")
    yearly_summary = df.groupby("category")["money"].sum()
    print(yearly_summary)

    yearly_summary.plot(kind="bar", color="skyblue", figsize=(8,6))
    plt.title("Yearly Category-wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Total Spending (₹)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

  elif choice == "monthly":
    month_name = input("Enter month name (e.g., July): ").capitalize()
    try:
      month_num = list(calendar.month_name).index(month_name)
    except ValueError:
      print("Invalid month name.")
      return

    df_month = df[df['date'].dt.month == month_num]

    if df_month.empty:
      print(f"No expenses found for {month_name}.")
      return

    print(f"\n=== Category Summary for {month_name} ===")
    monthly_summary = df_month.groupby("category")["money"].sum()
    print(monthly_summary)

    monthly_summary.plot(kind="bar", color="orange", figsize=(8,6))
    plt.title(f"Category-wise Spending in {month_name}")
    plt.xlabel("Category")
    plt.ylabel("Total Spending (₹)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

