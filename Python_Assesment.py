import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x600")
root.title("Party Hire Shop")
root.configure(bg='grey')

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

MAX_STOCK_FOR_EACH_PRODUCT_AVAILABLE = 100
Customer = []

def submit_data():
        if len(Customer) >= MAX_STOCK_FOR_EACH_PRODUCT_AVAILABLE:
            return messagebox.showerror("Sorry we are completely sold out of this product!")