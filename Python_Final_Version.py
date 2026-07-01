#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the part of my code for the imports
import tkinter as tk
import random
from tkinter import messagebox
from tkinter import ttk

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the part of my code for th geometry and the centering of the GUI, including the color of the GUI, and the header of the GUI
root = tk.Tk()
root.geometry("600x600")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(3, weight=1)
root.title("Party Hire Shop")
root.configure(bg='lightblue')

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the part of my code for the dictionaries, lists, and constants
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
# This is a title for the GUI, requesting that the user inpu their information for their purchace
Title_Label = tk.Label(root, text="Please enter your information: ", font=("sans-serif", 14, "bold"), bg="lightblue")
Title_Label.grid(row=0, column=0, columnspan=4, pady=10)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the input for the user to type their Name for the order
tk.Label(root, text="Name: ", fg="black", bg="lightblue", font=("sans-serif", 14, "bold")).grid(row=2, column=1, padx=10, pady=5)
Name_Entry = tk.Entry(root, bg="white", width=15)
Name_Entry.grid(row=3, column=1, padx=10, pady=5)
Name_Label = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="lightblue")
Name_Label.grid(row=10, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the input for the user to input their last name, while not nessesary it is valid for their full name
tk.Label(root, text="Last Name: ", fg="Black", bg="lightblue", font=("sans-serif", 14, "bold")).grid(row=2, column=2, padx=10, pady=5)
Last_Name_Entry = tk.Entry(root, bg="white", width=15)
Last_Name_Entry.grid(row=3, column=2, padx=10, pady=5)
Last_Name_Label = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="lightblue")
Last_Name_Label.grid(row=10, column=2, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the input for the user to select how much of the select Item they would like, as long it is in the range of 1 to 500
tk.Label(root, text="Item Amount:", fg="black", bg="lightblue", font=("Sans serif", 14, "bold" )).grid(row=4, column=1, padx=10, pady=5)
Item_Entry = tk.Entry(root, bg="white", width=15)
Item_Entry.grid(row=5, column=1, padx=10, pady=5)
Item_Label = tk.Label(root, text="", fg="grey", font=("sans-serif", 12), bg="lightblue")
Item_Label.grid(row=11, column=1, padx=10, pady=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the input in the form of a dropdown menu for the user to seolect which item that would like to purchace
tk.Label(root, text="Select Item: ", fg="black", bg="lightblue", font=("sans-serif", 14, "bold")).grid(row=4, column=2, padx=10, pady=5)
Item_Dropdown = ttk.Combobox(root, values=list(PRICING.keys()), state="readonly", width=15)
Item_Dropdown.grid(row=5, column=2, padx=10, pady=5)
Item_Dropdown.current(0) 

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the part of my code that validates the users input, and transfers the users input into the treeview
def submission():
    First_Name = Name_Entry.get().strip().title()
    Last_Name = Last_Name_Entry.get().strip().title()
    Item = Item_Dropdown.get()
    Quantity = Item_Entry.get().strip()

    if not First_Name or not Last_Name or not Quantity:
        messagebox.showerror("Input Error", "All input boxes must be filled out")
        return
    
    if not Quantity.isdigit() or int(Quantity) <= 0 or int(Quantity) > MAX_STOCK_FOR_EACH_PRODUCT_AVAILABLE:
        messagebox.showerror("Input Error", "There is only a maximum of 500 items for each product")
        return
    
    recipte = random.randint(10000, 99999)
    Customer.append({"Recipte": recipte, "FirstName": First_Name, "LastName": Last_Name, "Item": Item, "Quantity": Quantity})
    Tree_View.insert("", tk.END, values=(First_Name, Last_Name, Item, Quantity, recipte))

    Name_Entry.delete(0, tk.END)
    Last_Name_Entry.delete(0, tk.END)
    Item_Entry.delete(0, tk.END)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the part of my code that will delete and order for a user if they click on it via the treeview, then click the delete button it will delete that order
def Delet_An_Item():
    selected=Tree_View.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Pls Click a row in the table to delete an order")
        return
    for item in selected:
        remove = int(Tree_View.item(item)['values'][4])

        global Customer 
        Customer = [c for c in Customer if c ["Recipte"] != remove]

        Tree_View.delete(item)
    messagebox.showinfo("Deleted", "Item removed succesfully")
    return

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the part of my code that downloads the users inputs in the form of a txt file
def download_Recipte():
    if not Customer:
        messagebox.showerror("Erro", "There are no active orders")
        return
    Amount = Tree_View.get_children()

    with open("recipte.txt", "w") as file:
        file.write("---Party Supplies Recipte---\n\n")
        for item in Amount:
            rows = Tree_View.item(item)['values']

            First_Name = rows[0]
            Last_Name = rows[1]
            Item = rows[2]
            Qnty = int(rows[3])
            recipte = rows[4]

            file.write("-------------------------------------\n")
            file.write(f"You have bought {Item}\n")
            file.write(f"Your name is {First_Name} {Last_Name}\n")
            file.write(f"The quanity of {Item} you bought is {Qnty}\n")
            file.write(f"Your recipt number is {recipte}\n")
            file.write("-------------------------------------\n")
    messagebox.showinfo("Saved", "Your recipte was saved succesfully")
    return

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the treeview where, when the code is running it displays the users inputs
Tree_View = ttk.Treeview(root, column=("First_Name", "Last_Name", "Item", "Quantity", "recipte"), show="headings", height=6)
for col, text in [("First_Name", "First_Name"), ("Last_Name", "Last_Name"), ("Item", "Item"), ("Quantity", "Quantity"), ("recipte", "recipte")]:
    Tree_View.heading(col, text=text)
    Tree_View.column(col, width=90, anchor="center")
Tree_View.grid(row=6, column=1, columnspan=2, pady=20, sticky="")

#------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the code for my buttons on my GUI, their function use and aesthetics, and geometry. This is where the Button is designed and the commanded code is its purpose
Submit = tk.Button(root, text="Submit Order", bg="white", font=("sans-serif", 12, "bold"), command=submission)
Submit.grid(row=7, column=1, columnspan=2, pady=15)
Receipt = tk.Button(root, text="Download Receipt", bg="white", font=("sans-serif", 12, "bold"), command=download_Recipte)
Receipt.grid(row=8, column=1, columnspan=2, pady=5)
Delete = tk.Button(root, text="Delete an Item", bg="white", font=("sans-serif", 12, "bold"), command=Delet_An_Item)
Delete.grid(row=9, column=1, columnspan=2, pady=5)

#------------------------------------------------------------------------------------------------------------------------------------------------------
# This is the end of my code, It is ended with a root.mainloop()
root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------