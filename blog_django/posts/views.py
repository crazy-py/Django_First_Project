from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")

def post_details(request):
    return HttpResponse("<h1>Details</h1>")

def post_update(request):
    return HttpResponse("<h1>Updated</h1>")

def post_list(request):
    query = Posts.objects.all()
    context_data = {
    'title':'My Posts',
    'object_list' : query
    }
    return render(request, 'index.html', context_data)
    # return HttpResponse("<h1>List</h1>")
