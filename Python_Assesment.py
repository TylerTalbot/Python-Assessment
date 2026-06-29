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

TitleLabel = tk.Label(root, text="Please enter your information: ", font=("sans-serif", 14, "bold"), bg="grey")
TitleLabel.grid(row=0, column=0, columnspan=4, pady=10)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is a title describing the product amounts for eah product, its not much but its important information to the user

TitleLabel = tk.Label(root, text="There are 500 items for each product", font=("sans-serif", 14, "bold"), bg="grey")
TitleLabel.grid(row=1, column=0, columnspan=4, pady=10)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# First Name

tk.Label(root, text="Name: ", fg="black", bg="grey", font=("sans-serif", 14, "bold")).grid(row=2, column=1, padx=10, pady=5)
NameEntry = tk.Entry(root, bg="darkgrey", width=15)
NameEntry.grid(row=3, column=1, padx=10, pady=5)
NameLabel = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="grey")
NameLabel.grid(row=10, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the input for the user to input their last Name
# I did this so the information provided could be more accurate

tk.Label(root, text="Last Name: ", fg="black", bg="grey", font=("sans-serif", 14, "bold")).grid(row=2, column=2, padx=10, pady=5)
LastNameEntry = tk.Entry(root, bg="darkgrey", width=15)
LastNameEntry.grid(row=3, column=2, padx=10, pady=5)
LastNameLabel = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="grey")
LastNameLabel.grid(row=10, column=2, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is my input for the user to input how much of an item they want

amount_label = tk.Label(root, text="Item Amount:", fg="black", bg="grey", font=("Sans serif", 14, "bold" )).grid(row=4, column=1, padx=10, pady=5)
ItemEntry = tk.Entry(root, bg="darkgrey", width=15)
ItemEntry.grid(row=5, column=1, padx=10, pady=5)
ItemLabel = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="grey")
ItemLabel.grid(row=11, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# this is my drop down menu for the user to select what products they want to purchace
# When coding this part I acidendtly forgot to esnure there was a state: readoly, because it makes it so no one could type anything on the drop down menu

tk.Label(root, text="Select Item: ", fg="black", bg="grey", font=("sans-serif", 14, "bold")).grid(row=4, column=2, padx=10, pady=5)
ItemDropdown = ttk.Combobox(root, values=list(PRICING.keys()), state="readonly", width=15)
ItemDropdown.grid(row=5, column=2, padx=10, pady=5)
ItemDropdown.current(0) 

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the part of my code that handles the user's entries and downloads it as a txt file!

def Submit():
    Name = NameEntry.get()
    LastName = LastNameEntry.get()
    Dropdown = ItemDropdown.get()
    Quantity = ItemEntry.get()
    with open("receipt.txt") as file:
        file.write(".....RECEIPT..... \n")
        file.write(f"Customer Name: {Name} {LastName}\n")
        file.write(f"Item Selected: {Dropdown}\n")
        file.write(f"Item Quantity: {Quantity}\n")

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the code for the submit button, and the download the reciptt button

Submit = tk.Button(root, text="Submit Order", bg="darkgrey", font=("sans-serif", 12, "bold"), command=Submit)
Submit.grid(row=6, column=1, columnspan=2, pady=15)
Receipt = tk.Button(root, text="Download Receipt", bg="darkgrey", font=("sans-serif", 12, "bold"))
Receipt.grid(row=7, column=1, columnspan=2, pady=5)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# this is the end of the code, where I place my root.mainloop to conclude the code!

root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------
