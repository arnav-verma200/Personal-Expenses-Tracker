import sqlite3
conn =  sqlite3.connect("expenses/expenses.db")
cur = conn.cursor()

# Create categories table
cur.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
""")

# Create expenses table
cur.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category_id INTEGER,
    amount REAL,
    note TEXT,
    added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);
""")

default_categories = ["Food", "Transport", "Shopping", "Utilities", "Entertainment"]
for category in default_categories:
    cur.execute("INSERT OR IGNORE INTO categories (name) VALUES (?);", (category,))

conn.commit()
conn.close()

print("Database and tables created successfully.")
