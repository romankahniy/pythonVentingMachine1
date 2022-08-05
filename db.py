import sqlite3

connect = sqlite3.connect('VentingMachine.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Items(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  item_name TEXT,
                  item_price INTEGER,
                  item_count INTEGER);''')
connect.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS Purchases(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  item_id INTEGER,
                  purchases_at DATE);''')
connect.commit()

