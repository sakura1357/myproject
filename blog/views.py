import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from .models import Blog

# Create your views here.
@require_http_methods(['GET'])
def add_blog(request):
	
	response = {}
	try:
		title = request.GET.get('title')
		author = request.GET.get('author')
		blog_type = request.GET.get('blog_type')
		content = request.GET.get('content')
		blog = Blog()
		blog.title = title
		blog.author = author
		blog.blog_type = blog_type
		blog.content = content
		blog.save()
		response['msg'] = 'SUCCESS'
		response['error_num'] = 0
	except Exception as e:
		response['msg'] = str(e)
		response['error_num'] = 1
	
	return JsonResponse(response)


@require_http_methods(['GET'])
def show_blogs(request):

	response = {}
	try:
		blogList = Blog.objects.all()
		response['list'] = json.loads(serializers.serialize('json', blogList))
		response['msg'] = 'SUCCESS'
		response['error_num'] = 0
	except Exception as e:
		response['msg'] = str(e)
		response['error_num'] = 1

	return JsonResponse(response)




