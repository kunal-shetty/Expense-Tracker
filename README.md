# Expense Tracker – Python Application

The **Expense Tracker** is a Python-based application designed for managing personal or organizational financial records with efficiency and clarity. The system supports adding, updating, and tracking expenses, along with generating visual insights through dashboards and charts. It is structured with modular Python files for maintainability, reusability, and scalability.

---

## Key Features

* **Expense Management:** Add, update, and manage daily expenses with ease.
* **Dashboard Interface:** Provides a centralized view for entering new expenses and reviewing existing ones.
* **Database Integration:** Uses a dedicated database connection module for stable and secure data handling.
* **Chart Generation:** Automatically generates charts and visual summaries through the `chartGenerators.py` module.
* **Modular Architecture:** Ensures clean code separation using reusable utilities and organized Python files.

---

## How It Works

1. **Database Connection**
   The `databaseConnection.py` file manages all database interactions, including insertion, updating, querying, and retrieval of expense records.

2. **Adding & Updating Expenses**
   The main application (`expenseTracker.py`) provides interfaces for adding new expenses and updating existing ones. Validation and reusable utilities are imported from the `reusable` module.

3. **Dashboard & User Flow**
   A dashboard-style interface displays recent expenses, total spending, and navigational options for adding or modifying entries.

4. **Chart Generation**
   The `chartGenerators.py` module processes expense categories, totals, and timelines to generate visual charts such as bar graphs, pie charts, or trend lines (using libraries like Matplotlib or similar).

---

## Technology Stack

* **Python 3.x** – Core programming language
* **SQLite / MySQL / PostgreSQL** *(depending on your DB implementation)* – Data storage
* **Matplotlib / Plotly** – Chart and visualization libraries
* **Standard Python Modules** – OS, datetime, etc.
* **Custom Modules** – Modular files for clean separation of concerns

---

## Summary

This Expense Tracker is built with a strong focus on modularity, clarity, and extensibility. It demonstrates practical use of Python for real-world applications, incorporating database handling, dashboard-style workflows, and chart visualization. The architecture makes it easy to extend and maintain, making it suitable for both personal use and more advanced financial management systems.
