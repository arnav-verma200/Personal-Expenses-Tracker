import sqlite3

def insert_expense():
  conn =  sqlite3.connect("expenses\expenses.db")
  cur = conn.cursor()

  date = input("Enter the date (YYYY-MM-DD): ")

  amount = float(input("Enter the amount: "))

  print("\nAvailable Categories:")
  cur.execute("SELECT id, name FROM categories")
  categories = cur.fetchall()
  for cat in categories:
    print(f"{cat[0]} - {cat[1]}")

  category_id = int(input("Enter the category ID: "))

  note = input("Enter any details (or type 'no' for no comment): ")
  if note.strip().lower() == "no" or note.strip() == "":
    note = "No comment"
    
  cur.execute("""
              INSERT INTO expenses (date, category_id, amount, note)
              VALUES (?, ?, ?, ?)
              """, (date, category_id, amount, note))
  
  conn.commit()
  conn.close()
  print("Added Succesfully ")


def fetch_expenses():
  conn = sqlite3.connect("expenses\expenses.db")
  cursor = conn.cursor()
    
  cursor.execute("""
        SELECT expenses.id, expenses.date, expenses.amount, categories.name AS category
        FROM expenses
        JOIN categories ON expenses.category_id = categories.id
    """)
    
  rows = cursor.fetchall()
    
  conn.close()
  return rows