import tkinter as tk
import tkinter.ttk as ttk
from SQLite_func import create_contact

def reset_frame():
    for widget in fenetre.winfo_children():
        widget.destroy()

def ajouter_contact():
    reset_frame()

    # Create labels and entry fields for each contact attribute
    label_nom = ttk.Label(fenetre, text="Nom:")
    label_nom.pack()
    entry_nom = ttk.Entry(fenetre)
    entry_nom.pack()

    label_prenom = ttk.Label(fenetre, text="Prénom:")
    label_prenom.pack()
    entry_prenom = ttk.Entry(fenetre)
    entry_prenom.pack()

    label_email = ttk.Label(fenetre, text="Email:")
    label_email.pack()
    entry_email = ttk.Entry(fenetre)
    entry_email.pack()

    label_tel = ttk.Label(fenetre, text="Téléphone:")
    label_tel.pack()
    entry_tel = ttk.Entry(fenetre)
    entry_tel.pack()

    label_photo = ttk.Label(fenetre, text="Photo de profil (lien):")
    label_photo.pack()
    entry_photo = ttk.Entry(fenetre)
    entry_photo.pack()

    # Function to handle the submit button click
    def submit_contact():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        email = entry_email.get()
        tel = entry_tel.get()
        photo = entry_photo.get()

        create_contact(prenom, nom, email, tel, photo)

        # Close the add contact window
        affichage_base()

    # Create a submit button
    submit_button = ttk.Button(fenetre, text="Submit", command=submit_contact)
    submit_button.pack()


def modifier_contact():
    # Logique pour modifier un contact
    pass

def supprimer_contact():
    # Logique pour supprimer un contact
    pass

def rechercher_contact():
    # Logique pour rechercher un contact
    pass

# Création de la fenêtre principale
fenetre = tk.Tk()

def affichage_base():
    reset_frame()
    # Création des boutons
    bouton_ajouter = ttk.Button(fenetre, text="Ajouter un contact", command=ajouter_contact)
    bouton_modifier = ttk.Button(fenetre, text="Modifier un contact", command=modifier_contact)
    bouton_supprimer = ttk.Button(fenetre, text="Supprimer un contact", command=supprimer_contact)
    bouton_rechercher = ttk.Button(fenetre, text="Rechercher un contact", command=rechercher_contact)

    # Placement des boutons dans la fenêtre
    bouton_ajouter.pack()
    bouton_modifier.pack()
    bouton_supprimer.pack()
    bouton_rechercher.pack()

    # Boucle principale de la fenêtre
    fenetre.mainloop()

affichage_base()