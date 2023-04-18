from django.shortcuts import render
from .models import Book, BookInce
from django.views.generic import CreateView, DetailView

# Create your views here.


def index_view(request):

    num_books = Book.objects.all()
    num_instances = BookInce.objects.all().count()

    num_instances_avail = BookInce.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avail': num_instances_avail
    }

    return render(request, 'catalog/index.html', context=context)


class BookCreate(CreateView):
    model = Book
    fields = '__all__'

    success_url = ''


class BookDetail(DetailView):
    model = Book
