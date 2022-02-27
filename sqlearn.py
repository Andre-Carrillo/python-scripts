import sqlite3
con = sqlite3.connect('databas.db')

cursor = con.cursor()
# cursor.execute('''CREATE TABLE stocks (date, number1, number2)''')

cursor.execute('''INSERT INTO stocks VALUES (25, 2, 5)''')

cursor.execute('''INSERT INTO stocks VALUES (25, 6, 9)''')
print(list(cursor.execute('''SELECT * FROM stocks''')))

