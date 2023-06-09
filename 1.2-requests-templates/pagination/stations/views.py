from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    file_path = 'data-398-2018-08-30.csv'
    number_page = request.GET.get('page', 1)
    with open(file_path,'r',encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        bus_stations = list(reader)

    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(number_page)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
         'bus_stations': page,
          'page': page,
    }
    return render(request, 'stations/index.html', context)