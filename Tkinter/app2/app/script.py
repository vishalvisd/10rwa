import sqlite3

conn  = sqlite3.connect('lite.db')

cur = conn.cursor()


def createTable():
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()


def insertIntoStoreTable(item, quantity, price):
    cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    conn.commit()

def getAllRowsOfStoreTable():
    a = cur.execute("SELECT * FROM store")
    rows = a.fetchall()
    return rows

# createTable()
# insertIntoStoreTable('Bottle', 30, 10.99)
# insertIntoStoreTable('Pipe', 11, 11)

rows = getAllRowsOfStoreTable()
print(rows)

conn.close()