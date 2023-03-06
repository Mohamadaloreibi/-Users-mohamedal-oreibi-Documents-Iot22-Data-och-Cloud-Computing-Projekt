import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('CREATE TABLE users (username TEXT, password TEXT)')


def connect(param):
    return None