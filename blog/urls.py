from django.urls import path
from . import views

#this matches the root url to the "post_list" view
urlpatterns = [
    path('',views.post_list,name='post_list'),
]