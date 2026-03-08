#Creates a test Sqlite DB
import sqlite3

conn = sqlite3.connect("testDb.db")
conn.close()