# Delete newly created book
from bookshelf.models import Book
book = Book.objects.get(pk=6)
book.delete()
print(books)
# Expected Output
Book matching query does not exist.
-----------