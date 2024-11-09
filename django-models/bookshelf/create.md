# Create a new book
new_book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print("Created Book:")
print("Title:", new_book.title)
print("Author:", new_book.author)
print("Publication Year:", new_book.publication_year)
print("-----------")
# Expected Output
# Title: 1984
# Author: George Orwell
# Publication Year: 1949