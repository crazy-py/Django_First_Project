from django.shortcuts import render , get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Posts
# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")

def post_details(request):
    # query = Posts.objects.get(id=1)  #throw errors
    instance = get_object_or_404(Posts,id=1)
    context_data = {
    'title' : 'Detail Of Post',
    # 'object_list' : query
    'instance': instance
    }
    return render(request, 'detail.html', context_data)

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
