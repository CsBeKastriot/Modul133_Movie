from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Movie, MovieForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def list_movies(request):
    movie = Movie.objects.all()
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author succsessfully added')
    return render(request, 'MoviesAndStuff/list_Movies.html', {'movieManager': movie, 'form': form})

@login_required()
def show_movies(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm()
    except Movie.DoesNotExist:
        messages.error(request, 'There is no Movie with this ID!')
        return redirect(list_movies)
    form = MovieForm(initial={
        'movie_title': movie.movie_title,
        'movie_genre': movie.movie_genre,
        'movie_year': movie.movie_year,
    })
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie.movie_title = form.cleaned_data['movie_title']
            movie.movie_genre = form.cleaned_data['movie_genre']
            movie.movie_year = form.cleaned_data['movie_year']
            movie.image = form.cleaned_data['image']
            movie.save()
    return render(request, 'MoviesAndStuff/showMovies.html', {'movieManager': movie, 'form': form})

@login_required()
def delete_movie(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        movie.delete()
    except Movie.DoesNotExist:
        messages.error(request, 'There is no auhtor with this ID.')
    return redirect('list_movies')
