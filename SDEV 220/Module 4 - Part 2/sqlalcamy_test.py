import sqlite3
import csv

conn = sqlite3.connect('books.db')
cur  = conn.cursor()

cur.execute('DROP TABLE IF EXISTS books')
cur.execute('''
    CREATE TABLE books (
        title  TEXT,
        author TEXT,
        year   INTEGER
    )
''')
conn.commit()

with open('books2.csv', 'rt') as f:
    reader = csv.DictReader(f)
    to_insert = []
    for row in reader:
        try:
            year = int(row['year'])
        except ValueError:
            year = None
        to_insert.append((row['title'], row['author'], year))

cur.executemany(
    'INSERT INTO books (title, author, year) VALUES (?, ?, ?)',
    to_insert
)
conn.commit()

print("\n16.8 – Titles in alphabetical order:")
for (title,) in cur.execute('SELECT title FROM books ORDER BY title ASC'):
    print("  ", title)
conn.close()
