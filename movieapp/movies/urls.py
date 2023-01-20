from django.urls import path
from . import views

urlpatterns= [
path ("", views.home,name="home"),
path ("movies", views.movies,name="movies"),
path ("movies/<int:id>", views.moviedetails,name="details"),
path ("movies/<str:category>", views.categoryDetails,name="categoryDetails"),
]