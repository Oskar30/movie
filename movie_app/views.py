from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Acter

def index(request):
    template = 'movie_app/index.html'
    movies = Movie.objects.all()
    directors = Director.objects.all()
    context = {'movies': movies,
            'directors': directors
            }
    return render(request, template, context=context)

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
    directors = Director.objects.all()
    context = {'directors': directors}
    return render(request, template, context=context)

def show_one_director(request, id_director:int):
    template = 'movie_app/one_director.html'
    director = Director.objects.get(id = id_director)
    context = {'director': director}
    return render(request, template, context=context)

def all_acters(request):
    template = 'movie_app/all_acters.html'
    acters = Acter.objects.all()
    context = {'acters': acters}
    return render(request, template, context=context)

def show_one_acter(request, id_acter:int):
    template = 'movie_app/one_acter.html'
    acter = Acter.objects.get(id = id_acter)
    context = {'acter': acter}
    return render(request, template, context=context)