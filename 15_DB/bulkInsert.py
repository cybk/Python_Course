import sqlite3

with sqlite3.connect("testDb.db") as conn:
    cursor = conn.cursor()
    persons = [('Pedro', 'Perez', 'Pereyra', 35), ('Ingrid', 'Cancino', 'Rangel', 40), ('Milady', 'Moreno', 'Garcia', 44)]
    cursor.executemany("INSERT INTO PERSONA VALUES (?, ?, ?, ?)", persons)
    conn.commit()
    