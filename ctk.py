import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from SQLite_func import create_contact
from SQLite_func import get_all_contacts

ctk.set_default_color_theme("dark-blue")

def ajouter_contact():
    nom = nom_var.get()
    prenom = prenom_var.get()
    email = email_var.get()
    tel = telephone_var.get()
    photo = photo_var.get()

    create_contact(prenom, nom, email, tel, photo)
    update_contacts_list()

def supprimer_contact():
    pass

def modifier_contact():
    pass

def rechercher_contact():
    pass

def clear_fields():
    pass

def browse_photo():
    pass

fenetre = ctk.CTk(fg_color="#6F8FAF")
fenetre.title("Swiftlink") # Titre de la fenêtre
fenetre.iconbitmap("logo.ico") # Logo de la fenêtre


nom_var = ctk.StringVar()
prenom_var = ctk.StringVar()
email_var = ctk.StringVar()
telephone_var = ctk.StringVar()
photo_var = ctk.StringVar()

tree = ttk.Treeview(fenetre, columns=("Nom", "Prénom", "Email", "Téléphone", "Photo"), show="headings", height=10, )
tree.heading("Nom", text="Nom")
tree.heading("Prénom", text="Prénom")
tree.heading("Email", text="Email")
tree.heading("Téléphone", text="Téléphone")
tree.heading("Photo", text="Photo")
tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

def update_contacts_list():
    # Clear the old contacts from the treeview
    for i in tree.get_children():
        tree.delete(i)

    # Get all the contacts from the database
    contacts = get_all_contacts()

    # Add each contact to the treeview
    for contact in contacts:
        tree.insert('', 'end', values=(contact[1], contact[2], contact[3], contact[4], contact[5]))
update_contacts_list()

fields_frame = ctk.CTkFrame(fenetre)#, bg_color="#40E0D0")
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
#button_frame.configure(bg_color="blue")
button_frame.grid(row=5, columnspan=3, pady=5, sticky="nsew")

ctk.CTkButton(button_frame, text="Ajouter", command=ajouter_contact).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
ctk.CTkButton(button_frame, text="Supprimer", command=supprimer_contact).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
ctk.CTkButton(button_frame, text="Modifier", command=modifier_contact).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
ctk.CTkButton(button_frame, text="Rechercher", command=rechercher_contact).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.rowconfigure(0, weight=1)

fenetre.mainloop()