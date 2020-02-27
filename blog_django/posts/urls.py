from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('create/',views.post_create),
    path('delete/',views.post_delete),
    path('update/',views.post_update),
    path('', views.post_list),
    path('delete/',views.post_delete),

]
