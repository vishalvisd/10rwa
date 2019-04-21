import psycopg2

dbName = "10rwa.db"
dbUser = "postgres"
dbUserPassword = "postgres"
dbHost = "10rwa"
dbPort = "5432"

connection = psycopg2.connect(f"dbname={dbName} user={dbUser} password={dbUserPassword} host={dbHost} port={dbPort}'")
cursor = connection.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    connection.commit()

def insert(item, quantity, price):
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)", [item, quantity, price])
    connection.commit()

def view():
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    return rows

def delete(item):
    cursor.execute("DELETE FROM store where item=%s", (item, ))
    connection.commit()

def update(item, quantity, price):
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    connection.commit()

create_table()
print(view())
insert('shoe2', 13, 330)
#delete('shoe1')
#update("shoe", 11, 111)
print(view())

connection.close()
