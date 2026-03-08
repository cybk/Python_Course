import sqlite3

with sqlite3.connect("testDb.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PERSONA WHERE edad >= 40 ORDER BY nombre DESC")
    persons = cursor.fetchall()
    for person in persons:
        print(person)

    
    