import sqlite3
connection = sqlite3.connect('database.db')
print(connection.total_changes)
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

cursor.execute('INSERT INTO users VALUES (1, "John", 22)')
cursor.execute('INSERT INTO users VALUES (2, "Jane", 21)')
cursor.execute('INSERT INTO users VALUES (3, "Mike", 23)')
connection.commit()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)