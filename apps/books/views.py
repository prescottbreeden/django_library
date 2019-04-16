from django.shortcuts import render, redirect
from .models import Book, Author, Publisher


def index(request):
    context = {
        "books": Book.objects.all(),
        "publishers": Publisher.objects.all()
    }
    return render(request, "books/index.html", context)

def book_view(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id)
    }
    return render(request, "books/view.html", context)


def add_book(request):
    author_fn = request.POST['firstname']
    author_ln = request.POST['lastname']
    newAuthor = Author.objects.create(
        first_name=author_fn, last_name=author_ln)

    title = request.POST['title']
    description = request.POST['description']
    pub_id = request.POST['publisher']

    publisher = Publisher.objects.get(id=pub_id)

    new_book = Book.objects.create(title=title, description=description,
                        author=newAuthor)
    new_book.publishers.add(publisher) 
    return redirect(index)


def add_publisher(request):
    name = request.POST['name']
    Publisher.objects.create(name=name)
    return redirect(index)


def add_relationship(request):
    pass
