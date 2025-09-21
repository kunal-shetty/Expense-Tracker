import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from databaseConnection import addNewExpense, updateExpense, deleteExpense, getAllExpenses
from chartGenerators import showCategoryChart

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("950x550")
        self.selected_expense_id = None

        # ---- Input Frame ----
        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(frame, text="Expense Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Amount").grid(row=0, column=2, padx=5, pady=5)
        self.amount_entry = tk.Entry(frame)
        self.amount_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame, text="Category").grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Payment Mode").grid(row=1, column=2, padx=5, pady=5)
        self.payment_entry = tk.Entry(frame)
        self.payment_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(frame, text="Date").grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Description").grid(row=2, column=2, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame)
        self.desc_entry.grid(row=2, column=3, padx=5, pady=5)

        # ---- Buttons ----
        button_frame = tk.Frame(root, pady=10)
        button_frame.pack()
        tk.Button(button_frame, text="Add Expense", command=self.add_expense).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Update Expense", command=self.update_expense).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete Expense", command=self.delete_expense).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Clear Fields", command=self.clear_fields).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Show Category Chart", command=lambda: showCategoryChart()).grid(row=0, column=4, padx=5)

        # ---- Expense Table ----
        table_frame = tk.Frame(root)
        table_frame.pack(fill=tk.BOTH, expand=True)
        columns = ("expenseId", "expenseName", "expenseAmount", "description", "category", "paymentMode", "date")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

        self.load_expenses()

    # ---- Functions ----
    def load_expenses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for expense in getAllExpenses():
            self.tree.insert("", tk.END, values=expense)

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            expense_id = addNewExpense(
                self.name_entry.get(),
                amount,
                self.desc_entry.get(),
                self.category_entry.get(),
                self.payment_entry.get(),
                self.date_entry.get_date()
            )
            messagebox.showinfo("Success", f"Expense added! ID: {expense_id}")
            self.clear_fields()
            self.load_expenses()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_expense(self):
        if self.selected_expense_id:
            try:
                updateExpense(
                    self.selected_expense_id,
                    self.name_entry.get(),
                    float(self.amount_entry.get()),
                    self.desc_entry.get(),
                    self.category_entry.get(),
                    self.payment_entry.get(),
                    self.date_entry.get_date()
                )
                messagebox.showinfo("Success", "Expense updated!")
                self.clear_fields()
                self.load_expenses()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Selection Error", "Select an expense to update.")

    def delete_expense(self):
        if self.selected_expense_id:
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure?")
            if confirm:
                deleteExpense(self.selected_expense_id)
                messagebox.showinfo("Deleted", "Expense deleted!")
                self.clear_fields()
                self.load_expenses()
        else:
            messagebox.showwarning("Selection Error", "Select an expense to delete.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.payment_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.selected_expense_id = None

    def on_row_select(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            self.selected_expense_id = values[0]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[1])
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, values[2])
            self.desc_entry.delete(0, tk.END)
            self.desc_entry.insert(0, values[3])
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, values[4])
            self.payment_entry.delete(0, tk.END)
            self.payment_entry.insert(0, values[5])
            self.date_entry.set_date(values[6])

# ---------------------- Run App ----------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
