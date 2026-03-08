import sqlite3

with sqlite3.connect("PracticeDB") as conn:
    cursor = conn.cursor()

    #Creating first table
    #cursor.execute("CREATE TABLE Products (id INTEGER, nombre TEXT, precio INTEGER)")

    #Insert Data into table
    products = [(1, "Impresora", 300), (2, "Raton", 200), (3, "Ordenador", 600)]
    cursor.executemany("INSERT INTO Products VALUES (?,?,?)", products)

    conn.commit()
    
    #Read data from DB
    cursor.execute("SELECT * FROM Products")    
    prods = cursor.fetchall()
    for prod in prods:
        print(prod)

    