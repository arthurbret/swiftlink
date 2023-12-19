import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from SQLite_func import create_contact
from SQLite_func import delete_contact
from SQLite_func import update_contact
from SQLite_func import search_contact
from SQLite_func import get_all_contacts

ctk.set_default_color_theme("dark-blue")


def change_tab_Rechercher():
    tabview.set("Rechercher")

def clear_fields():
    prenom_var.set("")
    nom_var.set("")
    email_var.set("")
    telephone_var.set("")
    photo_var.set("")
    print("Clearing fields")

def ajouter_contact():
    nom = nom_var.get()
    prenom = prenom_var.get()
    email = email_var.get()
    tel = telephone_var.get()
    photo = photo_var.get()
    clear_fields()

    create_contact(prenom, nom, email, tel, photo)
    update_contacts_list()

def supprimer_contact():
    selected_item = tree.selection()
    if selected_item:
        contact_id = tree.item(selected_item)['values'][0]
        print(contact_id)
        delete_contact(contact_id)
        update_contacts_list()

def modifier_contact():
    selected_item = tree.selection()
    if selected_item:
        contact_id = tree.item(selected_item)['values'][0]
        prenom = prenom_var.get() if prenom_var.get() else tree.item(selected_item)['values'][1]
        nom = nom_var.get() if nom_var.get() else tree.item(selected_item)['values'][2]
        email = email_var.get() if email_var.get() else tree.item(selected_item)['values'][3]
        tel = telephone_var.get() if telephone_var.get() else tree.item(selected_item)['values'][4]
        photo = photo_var.get() if photo_var.get() else tree.item(selected_item)['values'][5]
        print("Prenom:{} Nom:{}" .format(prenom_var.get(), nom_var.get()))
        print("Prenom:{} Nom:{}" .format(tree.item(selected_item)['values'][1], tree.item(selected_item)['values'][2]))
        # Update the contact in the database
        update_contact(contact_id, prenom, nom, email, tel, photo)
        update_contacts_list()   
        clear_fields()

def rechercher_contact():
    nom = nom_var.get()
    prenom = prenom_var.get()
    email = email_var.get()
    tel = telephone_var.get()
    recherche = search_contact(prenom, nom, email, tel)
    print("oui")

    if recherche:
        print(recherche)

def browse_photo():
    pass

fenetre = ctk.CTk(fg_color="#6F8FAF")
fenetre.title("Swiftlink") # Titre de la fenêtre
fenetre.iconbitmap("logo.ico") # Logo de la fenêtre


tabview = ctk.CTkTabview(master=fenetre)
tabview.pack(padx=20, pady=20)

tabview.add("Contacts")  # add tab at the end
tabview.add("Rechercher")  # add tab at the end
tabview.set("Contacts")  # set currently visible tab


nom_var = ctk.StringVar()
prenom_var = ctk.StringVar()
email_var = ctk.StringVar()
telephone_var = ctk.StringVar()
photo_var = ctk.StringVar()


tree = ttk.Treeview(columns=("ID","Prénom", "Nom", "Email", "Téléphone", "Photo"), show="headings", height=10, master=tabview.tab("Contacts") )
tree.heading("ID", text="ID")
tree.heading("Prénom", text="Prénom")
tree.heading("Nom", text="Nom")
tree.heading("Email", text="Email")
tree.heading("Téléphone", text="Téléphone")
tree.heading("Photo", text="Photo")
tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

tree.column("ID", width=15)

contacts_button_frame = ctk.CTkFrame(master=tabview.tab("Contacts"))
contacts_button_frame.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")

ctk.CTkButton(contacts_button_frame, text="Supprimer", command=supprimer_contact).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
ctk.CTkButton(contacts_button_frame, text="Modifier", command=change_tab_Rechercher).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

def update_contacts_list():
    # Clear the old contacts from the treeview
    for i in tree.get_children():
        tree.delete(i)

    # Get all the contacts from the database
    contacts = get_all_contacts()

    # Add each contact to the treeview
    for contact in contacts:
        tree.insert('', 'end', values=(contact[0],contact[1], contact[2], contact[3], contact[4], contact[5]))
update_contacts_list()

fields_frame = ctk.CTkFrame(master=tabview.tab("Rechercher"))
fields_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

ctk.CTkLabel(fields_frame, text="Nom:").grid(row=0, column=0, sticky="e")
ctk.CTkEntry(fields_frame, textvariable=nom_var).grid(row=0, column=1, padx=5, pady=5, sticky="w")

ctk.CTkLabel(fields_frame, text="Prénom:").grid(row=1, column=0, sticky="e")
ctk.CTkEntry(fields_frame, textvariable=prenom_var).grid(row=1, column=1, padx=5, pady=5, sticky="w")

ctk.CTkLabel(fields_frame, text="Email:").grid(row=2, column=0, sticky="e")
ctk.CTkEntry(fields_frame, textvariable=email_var).grid(row=2, column=1, padx=5, pady=5, sticky="w")

ctk.CTkLabel(fields_frame, text="Téléphone:").grid(row=3, column=0, sticky="e")
ctk.CTkEntry(fields_frame, textvariable=telephone_var).grid(row=3, column=1, padx=5, pady=5, sticky="w")

ctk.CTkLabel(fields_frame, text="Photo:").grid(row=4, column=0, sticky="e")
ctk.CTkEntry(fields_frame, textvariable=photo_var).grid(row=4, column=1, padx=5, pady=5, sticky="w")
ctk.CTkButton(fields_frame, text="Parcourir", command=browse_photo).grid(row=4, column=2, sticky="w")

# Buttons
button_frame = ctk.CTkFrame(fields_frame)
button_frame.grid(row=5, columnspan=3, pady=5, sticky="nsew")

ctk.CTkButton(button_frame, text="Ajouter", command=ajouter_contact).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
ctk.CTkButton(button_frame, text="Modifier", command=modifier_contact).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
ctk.CTkButton(button_frame, text="Rechercher", command=rechercher_contact).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.rowconfigure(0, weight=1)

tabview.set("Contacts")  # set currently visible tab

fenetre.mainloop()