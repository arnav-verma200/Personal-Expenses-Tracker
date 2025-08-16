## 🧾 Personal Expenses Tracker
A Python-based expense tracking system using **SQLite** for storage, **Pandas** for clean tabular reports, and **Matplotlib** for visualizations.  
Track your expenses, view yearly/monthly trends, and analyze spending categories with ease.

---

## 📁 Project Structure

```

.
├── main.py               # Entry point (menu-driven CLI for tracker)
├── db.py                 # Database functions (insert & connect to SQLite)
├── expense\_report.py     # Reports: yearly, monthly, and category summary
├── expenses/expenses.db  # SQLite database file (auto-created)
└── README.md             # Documentation

```


## 🧠 Features
```
📅 **Yearly Expenses** – View monthly breakdown + total yearly spend (Pie Chart)
📆 **Monthly Expenses** – Track daily spending trends (Line Graph)
📊 **Category Summary** – Analyze spending by category (Yearly or Monthly) with Bar Graph
💾 **SQLite Database** – Persistent local storage for all expenses
📋 **Pandas Reports** – Clean and readable tabular summaries

---
```
## 🚀 Getting Started

### 📦 Requirements
```
* Python 3.7+
* Pandas
* Matplotlib
* SQLite (comes pre-installed with Python)
```
### 📥 Install dependencies
```
```bash
pip install pandas matplotlib
```

---

## ▶️ How to Run

Run the tracker from the terminal:

```bash
python main.py
```

You’ll see a **menu** like this:

```bash
========================================
   🧾 Personal Expenses Tracker 🧾
========================================

What would you like to do?
 1️⃣  Add Expense
 2️⃣  View Yearly Expenses Report
 3️⃣  View Monthly Expenses Report
 4️⃣  View Category Summary
 5️⃣  Exit
```

---

## 🛠️ File Details

* **main.py** – Entry point; displays menu and routes user to the right function.
* **db.py** – Handles database connection and adding expenses to SQLite.
* **expense\_report.py** – Generates reports:

  * `yearly_expenses()` → Monthly breakdown + total (Pie Chart)
  * `monthly_expenses()` → Daily spend trends (Line Graph)
  * `category_summary()` → Category-wise breakdown (Bar Graph, yearly/monthly choice)

---

## 🔮 Future Improvements


- 🌐 **Full-stack apps with UI/UX design** — building interactive and clean user interfaces.  
- 📸 **OpenCV-based automation** — capture photos of bills/receipts and automatically extract data.  
- 📊 **Expense Trend Analyzer** — predict approximate spending (e.g., “September expenses will be ~₹X”) using ML.  
- 🚨 **Smart Alerts** — notify when too much money is spent on one category or when unusual transactions appear.  

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to add new features (export, GUI, ML insights), feel free to fork and contribute.


