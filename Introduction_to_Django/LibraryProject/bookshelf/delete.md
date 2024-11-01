# Delete newly created book
from bookshelf.models import Book
books = Book.objects.get(pk=6)
books.delete()
print(books)

# Expected Output
Book matching query does not exist.
-----------