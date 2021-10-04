from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.ListView):
    model = Book


class BokListView(generic.ListView):
    model = Book


class BokDetailView(generic.ListView):
    model = Book


class BkListView(generic.ListView):
    model = Book


class BkDetailView(generic.ListView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.ListView):
    model = Author
