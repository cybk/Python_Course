import sqlite3



with sqlite3.connect("testDb.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Persona(nombre TEXT, Apellido1 TEXT, Apellido2 TEXT, Edad INTEGER)")

    conn.commit()