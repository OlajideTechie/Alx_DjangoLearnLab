# Retrieve a newly created book
books = Book.objects.get(pk=6)
 print(
...   f"Title: {book.title}\n"
...   f"Author: {book.author}\n"
...   f"Publication Year: {book.publication_year}\n"
...   "---------"
... )
# Expected Output
Title: 1984
Author: George Orwell
Publication Year: 1949
-----------