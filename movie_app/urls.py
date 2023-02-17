from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('movies/', views.show_all_movies, name='movies'),
    path('movies/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.all_directors, name='directors'),
    path('directors/<int:id_director>', views.show_one_director, name='director'),
    path('acters/', views.all_acters, name='acters'),
    path('acters/<int:id_acter>', views.show_one_acter, name='acter'),

]