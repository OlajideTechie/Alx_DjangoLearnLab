# relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Function-based view to display a list of books and their authors
def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details along with its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template to render
    context_object_name = 'library'  # Name the context variable for the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  # Get the specific library object
        context['books'] = library.books.all()  # Get all books related to this library using the ManyToMany relationship
        return context