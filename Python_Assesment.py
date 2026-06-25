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
# This is my space for all of my lists and constants

PRICING = [
    #Furniture
    {"Chairs": 2.00, "Tables": 5.00},
    #Tableware
    {"Plates": 3.00, "Cups": 1.00, "Napkins": 1.00},
    #Cutlery
    {"Forks": 1.00, "Knives": 1.00, "Spoons": 1.00},
    #Audio/Visual
    {"Speakers": 10.00, "Projectors": 10.00, "Microphones": 10.00},
    #Entertainment
    {"Bouncy Castles": 20.00, "Clowns": 15.00, "Magicians": 15.00}
]

MAX_STOCK_FOR_EACH_PRODUCT_AVAILABLE = 500
Customer = []

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is my name input for the program

title_label = tk.Label(root, text="Please enter your information:", font=("sans-serif", 14, "bold"), bg="grey")
title_label.grid(row=0, column=0, columnspan=4, pady=10)
tk.Label(root, text="Name: ", fg="black", bg="grey", font=("sans-serif", 14, "bold")).grid(row=2, column=1, padx=10, pady=5)
name_entry = tk.Entry(root, bg="darkgrey", width=15)
name_entry.grid(row=3, column=1, padx=10, pady=5)
name_label = tk.Label(root, text="", fg="Blue", font=("sans-serif", 12), bg="grey")
name_label.grid(row=10, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------
