import matplotlib.pyplot as plt
from databaseConnection import getAllExpenses

def showCategoryChart(filterDate=None):
    """Displays a pie chart of expenses by category"""
    data = getAllExpenses()
    category_totals = {}
    for row in data:
        category = row[4]
        amount = float(row[2])
        category_totals[category] = category_totals.get(category, 0) + amount

    if category_totals:
        plt.figure(figsize=(6,6))
        plt.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%', startangle=140)
        plt.title("Expenses by Category")
        plt.show()
    else:
        print("No data to show.")
