from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book
from .converters import DateConverter

def books_view(request, pub_date=None):
    template = 'books/books_list.html'

    all_books = Book.objects.all().order_by('pub_date')
    print(all_books)

    if pub_date:
        date_converter = DateConverter()
        pub_date = date_converter.to_python(pub_date)
        filtered_books = all_books.filter(pub_date=pub_date)

        prev_date = all_books.filter(pub_date__lt=pub_date).last()
        next_date = all_books.filter(pub_date__gt=pub_date).first()

        context = {
            'books': filtered_books,
            'prev_date': prev_date.pub_date if prev_date else None,
            'next_date': next_date.pub_date if next_date else None,
            'pub_date': pub_date,
        }
    else:
        paginator = Paginator(all_books, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
        }

    return render(request, template, context)
