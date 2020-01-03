from django.views.generic import RedirectView
from django.urls import path, re_path

from blog import views

# app name
# <a href="{% url 'app_name:urlpatterns(name)' %}">
app_name = 'blogpost'
urlpatterns = [
    # path('', views.BlogPostLV.as_view(), name='index'),
    path('', RedirectView.as_view(url='post')),
    
    # TODO name='' means : .html url naming conf 
    path('post/', views.BlogPostLV.as_view(), name='blogpost_list'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.BlogPostDV.as_view(), name='blogpost_detail'),

    path('archive/', views.BlogPostAV.as_view(), name='blogpost_archive'),

    path('archive/<int:year>/', views.BlogPostYAV.as_view(), name='blogpost_year_archive'),

    path('archive/<int:year>/<str:month>/', views.BlogPostMAV.as_view(), name='blogpost_month_archive'),
]
