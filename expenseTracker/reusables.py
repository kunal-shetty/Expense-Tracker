from tkcalendar import DateEntry
import tkinter as tk

def createLabelEntry(parent, label_text, row, column):
    """Creates a label and entry in a grid layout"""
    tk.Label(parent, text=label_text).grid(row=row, column=column, padx=5, pady=5)
    entry = tk.Entry(parent)
    entry.grid(row=row, column=column+1, padx=5, pady=5)
    return entry

def createDateEntry(parent, row, column):
    """Creates a tkcalendar DateEntry"""
    tk.Label(parent, text="Date").grid(row=row, column=column, padx=5, pady=5)
    date_entry = DateEntry(parent, date_pattern='yyyy-mm-dd')
    date_entry.grid(row=row, column=column+1, padx=5, pady=5)
    return date_entry
