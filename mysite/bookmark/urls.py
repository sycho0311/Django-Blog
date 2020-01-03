from django.views.generic import RedirectView
from django.urls import path, re_path

from bookmark import views

# app name
# <a href="{% url 'app_name:urlpatterns(name)' %}">
app_name = 'bookmark'
urlpatterns = [
    # path('', views.BlogPostLV.as_view(), name='index'),
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
]
