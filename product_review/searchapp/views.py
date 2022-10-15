# Import necessary modules

from django.shortcuts import render,get_object_or_404

from django.db.models import *



# Define function to search book

def search(request):

    # results = []

    # if request.method == "GET":

    #     query = request.GET.get('search')

    #     if query == '':

    #         query = 'None'

    #     # results = Book.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(price__icontains=query) )
    #     results = ""
    return render(request, 'search.html')