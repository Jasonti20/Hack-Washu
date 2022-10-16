# Import necessary modules

from django.shortcuts import render,get_object_or_404

from django.db.models import *
from searchapp.models import *


# Define function to search book

def SearchView(request):

    # results = []

    # if request.method == "GET":

    #     query = request.GET.get('search')

    #     if query == '':

    #         query = 'None'

    #     # results = Book.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(price__icontains=query) )
    #     results = ""
    return render(request, 'search.html')

def ResultView(request):
    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        result = Rating.objects.filter(Q(Product=query) | Q(Company=query) )
    return render(request, 'result.html', {"objects":result})