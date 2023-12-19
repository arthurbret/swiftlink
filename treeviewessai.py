import customtkinter as ctk

fenetre=ctk.CTk()

tabview = ctk.CTkTabview(master=fenetre)
tabview.pack(padx=20, pady=20)

tabview.add("Contacts")  # add tab at the end
tabview.add("Rechercher")  # add tab at the end
tabview.set("Rechercher")  # set currently visible tab

button = ctk.CTkButton(master=tabview.tab("Contacts"))
button.pack(padx=20, pady=20)

fenetre.mainloop()