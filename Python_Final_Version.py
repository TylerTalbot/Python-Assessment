import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")
root.grid_columnconfigure(2, weight=1)
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

TitleLabel = tk.Label(root, text="There are 500 items for each product", font=("sans-serif", 14, "bold"), bg="lightblue")
TitleLabel.grid(row=1, column=0, columnspan=4, pady=10)

#------------------------------------------------------------------------------------------------------------------------------------------------------

tk.Label(root, text="Name: ", fg="black", bg="lightblue", font=("sans-serif", 14, "bold")).grid(row=2, column=1, padx=10, pady=5)
NameEntry = tk.Entry(root, bg="white", width=15)
NameEntry.grid(row=3, column=1, padx=10, pady=5)
NameLabel = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="lightblue")
NameLabel.grid(row=10, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------

amount_label = tk.Label(root, text="Item Amount:", fg="black", bg="lightblue", font=("Sans serif", 14, "bold" )).grid(row=4, column=1, padx=10, pady=5)
ItemEntry = tk.Entry(root, bg="white", width=15)
ItemEntry.grid(row=5, column=1, padx=10, pady=5)
ItemLabel = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="lightblue")
ItemLabel.grid(row=11, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------

tk.Label(root, text="Last Name: ", fg="Black", bg="lightblue", font=("sans-serif", 14, "bold")).grid(row=2, column=2, padx=10, pady=5)
LastNameEntry = tk.Entry(root, bg="white", width=15)
LastNameEntry.grid(row=3, column=2, padx=10, pady=5)
LastNameLabel = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="lightblue")
LastNameLabel.grid(row=10, column=2, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------

tk.Label(root, text="Select Item: ", fg="black", bg="lightblue", font=("sans-serif", 14, "bold")).grid(row=4, column=2, padx=10, pady=5)
ItemDropdown = ttk.Combobox(root, values=list(PRICING.keys()), state="readonly", width=15)
ItemDropdown.grid(row=5, column=2, padx=10, pady=5)
ItemDropdown.current(0) 

#------------------------------------------------------------------------------------------------------------------------------------------------------

def Submit():
    Name = NameEntry.get()
    LastName = LastNameEntry.get()
    Dropdown = ItemDropdown.get()
    Quantity = ItemEntry.get()
    with open("receipt.txt", "w") as file:
        file.write(".....RECEIPT..... \n")
        file.write(f"Customer Name: {Name} {LastName}\n")
        file.write(f"Item Selected: {Dropdown}\n")
        file.write(f"Item Quantity: {Quantity}\n")

#------------------------------------------------------------------------------------------------------------------------------------------------------

Submit = tk.Button(root, text="Submit Order", bg="white", font=("sans-serif", 12, "bold"), command=Submit)
Submit.grid(row=6, column=1, columnspan=2, pady=15)
Receipt = tk.Button(root, text="Download Receipt", bg="white", font=("sans-serif", 12, "bold"))
Receipt.grid(row=7, column=1, columnspan=2, pady=5)

#------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
