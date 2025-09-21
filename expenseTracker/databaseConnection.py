
import pymysql

def connectToDatabase():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="Expenses"
    )

def getAllExpenses():
    conn = connectToDatabase()
    cur = conn.cursor()

    query = """
        SELECT expenseName, expenseAmount, description, category, paymentMode, date
        FROM Expenses
        WHERE del = 0
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        expenseName = row[0]
        expenseAmount = float(row[1])  # Convert Decimal -> float
        description = row[2]
        category = row[3]
        paymentMode = row[4]
        date = row[5].strftime("%Y-%m-%d") # Convert date -> string

        print(expenseName, expenseAmount, description, category, paymentMode, date)

    conn.close()
    return rows

def getOneExpense(expenseId):
    conn = connectToDatabase()
    cur = conn.cursor()

    query = """
            SELECT expenseName, expenseAmount, description, category, paymentMode, date
            FROM Expenses
            WHERE expenseId = %s AND del = 0 
        """
    params = (expenseId,)
    cur.execute(query, params)
    row = cur.fetchone()
    if row:
        expenseName = row[0]
        expenseAmount = float(row[1])           # Decimal -> float
        description = row[2]
        category = row[3]
        paymentMode = row[4]
        date = row[5].strftime("%Y-%m-%d")      # date -> string

        print(expenseName, expenseAmount, description, category, paymentMode, date)
    else:
        print("No expense found with given ID")

    conn.close()

def addNewExpense(expenseName, expenseAmount, description, category, paymentMode, date):
    conn = connectToDatabase()
    cur = conn.cursor()

    query = """
        INSERT INTO Expenses (expenseName, expenseAmount, description, category, paymentMode, date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (expenseName, expenseAmount, description, category, paymentMode, date)
    cur.execute(query, values)
    conn.commit()

    inserted_id = cur.lastrowid   # Get the auto-generated expenseId
    conn.close()

    return inserted_id

def updateExpense(expenseId, expenseName, expenseAmount, description, category, paymentMode, date):
    conn = connectToDatabase()
    cur = conn.cursor()

    query = """
        UPDATE Expenses
        SET expenseName = %s,
            expenseAmount = %s,
            description = %s,
            category = %s,
            paymentMode = %s,
            date = %s
        WHERE expenseId = %s AND del = 0
    """
    values = (expenseName, expenseAmount, description, category, paymentMode, date, expenseId)
    cur.execute(query, values)
    conn.commit()
    print("Rows updated:", cur.rowcount)
    conn.close()

def deleteExpense(expenseId):
    conn = connectToDatabase()
    cur = conn.cursor()

    query = """UPDATE Expenses
             SET del = 1
             WHERE expenseId = %s"""
    params = (expenseId,)
    if cur.execute(query, params):
        print("Row with ID", expenseId, "DELETED successfully")
    else:
        print("No row with given ID exists")
    conn.commit()
    conn.close()

addNewExpense(
    "Grocery Shopping",                # expenseName
    1250.75,                           # expenseAmount
    "Bought vegetables, fruits, and snacks",  # description
    "Food",                             # category
    "UPI",                               # paymentMode
    "2025-09-18"                         # date (YYYY-MM-DD)
)
