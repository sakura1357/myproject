from django.urls import path
from . import views

# start with blog
urlpatterns = [
    path('add_blog/', views.add_blog, name='add_blog'),
    path('show_blogs/', views.show_blogs, name='show_blogs'),
]