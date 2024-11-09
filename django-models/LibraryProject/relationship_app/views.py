from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
from django.shortcuts import render

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      
      book_date = []
      for book in books:
            book_date.append(f"Title: {book.title}, Author: {book.author.name}")
            
            
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html' 
    context_object_name = 'library'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  # Get the Library object
        context['books'] = library.books.all()  # Get all books related to this library
        return context

