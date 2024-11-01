# Update a Book Detail
books = Book.objects.get(pk=6)
books.title = "Nineteen-Eighty-Four"
books.save()
# Print Resukt
 print(
...   f"Title: {book.title}\n"
...   f"Author: {book.author}\n"
...   f"Publication Year: {book.publication_year}\n"
...   "---------"
... )
# Expected Output
Title: Nineteen-Eighty-Four
Author: George Orwell
Publication Year: 1949
-----------