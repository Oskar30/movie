from django.shortcuts import render, get_object_or_404
from .models import Movie

def show_all_movies(request):
    template = 'movie_app/all_movies.html'
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, template, context=context)

def show_one_movie(request, slug_movie:str):
    template = 'movie_app/one_movie.html'
    movie = get_object_or_404(Movie, slug=slug_movie)
    context = {'movie': movie}
    return render(request, template, context=context)

def all_directors(request):
    template = 'movie_app/all_directors.html'
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, template, context=context)

    
