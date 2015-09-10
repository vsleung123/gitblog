#-*- coding: UTF-8 -*-

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from myblog.models import Post

# Create your views here.

def home(request):
    #get all the posts
    post_list = Post.objects.all()
    return render_to_response('home.html',{'post_list':post_list})

def post_page(request,id):
    post = Post.objects.get(id=id)
    return render_to_response('post.html',{'post':post})