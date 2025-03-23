from django.shortcuts import render
from base.models import Book, Author

def display_books_and_authors(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'display_books_and_authors.html', {'books': books, 'authors': authors})
