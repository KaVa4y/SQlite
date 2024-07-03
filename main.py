import sqlite3

conn = sqlite3.connect("Test.dp")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT NUT NULL,
    grade REAL 
)
''')

cursor.execute('''
INSERT INTO student (name, grade)
VALUES ('Gleb',192.5), ('Sava',160), ('Artem',180)
''')

conn.commit()

cursor.execute('SELECT * FROM student')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()