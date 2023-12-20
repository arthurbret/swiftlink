import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from SQLite_func import create_contact
from SQLite_func import delete_contact
from SQLite_func import update_contact
from SQLite_func import search_contact
from SQLite_func import get_all_contacts

ctk.set_default_color_theme("dark-blue")


def change_tab_action():
    tabview.set("Actions")

def state_modif(label, text, color):
    label.configure(text=text, text_color=color)

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

    if "@" not in email:
        state_modif(state_notif,"email incorrect","red")
        email_var.set("")
    else:
        for char in tel:
            if char.isalpha():
                state_modif(state_notif,"numero de telephone incorrect", "red")
                telephone_var.set("")
            else:
                clear_fields()
                create_contact(prenom, nom, email, tel, photo)
                update_contacts_list()
                state_modif(state_notif,"Contact ajoute","green")

def supprimer_contact():
    selected_item = tree.selection()
    if selected_item:
        contact_id = tree.item(selected_item)['values'][0]
        print(contact_id)
        delete_contact(contact_id)
        update_contacts_list()
        state_modif(state_notif2,"contact supprime","green")

def modifier_contact():
    selected_item = tree.selection()
    if selected_item:
        contact_id = tree.item(selected_item)['values'][0]
        prenom = prenom_var.get() if prenom_var.get() else tree.item(selected_item)['values'][1]
        nom = nom_var.get() if nom_var.get() else tree.item(selected_item)['values'][2]
        email = email_var.get() if email_var.get() else tree.item(selected_item)['values'][3]
        tel = telephone_var.get() if telephone_var.get() else tree.item(selected_item)['values'][4]
        photo = photo_var.get() if photo_var.get() else tree.item(selected_item)['values'][5]
        # Update the contact in the database
    update_contact(contact_id, prenom, nom, email, tel, photo)
    update_contacts_list()
    clear_fields()
    state_modif(state_notif,"Contact modifié","green")

def rechercher_contact():
    nom = nom_var.get()
    prenom = prenom_var.get()
    email = email_var.get()
    tel = telephone_var.get()
    recherche = search_contact(prenom, nom, email, tel)
    print("Recherche en cours...")
    if recherche:
        print(recherche)            
        tabview.set("Résultats")  # Configuration de l'onglet "Résultats" comme onglet actif
        tree_results = ttk.Treeview(columns=("ID","Prénom", "Nom", "Email", "Téléphone", "Photo"), show="headings", height=10, master=tabview.tab("Résultats") )
        tree_results.heading("ID", text="ID")
        tree_results.heading("Prénom", text="Prénom")
        tree_results.heading("Nom", text="Nom")
        tree_results.heading("Email", text="Email")
        tree_results.heading("Téléphone", text="Téléphone")
        tree_results.heading("Photo", text="Photo")
        tree_results.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tree_results.column("ID", width=15)
        for contact in recherche:
            tree_results.insert('', 'end', values=(contact[0],contact[1], contact[2], contact[3], contact[4], contact[5]))
    else:
        state_modif(state_notif,"Aucun résultat","red")
    clear_fields()
        
def browse_photo():
    selected_item = tree.selection()
    if selected_item:
        tabview.set("Photo")  # Configuration de l'onglet "Photo" comme onglet actif
        url = tree.item(selected_item)['values'][5]
        print(url)

        # Récupérer l'image depuis l'URL
        reponse = requests.get(url)
        img_data = reponse.content
        img = Image.open(BytesIO(img_data))

        # Convertir l'image en format tkinter
        tk_img = ImageTk.PhotoImage(img)

        # Afficher l'image dans le label
        label.config(image=tk_img)
        label.image = tk_img
        label.pack()

# Création de la fenêtre
fenetre = ctk.CTk(fg_color="#6F8FAF")
fenetre.title("Swiftlink") # Titre de la fenêtre
fenetre.iconbitmap("logo.ico") # Logo de la fenêtre

# Création du tabview et des onglets
tabview = ctk.CTkTabview(master=fenetre)
tabview.pack(padx=20, pady=20)
tabview.add("Contacts")  # Ajout d'un onglet "Contacts"
tabview.add("Actions")  # Ajout d'un onglet "Actions"
tabview.add("Résultats")  # Ajout d'un onglet "Résultats"
tabview.add("Photo")  # Ajout d'un onglet "Photo"
tabview.set("Contacts")  # Configuration de l'onglet "Contacts" comme onglet actif

# Création des widgets champs de saisie
nom_var = ctk.StringVar()
prenom_var = ctk.StringVar()
email_var = ctk.StringVar()
telephone_var = ctk.StringVar()
photo_var = ctk.StringVar()

# Création du treeview
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
ctk.CTkButton(contacts_button_frame, text="Modifier", command=change_tab_action).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
ctk.CTkButton(contacts_button_frame, text="Voir photo", command=browse_photo).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

label = tk.Label(tabview.tab("Photo"))

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

fields_frame = ctk.CTkFrame(master=tabview.tab("Actions"))
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

# Buttons
button_frame = ctk.CTkFrame(fields_frame)
button_frame.grid(row=5, columnspan=3, pady=5, sticky="nsew")

ctk.CTkButton(button_frame, text="Ajouter", command=ajouter_contact).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
ctk.CTkButton(button_frame, text="Modifier", command=modifier_contact).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
ctk.CTkButton(button_frame, text="Rechercher", command=rechercher_contact).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

state_notif= ctk.CTkLabel(tabview.tab("Actions"), text="", justify="center", anchor="center")
state_notif.grid(row=1, column=1)
state_notif2= ctk.CTkLabel(tabview.tab("Contacts"), text="", justify="center", anchor="center")
state_notif2.grid(row=2,column=0)

fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.rowconfigure(0, weight=1)



fenetre.mainloop()