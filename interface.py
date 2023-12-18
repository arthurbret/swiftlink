import tkinter as tk
import tkinter.ttk as ttk

def ajouter_contact():
    # Logique pour ajouter un contact
    pass

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
