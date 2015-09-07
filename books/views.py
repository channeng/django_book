# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

def search_form(request):
	# renders template - search_form.html from books > templates
	return render(request, 'books/search_form.html')

def search(request):
	# request.GET accesses query string parameters
	# GET is used to retrieve & display data. NOT for any server-side changes
	# This checks GET request for 'q' param: 
	# Ensure fail-safe check: if 'q' param = false
	if request.GET.get('q'):
		# str() helps to convert the return value from unicode to string
		q = request.GET['q']
		books = Book.objects.filter(title__icontains=q)
		context = {'books': books, 'query': q}
		return render(request, 'books/search_results.html',context)
	else:
		message = 'You submitted an empty form.'
		return HttpResponse(message)