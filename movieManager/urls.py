from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('movies', views.list_movies, name='list_movies'),
    path('movies/<int:movie_id>', views.show_movies, name='showMovies'),
    path('movies<int:movie_id>/delete', views.delete_movie, name='delete_movie'),
]