import json
import math
import logging
import datetime
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import  settings
from django.views.decorators.http import require_http_methods
from .models import Blog

logger = logging.getLogger('django')

# 继承Django自带的DjangoJSONEncoder，并重写default方法，格式化datetime字段类型的数据
# 使用参见：https://docs.djangoproject.com/en/2.0/topics/serialization/#serialization-formats-json
class DateTimeEncoder(DjangoJSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime.datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		else:
			return super().default(obj)


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
		# 获取当前请求的是第几页，如果没获取到，则设置为第1页
		current_page_number = request.GET.get('cPage', 1)
		# 如果是技术杂谈或者随心而记，则返回分页后的分类数据
		if request.GET.get('blog_mark'):
			mark_name = request.GET.get('blog_mark')
			blogList = Blog.objects.filter(blog_mark__mark_name = mark_name)

		# 否则则是home页面，返回分页后的所有数据
		else:
			blogList = Blog.objects.all()

		response['list'] = json.loads(serializers.serialize('json', blogList, cls = DateTimeEncoder))
		response['msg'] = 'SUCCESS'
		response['total_count'] = len(blogList)
		response['error_num'] = 0
	except Exception as e:
		response['msg'] = str(e)
		response['error_num'] = 1

	return JsonResponse(response)


@require_http_methods(['GET'])
def show_blogs_pages(request):
	response = {}
	try:
		# 首页|技术杂谈|随心而记 判断
		if request.GET.get('blog_mark'):
			mark_name = request.GET.get('blog_mark')
			blogList = Blog.objects.filter(blog_mark__mark_name = mark_name)
		else:
			blogList = Blog.objects.all()
			
		# 总页数，向上取整
		blog_pages = math.ceil((blogList.count())/settings.EACH_PAGE_BLOGS_NUMBER)

		# 如果没有获取到请求的页数，则返回第1页的数据
		current_page_number = int(request.GET.get('cPage', 1))
		start = (current_page_number - 1) * settings.EACH_PAGE_BLOGS_NUMBER
		end = current_page_number * settings.EACH_PAGE_BLOGS_NUMBER
		if end > blogList.count():
			end	= blogList.count()
		# response['list'] = json.loads(serializers.serialize('json', blogList[start:end]))
		response['list'] = json.loads(serializers.serialize('json', blogList[start:end], cls = DateTimeEncoder))
		response['blog_pages'] = blog_pages
		response['msg'] = 'SUCCESS'
		response['error_num'] = 0
	except Exception as e:
		response['msg'] = str(e)
		response['error_num'] = 1

	return JsonResponse(response)


@require_http_methods(['GET'])
def show_blog_detail(request):
	response = {}
	try:
		if request.GET.get('id'):
			blog = get_object_or_404(Blog, pk = request.GET.get('id'))
			if Blog.objects.filter(created_time__gt = blog.created_time).last():
				previous_blog = Blog.objects.filter(created_time__gt = blog.created_time).last()
				response['previous_blog'] = json.loads(previous_blog.toJSON())
			else:
				response['previous_blog'] = '没有数据'
			if Blog.objects.filter(created_time__lt = blog.created_time).first():
				next_blog = Blog.objects.filter(created_time__lt = blog.created_time).first()
				response['next_blog'] = json.loads(next_blog.toJSON())
			else:
				response['next_blog'] = '没有数据'
			response['blog'] = json.loads(blog.toJSON())			
			response['msg'] = 'SUCCESS'
			response['error_num'] = 0
		else:
			response['msg'] = 'ERROR'
			response['error_num'] = 1
	except Exception as e:
		response['msg'] = str(e)
		response['error_num'] = 1

	return JsonResponse(response)




