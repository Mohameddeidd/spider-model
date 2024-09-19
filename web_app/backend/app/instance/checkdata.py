import sqlite3


conn = sqlite3.connect('mydatabase.db')


cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)


cursor.execute("SELECT * FROM User")
rows = cursor.fetchall()

print("User Table Data:")
for row in rows:
    print(row)


conn.close()
