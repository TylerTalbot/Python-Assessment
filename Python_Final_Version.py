import tkinter as tk
import random
from tkinter import messagebox
from tkinter import ttk


root = tk.Tk()
root.geometry("600x600")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(3, weight=1)
root.title("Party Hire Shop")
root.configure(bg='lightblue')

PRICING = {
    #Furniture
    "Chairs": 2, "Tables": 5,
    #Tableware
    "Plates": 3, "Cups": 1, "Napkins": 1,
    #Cutlery
    "Forks": 1, "Knives": 1, "Spoons": 1,
    #Audio/Visual
    "Speakers": 10, "Projectors": 10, "Microphones": 10,
    #Entertainment
    "Bouncy Castles": 20, "Clowns": 15, "Magicians": 15
}

MAX_STOCK_FOR_EACH_PRODUCT_AVAILABLE = 500
Customer = []

#------------------------------------------------------------------------------------------------------------------------------------------------------

TitleLabel = tk.Label(root, text="Please enter your information: ", font=("sans-serif", 14, "bold"), bg="lightblue")
TitleLabel.grid(row=0, column=0, columnspan=4, pady=10)

#------------------------------------------------------------------------------------------------------------------------------------------------------

tk.Label(root, text="Name: ", fg="black", bg="lightblue", font=("sans-serif", 14, "bold")).grid(row=2, column=1, padx=10, pady=5)
NameEntry = tk.Entry(root, bg="white", width=15)
NameEntry.grid(row=3, column=1, padx=10, pady=5)
NameLabel = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="lightblue")
NameLabel.grid(row=10, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------

tk.Label(root, text="Last Name: ", fg="Black", bg="lightblue", font=("sans-serif", 14, "bold")).grid(row=2, column=2, padx=10, pady=5)
LastNameEntry = tk.Entry(root, bg="white", width=15)
LastNameEntry.grid(row=3, column=2, padx=10, pady=5)
LastNameLabel = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="lightblue")
LastNameLabel.grid(row=10, column=2, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------

tk.Label(root, text="Item Amount:", fg="black", bg="lightblue", font=("Sans serif", 14, "bold" )).grid(row=4, column=1, padx=10, pady=5)
ItemEntry = tk.Entry(root, bg="white", width=15)
ItemEntry.grid(row=5, column=1, padx=10, pady=5)
ItemLabel = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="lightblue")
ItemLabel.grid(row=11, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------

tk.Label(root, text="Select Item: ", fg="black", bg="lightblue", font=("sans-serif", 14, "bold")).grid(row=4, column=2, padx=10, pady=5)
ItemDropdown = ttk.Combobox(root, values=list(PRICING.keys()), state="readonly", width=15)
ItemDropdown.grid(row=5, column=2, padx=10, pady=5)
ItemDropdown.current(0) 

#------------------------------------------------------------------------------------------------------------------------------------------------------

def submission():
    FirstName = NameEntry.get().strip().title()
    LastName = LastNameEntry.get().strip().title()
    Item = ItemDropdown.get()
    Quantity = ItemEntry.get().strip()

    if not FirstName or not LastName or not Quantity:
        messagebox.showerror("Input Error", "All input boxes must be filled out")
        return
    
    if not Quantity.isdigit() or int(Quantity) <= 0 or int(Quantity) > MAX_STOCK_FOR_EACH_PRODUCT_AVAILABLE:
        messagebox.showerror("Input Error", "There is only a maximum of 500 items for each product")
        return
    
    recipte = random.randint(10000, 99999)
    Customer.append({"Recipte": recipte, "FirstName": FirstName, "LastName": LastName, "Item": Item, "Quantity": Quantity})
    TreeView.insert("", tk.END, values=(FirstName, LastName, Item, Quantity, recipte))

    NameEntry.delete(0, tk.END)
    LastNameEntry.delete(0, tk.END)
    ItemEntry.delete(0, tk.END)

#------------------------------------------------------------------------------------------------------------------------------------------------------

def DeletAnItem():
    selected=TreeView.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Pls Click a row in the table to delete an order")
        return
    for item in selected:
        remove = int(TreeView.item(item)['values'][4])

        global Customer 
        Customer = [c for c in Customer if c ["Recipte"] != remove]

        TreeView.delete(item)
    messagebox.showinfo("Deleted", "Item removed succesfully")

#------------------------------------------------------------------------------------------------------------------------------------------------------

def downloadRecipte():
    if not Customer:
        messagebox.showerror("Erro", "There are no active orders")
    Amount = TreeView.get_children()

    with open("recipte.txt", "w") as file:
        file.write("---Party Supplies Recipte---\n\n")
        for item in Amount:
            rows = TreeView.item(item)['values']

            FirstName = rows[0]
            LastName = rows[1]
            Item = rows[2]
            Qnty = int(rows[3])
            recipte = rows[4]

            file.write("-------------------------------------\n")
            file.write(f"You have bought {Item}\n")
            file.write(f"Your name is {FirstName} {LastName}\n")
            file.write(f"The quanity of {Item} you bought is {Qnty}\n")
            file.write(f"Your recipt number is {recipte}\n")
            file.write("-------------------------------------\n")
    messagebox.showinfo("Saved", "Your recipte was saved succesfully")

#------------------------------------------------------------------------------------------------------------------------------------------------------

TreeView = ttk.Treeview(root, column=("First Name", "Last Name", "Item", "Quantity", "recipte"), show="headings", height=6)
for col, text in [("First Name", "FirstName"), ("Last Name", "LastName"), ("Item", "Item"), ("Quantity", "Quantity"), ("recipte", "recipte")]:
    TreeView.heading(col, text=text)
    TreeView.column(col, width=90, anchor="center")
TreeView.grid(row=6, column=1, columnspan=2, pady=20, sticky="")

#------------------------------------------------------------------------------------------------------------------------------------------------------

Submit = tk.Button(root, text="Submit Order", bg="white", font=("sans-serif", 12, "bold"), command=submission)
Submit.grid(row=7, column=1, columnspan=2, pady=15)
Receipt = tk.Button(root, text="Download Receipt", bg="white", font=("sans-serif", 12, "bold"), command=downloadRecipte)
Receipt.grid(row=8, column=1, columnspan=2, pady=5)
Delete = tk.Button(root, text="Delete an Item", bg="white", font=("sans-serif", 12, "bold"), command=DeletAnItem)
Delete.grid(row=9, column=1, columnspan=2, pady=5)

#------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
