from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView

from blog.models import BlogPost


# Create your views here.
class BlogPostLV(ListView):
    model = BlogPost
    # template_name = 'blog/blogpost_all.html'
    context_object_name = 'blogposts'
    paginate_by = 2


class BlogPostDV(DetailView):
    model = BlogPost
    # template_name = 'blog/blogpost_detail.html'
    context_object_name = 'blogpost'


class BlogPostAV(ArchiveIndexView):
    model = BlogPost
    date_field = 'modify_dt'


class BlogPostYAV(YearArchiveView):
    model = BlogPost
    date_field = 'modify_dt'
    make_object_list = True


class BlogPostMAV(MonthArchiveView):
    model = BlogPost
    date_field = 'modify_dt'

