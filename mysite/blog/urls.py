from django.urls import path, re_path

from blog import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.PostLV.as_view(), name='index'),

    # /blog/post/
    path('post/', views.PostLV.as_view(), name='post_list'),

    # /blog/post/slug-exam/
    # 한국어 처리를 위한 re_path 및 패턴
    # path('post/<slug:slug>/', views.PostDV.as_view(), name='post_detail'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # /blog/archive/2020/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # /blog/archive/2020/nov/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # /blog/archive/2020/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='archive_today_archive'),
]
