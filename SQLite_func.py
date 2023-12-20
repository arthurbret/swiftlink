# Initialisation de la base de données sqlite3
import sqlite3
connection = sqlite3.connect('swiftlinkdb.db')
print(connection.total_changes)
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, prenom TEXT, nom TEXT, email TEXT UNIQUE, tel TEXT UNIQUE, profilepic TEXT)')

# Fonction création d'un contact
def create_contact(prenom, nom, email, tel, profilepic):
    cursor.execute('INSERT INTO contacts (prenom, nom, email, tel, profilepic) VALUES (?, ?, ?, ?, ?)', (prenom, nom, email, tel, profilepic))
    connection.commit()

# Fonction suppression d'un contact
def delete_contact(id):
    cursor.execute('DELETE FROM contacts WHERE id = ?', (id,))
    connection.commit()

# Fonction modification d'un contact
def update_contact(id, prenom, nom, email, tel, profilepic):
    cursor.execute('UPDATE contacts SET prenom = ?, nom = ?, email = ?, tel = ?, profilepic = ? WHERE id = ?', (prenom, nom, email, tel, profilepic, id))
    connection.commit()

# Fonction recherche d'un contact
def search_contact(prenom=None, nom=None, email=None, tel=None):
    query = 'SELECT * FROM contacts WHERE'
    conditions = []
    values = []

    if prenom:
        conditions.append('prenom = ?')
        values.append(prenom)
    if nom:
        conditions.append('nom = ?')
        values.append(nom)
    if tel:
        conditions.append('tel = ?')
        values.append(tel)
    if email:
        conditions.append('email = ?')
        values.append(email)

    if conditions:
        query += ' ' + ' AND '.join(conditions)
        cursor.execute(query, tuple(values))
        return cursor.fetchall()
    else:
        return []


# Fonction récupération de tous les contacts
def get_all_contacts():
    cursor.execute('SELECT * FROM contacts')
    return cursor.fetchall()
print(get_all_contacts())