# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

def search(request):
	errors = []
	# request.GET accesses query string parameters
	# GET is used to retrieve & display data. NOT for any server-side changes
	# This checks GET request for 'q' param: 
	# Ensure fail-safe check: if 'q' param = false, before passing query to db
	if 'q' in request.GET:
		q = request.GET['q']
		if len(q)>20:
			errors.append('Please enter at most 20 characters.')
		elif request.GET.get('q'):
			# This gets the query appended to q
			# icontains is a case-insensitive filter
			# Not recommended for large production database, as it can be slow
			# Google for open-source full-text search
			books = Book.objects.filter(title__icontains=q)
			back_link = "http://" + str(request.get_host()+request.path)
			context = {'books': books, 'query': q, 'backlink': back_link}
			# renders template - search_form.html from books > templates
			return render(request, 'books/search_results.html',context)
		else:
			errors.append('Enter a search term.')
	return render(request, 'books/search_form.html',{'errors': errors})