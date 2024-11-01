# Delete newly created book
books = Book.objects.get(pk=6)
books.delete()
print(books)

# Expected Output
Book matching query does not exist.
-----------