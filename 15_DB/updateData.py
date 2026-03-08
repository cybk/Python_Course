import sqlite3

with sqlite3.connect("testDb.db") as conn:
    cursor = conn.cursor()
    cursor.execute("UPDATE persona SET apellido2 = 'Cogida por Juan' WHERE nombre = 'Ingrid'")

    conn.commit()