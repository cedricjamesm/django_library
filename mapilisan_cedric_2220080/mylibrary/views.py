from django.shortcuts import render
from .models import Author, Book, BookInstance
# Create your views here.

def home(request):
    contents = {'Book': Book.objects.all()}
    return render(request, 'mylibrary/index.html', contents)

def author(request):
    auth = {'Author': Author.objects.all()}
    return render(request, 'mylibrary/author_list.html', auth)

def details(request, id):
    book_instance = BookInstance.objects.get(id=id)
    return render (request, 'mylibrary/bookInstance.html', {'book_instance': book_instance})