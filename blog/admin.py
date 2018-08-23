from django.contrib import admin
from .models import BlogType, BlogMark, Blog

# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'type_name')

@admin.register(BlogMark)
class BlogMark(admin.ModelAdmin):
	list_display = ('id', 'mark_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('blog_title', 'blog_type', 'blog_mark', 'author', 'created_time', 'last_updated_time')


