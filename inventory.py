import tkinter as tk
from tkinter import messagebox

inventory = {}

def add_item():
    item, qty = entry_item.get().strip(), entry_qty.get().strip()
    if not item or not qty.isdigit():
        return messagebox.showerror("Error", "Enter valid item and quantity")
    inventory[item] = inventory.get(item, 0) + int(qty)
    messagebox.showinfo("Added", f"{item}: {inventory[item]}")
    entry_item.delete(0, tk.END); entry_qty.delete(0, tk.END)

def retrieve_item():
    item = entry_item.get().strip()
    messagebox.showinfo("Info", f"{item}: {inventory.get(item,'Not found')}")
    entry_item.delete(0, tk.END)

def show_total():
    messagebox.showinfo("Total", f"{sum(inventory.values())}")

root = tk.Tk(); root.title("Inventory")

tk.Label(root, text="Item:").pack()
entry_item = tk.Entry(root, width=20); entry_item.pack()

tk.Label(root, text="Quantity:").pack()
entry_qty = tk.Entry(root, width=20); entry_qty.pack()

tk.Button(root, text="Add/Update", command=add_item).pack(pady=3)
tk.Button(root, text="Retrieve", command=retrieve_item).pack(pady=3)
tk.Button(root, text="Show Total", command=show_total).pack(pady=3)
tk.Button(root, text="Exit", command=root.quit).pack(pady=3)

root.mainloop()
