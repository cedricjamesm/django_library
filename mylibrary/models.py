from django.db import models

# Create your models here.

class Author(models.Model):
 
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dateOfBirth =  models.DateField()
 
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
 
class Genre(models.Model):
 
    name = models.CharField(max_length=200)
 
    def __str__(self):
        return self.name
   
class Book(models.Model):
 
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title
   
class BookInstance(models.Model):
 
    status_choice = (("MAINTANANCE", "Maintanance"), 
                     ("BOOKED", "Booked"), 
                     ("AVAILABLE", "Available"), 
                     ("RESERVED", "Reserved"))
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length = 15, choices = status_choice, default="MAINTANANCE")
    dueDate = models.DateField()
 
    def __str__(self):
        return self.book.title