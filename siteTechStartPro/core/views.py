import csv, io
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category, Product


def home(request):
    return render(request, 'index.html')


def category_upload(request):
    template = "category_upload.html"
    data = Category.objects.all()

    prompt = {
        'order': 'name',
        'categories': data
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = Category.objects.update_or_create(
            name = column[0]
        )
    context = {}
    return render (request, template, context)


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'categories']
    success_url = reverse_lazy('product_list')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'categories']
    success_url = reverse_lazy('product_list')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')