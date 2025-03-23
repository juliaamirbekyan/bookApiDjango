from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.Get_books),
    path("books/add", views.add_book),
    path("books/update", views.update_book),
    path("books/delete", views.delete_book),
    path("authors/", views.Get_authors),
    path('authors/add', views.add_author),
    path("authors/update", views.update_author),
    path("authors/delete", views.delete_author),
    path('books_and_authors/', views.display_books_and_authors, name="display_books_and_authors"),
]
