import sqlite3

with sqlite3.connect("testDb.db") as conn:
    cursor = conn.cursor()

    cursor.execute("DELETE FROM persona WHERE nombre = 'Pedro'")

    conn.commit()