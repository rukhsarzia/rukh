from django.shortcuts import render
from .models import Post

# Create your views here.

# from django.http import HttpResponse

# def home1(request):
#     return HttpResponse("Hello")

def home(request):
    posts = Post.objects.all
    return render(request,'home.html',{"posts":posts})