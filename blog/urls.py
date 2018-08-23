from django.urls import path
from . import views

# start with blog
urlpatterns = [
    path('add_blog/', views.add_blog, name='add_blog'),
    path('show_blogs/', views.show_blogs, name='show_blogs'),
    path('show_blogs_pages/', views.show_blogs_pages, name='show_blogs_pages'),
    path('show_blog_detail/', views.show_blog_detail, name='show_blog_detail'),
]