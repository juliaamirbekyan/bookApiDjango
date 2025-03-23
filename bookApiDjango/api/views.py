from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from base.models import Book, Author
from rest_framework.decorators import api_view
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import status


@api_view(['GET'])
def Get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_book(request, num):
    book = get_object_or_404(Book, book_id=num)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_book(request, num):
    book = get_object_or_404(Book, book_id=num)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def Get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_author(request, id):
    author = get_object_or_404(Author, author_id=id)
    serializer = AuthorSerializer(author, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_author(request, id):
    author = get_object_or_404(Author, author_id=id)
    author.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def display_books_and_authors(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'display_books_and_authors.html', {'books': books, 'authors': authors})
