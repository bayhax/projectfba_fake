import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from blog.models import Blogs


class BlogView(View):
    """
    博客信息
    """
    def get(self, request):
        blog_id = request.GET['blog_id']
        blog_id = int(blog_id)
        blog = Blogs.objects.get(id=blog_id)
        return HttpResponse(json.dumps({'blog_date': datetime.datetime.strftime(blog.mod_date, '%Y-%m-%d'),
                                        'blog_title': blog.title, 'blog_author': blog.author,
                                        'blog_description': blog.description, 'blog_keyword': blog.keywords,
                                        'blog_content': blog.content}), content_type="application/json, charset=utf-8")

    def post(self, request):
        pass
