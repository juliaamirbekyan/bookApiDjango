from django.db import models

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    pagesCount = models.BigIntegerField()
    ISBN = models.CharField(max_length=200)

class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birthday = models.BigIntegerField()
    gender = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)