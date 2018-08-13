import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from .models import Book

# Create your views here.
@require_http_methods(['GET'])
def add_book(request):
	
	response = {}
	try:
		book_name = request.GET.get('book_name')
		author = request.GET.get('author')
		book = Book()
		book.book_name =  book_name
		book.author =  author
		book.save()
		response['msg'] = 'SUCCESS'
		response['error_num'] = 0
	except Exception as e:
		response['msg'] = str(e)
		response['error_num'] = 1
	
	return JsonResponse(response)

@require_http_methods(['GET'])
def show_books(request):

	response = {}
	try:
		books = Book.objects.all()
		response['list'] = json.loads(serializers.serialize('json', books))
		response['msg'] = 'SUCCESS'
		response['error_num'] = 0
	except Exception as e:
		response['msg'] = str(e)
		response['error_num'] = 1

	return JsonResponse(response)




