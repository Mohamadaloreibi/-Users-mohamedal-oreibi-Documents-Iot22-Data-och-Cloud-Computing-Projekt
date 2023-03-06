import sqlite3 as sql

con = sql.connect("data.db")
cur = con.cursor()
statement = "SELECT username, password FROM users"
cur.execute(statement)
print(cur.fetchall())
