import sqlite3

with sqlite3.connect("testDb.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Persona VALUES('Homero', 'J', 'Simpson', 40)")
    conn.commit()


