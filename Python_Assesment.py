#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is place for all my imports

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#------------------------------------------------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.geometry("400x400")
root.grid_columnconfigure(2, weight=1)
root.title("Party Hire Shop")
root.configure(bg='grey')
customers = []

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is my space for all of my lists, constants, and dictionaries
# I have categorized each of the products into dictionaries for a more organized approach

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
# This is my name input for the program

title_label = tk.Label(root, text="Please enter your information:", font=("sans-serif", 14, "bold"), bg="grey")
title_label.grid(row=0, column=0, columnspan=4, pady=10)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is a title describing the product amounts for eah product, its not much but its important information to the user

title_label = tk.Label(root, text="There are 500 items for each product", font=("sans-serif", 14, "bold"), bg="grey")
title_label.grid(row=1, column=0, columnspan=4, pady=10)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# First Name

tk.Label(root, text="Name: ", fg="black", bg="grey", font=("sans-serif", 14, "bold")).grid(row=2, column=1, padx=10, pady=5)
name_entry = tk.Entry(root, bg="darkgrey", width=15)
name_entry.grid(row=3, column=1, padx=10, pady=5)
name_label = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="grey")
name_label.grid(row=10, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------

tk.Label(root, text="Last Name: ", fg="black", bg="grey", font=("sans-serif", 14, "bold")).grid(row=2, column=2, padx=10, pady=5)
LastName_entry = tk.Entry(root, bg="darkgrey", width=15)
LastName_entry.grid(row=3, column=2, padx=10, pady=5)
LastName_label = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="grey")
LastName_label.grid(row=10, column=2, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is my input for the user to input how much of an item they want

amount_label = tk.Label(root, text="Item Amount:", fg="black", bg="grey", font=("Sans serif", 14, "bold" )).grid(row=4, column=1, padx=10, pady=5)
item_entry = tk.Entry(root, bg="darkgrey", width=15)
item_entry.grid(row=5, column=1, padx=10, pady=5)
item_label = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="grey")
item_label.grid(row=10, column=2, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------

tk.Label(root, text="Select Item: ", fg="black", bg="grey", font=("sans-serif", 14, "bold")).grid(row=4, column=2, padx=10, pady=5)
item_dropdown = ttk.Combobox(root, values=list(PRICING.keys()), width=15)
item_dropdown.grid(row=5, column=2, padx=10, pady=5)
item_dropdown.current(0) 

#------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------
