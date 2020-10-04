from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/<int:movie_id>', views.show_movies, name='showMovies')
]