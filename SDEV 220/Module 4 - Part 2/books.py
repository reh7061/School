import csv
with open('books.csv', 'rt') as csvfile:
    reader = csv.DictReader(csvfile)
    books = list(reader)

print(books)