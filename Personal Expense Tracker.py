#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime


# In[2]:


class BudgetTracker:
    def __init__(self, filename='budget.csv'):
        self.filename = filename
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                self.transactions = list(reader)
        except FileNotFoundError:
            self.transactions = []

    def save_transactions(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.transactions)

    def add_transaction(self, amount, category, description=''):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append([date, amount, category, description])
        self.save_transactions()

    def get_balance(self):
        balance = 0.0
        for transaction in self.transactions:
            balance += float(transaction[1])
        return balance

    def get_transactions(self):
        return self.transactions


# In[5]:


class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Tracker")

        self.tracker = BudgetTracker()

        # Entry fields for amount, category, and description
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=1, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1, padx=10, pady=10)

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.grid(row=2, column=0, padx=10, pady=10)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=2, column=1, padx=10, pady=10)

        # Buttons to add transaction, view balance, and exit
        self.add_button = tk.Button(root, text="Add Transaction", command=self.add_transaction)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Transactions", command=self.view_transactions)
        self.view_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.balance_button = tk.Button(root, text="View Balance", command=self.view_balance)
        self.balance_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_transaction(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()

        if not amount or not category:
            messagebox.showwarning("Input Error", "Please fill in the amount and category fields.")
            return

        self.tracker.add_transaction(amount, category, description)
        messagebox.showinfo("Transaction Added", "Your transaction has been added successfully.")
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def view_transactions(self):
        transactions = self.tracker.get_transactions()
        transaction_window = tk.Toplevel(self.root)
        transaction_window.title("Transaction History")

        text = tk.Text(transaction_window, width=50, height=20)
        text.pack()

        for transaction in transactions:
            text.insert(tk.END, "\t".join(transaction) + "\n")

    def view_balance(self):
        balance = self.tracker.get_balance()
        messagebox.showinfo("Current Balance", f"Your current balance is: Rs.{balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()


# In[ ]:





# In[ ]:




