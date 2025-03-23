from rest_framework import serializers
from base.models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'year', 'pagesCount', 'ISBN']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id', 'name', 'surname', 'birthday', 'gender', 'nationality', 'books']